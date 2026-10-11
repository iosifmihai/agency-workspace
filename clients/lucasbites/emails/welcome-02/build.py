#!/usr/bin/env python3
"""Lucas Bites, Welcome Email 2: asset builder.

Usage:  python3 build.py        (needs Pillow only, no network)

- Photos dropped into images/ (names from image-prompts.md, .png/.jpg/.jpeg) are
  cut out locally (white or fake-checkerboard background removed), then
  pre-composited on the section colour as opaque images (safe in Outlook).
- Missing photos get a brand-colour placeholder at the final size, so index.html
  never changes: rerun this script after adding photos and the email updates.
- Also builds wave dividers, logos, social icons, drawn arrows and tick icons.

Brand colours only: #FAA61A, #F7ACB4, #86D2DA, #000000, plus white.
"""
import math
import re
import sys
from collections import deque
from io import BytesIO
from pathlib import Path

try:
    from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps
except ImportError:
    sys.exit("Pillow missing. Install it in a venv: python3 -m venv .venv && .venv/bin/pip install Pillow")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]                     # repo root (contains Logo/)
IMAGES = HERE / "images"
ASSETS = HERE / "assets"
LOGO_DIR = ROOT / "Logo"

ORANGE = (250, 166, 26)
PINK = (247, 172, 180)
TURQ = (134, 210, 218)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SS = 4                                     # supersampling factor for smooth edges
JPG_MAX = 200_000                          # bytes, hero
JPG_MAX_SMALL = 110_000                    # bytes, category / ingredient photos
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

# Background removal thresholds (tune here if a photo needs it)
WHITE_MIN = 225        # min channel above this = near-white
SAT_MAX = 14           # max-min channel below this = neutral (no colour)
CHECKER_MIN = 170      # looser "light neutral" threshold when a fake checkerboard is detected
WORK_MAX = 1600        # longest side processed (inputs are 2K)
# Per-image overrides (white_min, sat_max). Flour is white: only pure-white pixels
# count as background, so the flour mound above the black rim survives.
THRESHOLDS = {"img6-faina": (246, 8)}
# Soft shadows under the subject: light neutral greys connected to the white
# background are treated as shadow, not subject. They are rebuilt as a
# semi-transparent black layer, so they darken the brand colour underneath
# instead of showing as a white/grey blob. Not applied to stems in THRESHOLDS.
SHADOW_MIN = 120       # min channel above this (and neutral) can be shadow
SHADOW_SAT = 26        # max-min channel below this = neutral enough for shadow
SHADOW_GAIN = 0.55     # shadow strength (0 = no shadow, 1 = full)
# White subjects (flour) keep strict thresholds, but the shadow pass still runs
# below this fraction of the image height, i.e. under the bowl only.
SHADOW_BELOW = {"img6-faina": 0.60}

report = []


# ---------------------------------------------------------------- helpers
def font(size, bold=True):
    path = FONT_BOLD if bold else FONT_REG
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        try:
            return ImageFont.truetype("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf", size)
        except OSError:
            return ImageFont.load_default(size=size)


def save_jpg(img, path, max_bytes=JPG_MAX):
    """4:4:4 chroma so flat brand backgrounds stay on the exact HTML bgcolor."""
    img = img.convert("RGB")
    for q in range(88, 55, -4):
        buf = BytesIO()
        img.save(buf, "JPEG", quality=q, optimize=True, progressive=True, subsampling=0)
        if buf.tell() <= max_bytes or q <= 60:
            path.write_bytes(buf.getvalue())
            report.append(f"{path.relative_to(HERE)}  {img.width}x{img.height}  q{q}  {buf.tell() // 1024}KB")
            return


def save_png(img, path):
    img.save(path, "PNG", optimize=True)
    report.append(f"{path.relative_to(HERE)}  {img.width}x{img.height}  {path.stat().st_size // 1024}KB")


def wave_mask(w, h, base, amp, periods, phase, fill_below=True):
    """L-mode mask (w x h): 255 on one side of a sine wave, antialiased."""
    W, H = w * SS, h * SS
    pts = []
    steps = 240
    for i in range(steps + 1):
        x = W * i / steps
        y = (base + amp * math.sin(2 * math.pi * periods * i / steps + phase)) * SS
        pts.append((x, y))
    pts += [(W, H), (0, H)] if fill_below else [(W, 0), (0, 0)]
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).polygon(pts, fill=255)
    return m.resize((w, h), Image.LANCZOS)


def centered_text(draw, box, lines, fill=BLACK):
    """lines: list of (text, font). Centred block inside box (x0,y0,x1,y1)."""
    x0, y0, x1, y1 = box
    heights = [draw.textbbox((0, 0), t, font=f)[3] for t, f in lines]
    gap = 12
    total = sum(heights) + gap * (len(lines) - 1)
    y = y0 + (y1 - y0 - total) / 2
    for (t, f), hgt in zip(lines, heights):
        tw = draw.textlength(t, font=f)
        draw.text((x0 + (x1 - x0 - tw) / 2, y), t, font=f, fill=fill)
        y += hgt + gap


def find_input(stem):
    """images/<stem>.png | .jpg | .jpeg (any case)."""
    for p in sorted(IMAGES.glob("*")):
        if p.stem.lower() == stem.lower() and p.suffix.lower() in (".png", ".jpg", ".jpeg"):
            return p
    return None


def sync_html_height(src_path, display_h):
    """Keep the height attribute in index.html in step with the generated image."""
    html = HERE / "index.html"
    if not html.exists():
        return
    text = html.read_text(encoding="utf-8")
    pat = re.compile(r'(src="' + re.escape(src_path) + r'"[^>]*?height=")\d+(")')
    new = pat.sub(lambda m: f"{m.group(1)}{display_h}{m.group(2)}", text)
    if new != text:
        html.write_text(new, encoding="utf-8")


# ---------------------------------------------------------------- cutout (local, no network)
def _and(a, b):
    return ImageChops.multiply(a, b)          # binary masks: 255*255/255 = 255


def _binary(img, test):
    return img.point(lambda v: 255 if test(v) else 0)


def _flood_from_border(cand):
    """Pixels of binary mask `cand` connected to the image border (4-connectivity).
    Pure Python BFS, so run it on a small mask."""
    w, h = cand.size
    src = cand.load()
    out = Image.new("L", (w, h), 0)
    dst = out.load()
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if src[x, y] and not dst[x, y]:
                dst[x, y] = 255
                q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if src[x, y] and not dst[x, y]:
                dst[x, y] = 255
                q.append((x, y))
    while q:
        x, y = q.popleft()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and src[nx, ny] and not dst[nx, ny]:
                dst[nx, ny] = 255
                q.append((nx, ny))
    return out


def cutout(img, name="image", stem=""):
    """Return an RGBA cutout cropped to its content.

    1. If the file already has real transparency, keep it.
    2. Otherwise background = near-white, low-saturation pixels connected to the
       border (flood fill). If the border looks like a fake grey/white
       checkerboard, any light neutral pixel (min channel > CHECKER_MIN) counts.
    3. Erode 1px (kills the white halo), feather ~1px, crop to the alpha bbox.
    """
    img = ImageOps.exif_transpose(img)
    if max(img.size) > WORK_MAX:
        img = ImageOps.contain(img, (WORK_MAX, WORK_MAX), Image.LANCZOS)

    if img.mode in ("RGBA", "LA", "PA") or (img.mode == "P" and "transparency" in img.info):
        rgba = img.convert("RGBA")
        if rgba.getchannel("A").getextrema()[0] < 250:
            report.append(f"  {name}: existing transparency used")
            return rgba.crop(rgba.getchannel("A").getbbox())

    rgb = img.convert("RGB")
    r, g, b = rgb.split()
    mx = ImageChops.lighter(ImageChops.lighter(r, g), b)
    mn = ImageChops.darker(ImageChops.darker(r, g), b)
    sat = ImageChops.subtract(mx, mn)
    white_min, sat_max = THRESHOLDS.get(stem, (WHITE_MIN, SAT_MAX))
    neutral = _binary(sat, lambda v: v < sat_max)

    # checkerboard detection: share of light-grey neutral pixels on the border frame
    w, h = rgb.size
    border = [(x, 0) for x in range(0, w, 4)] + [(x, h - 1) for x in range(0, w, 4)] + \
             [(0, y) for y in range(0, h, 4)] + [(w - 1, y) for y in range(0, h, 4)]
    mnp, satp = mn.load(), sat.load()
    grey = sum(1 for p in border if CHECKER_MIN < mnp[p] <= WHITE_MIN and satp[p] < SAT_MAX)
    checker = grey / len(border) > 0.08
    thr = CHECKER_MIN if checker else white_min
    if checker and stem in THRESHOLDS:
        print(f"WARNING: {name}: fake checkerboard behind a white subject; white parts may be lost. "
              "Regenerate it on plain white.")
    cand = _and(neutral, _binary(mn, lambda v: v > thr))

    # flood fill at 1/4 resolution on cells that are fully candidate ...
    k = 4
    small = cand.reduce(k).point(lambda v: 255 if v >= 250 else 0)
    bg = _flood_from_border(small).resize(cand.size, Image.NEAREST)
    bg = _and(bg, cand)
    # ... then grow it back to full resolution, only through candidate pixels
    for _ in range(2 * k + 2):
        grown = _and(bg.filter(ImageFilter.MaxFilter(3)), cand)
        if grown.getbbox() == bg.getbbox() and ImageChops.difference(grown, bg).getbbox() is None:
            break
        bg = grown

    shadow = None
    if (stem not in THRESHOLDS or stem in SHADOW_BELOW) and not checker:
        # second, looser pass: background plus the soft shadow around the subject
        loose = _and(_binary(sat, lambda v: v < SHADOW_SAT), _binary(mn, lambda v: v > SHADOW_MIN))
        if stem in SHADOW_BELOW:
            cut = int(h * SHADOW_BELOW[stem])
            keep = Image.new("L", (w, h), 0)
            keep.paste(255, (0, cut, w, h))
            loose = _or(_and(loose, keep), bg) if "_or" in globals() else ImageChops.lighter(_and(loose, keep), bg)
        lbg = _and(_flood_from_border(loose.reduce(k).point(lambda v: 255 if v >= 250 else 0))
                   .resize(loose.size, Image.NEAREST), loose)
        for _ in range(2 * k + 2):
            grown = _and(lbg.filter(ImageFilter.MaxFilter(3)), loose)
            if ImageChops.difference(grown, lbg).getbbox() is None:
                break
            lbg = grown
        lum = rgb.convert("L")
        # shadow alpha from how much darker than the white background a pixel is
        shade = lum.point(lambda v: max(0, min(255, int((250 - v) * 255 / 130 * SHADOW_GAIN))))
        shadow = ImageChops.multiply(shade, _and(lbg, ImageOps.invert(bg)))
        bg = lbg

    hard = ImageOps.invert(bg).filter(ImageFilter.MinFilter(3))   # erode 1px
    alpha = hard.filter(ImageFilter.GaussianBlur(0.9))            # feather ~1px
    # de-halo: the outer 3px of the subject still carry white from the old
    # background; replace them with the darkest nearby colour from inside
    band = ImageChops.subtract(hard, hard.filter(ImageFilter.MinFilter(7)))
    rgb = Image.composite(rgb.filter(ImageFilter.MinFilter(5)), rgb, band)
    bbox = alpha.point(lambda v: 255 if v > 24 else 0).getbbox()
    if bbox is None:
        print(f"WARNING: {name}: background removal left nothing, using the full image.")
        return rgb.convert("RGBA")
    if shadow is not None:
        shadow = ImageChops.multiply(shadow.filter(ImageFilter.GaussianBlur(2)), ImageOps.invert(alpha))
        rgb = Image.composite(rgb, Image.new("RGB", rgb.size, (0, 0, 0)), alpha)
        alpha = ImageChops.lighter(alpha, shadow)
        bbox = alpha.point(lambda v: 255 if v > 8 else 0).getbbox()
    out = rgb.convert("RGBA")
    out.putalpha(alpha)
    removed = 1 - (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) / (w * h)
    report.append(f"  {name}: background removed ({'checkerboard' if checker else 'white'} mode, "
                  f"bbox {bbox[2] - bbox[0]}x{bbox[3] - bbox[1]})")
    if removed < 0.02:
        print(f"WARNING: {name}: almost no background found. Is it shot on plain white?")
    return out.crop(bbox)


def placeholder_cutout(w, h, plate, label, sub, food=None):
    """Stylised plate on transparency, so layout and overlap are visible before photos exist."""
    S = 2
    img = Image.new("RGBA", (w * S, h * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    W, H = w * S, h * S
    d.ellipse((W * 0.04, H * 0.30, W * 0.96, H * 0.96), fill=plate + (255,), outline=BLACK + (255,), width=6 * S)
    if food:
        d.rounded_rectangle((W * 0.30, H * 0.10, W * 0.70, H * 0.62), radius=int(W * 0.06),
                            fill=food + (255,), outline=BLACK + (255,), width=6 * S)
    img = img.resize((w, h), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    cy = h * (0.36 if food else 0.63)
    centered_text(d, (0, cy - h * 0.12, w, cy + h * 0.12),
                  [(label, font(max(18, w // 16))), (sub, font(max(13, w // 30), False))],
                  fill=ORANGE if plate == BLACK and not food else BLACK)
    return img


def load_cutout(stem, ph):
    p = find_input(stem)
    if p is not None:
        return cutout(Image.open(p), p.name, stem), "real"
    return ph(), "placeholder"


# ---------------------------------------------------------------- logos
def build_logos():
    src = Image.open(LOGO_DIR / "Logo_LucasBites.png").convert("RGBA")
    w = 360                                                # displayed at 180px
    src.resize((w, round(src.height * w / src.width)), Image.LANCZOS).save(ASSETS / "logo.png", optimize=True)
    report.append(f"assets/logo.png  {w}px wide (shown 180px)")

    # Stripes logo: identical treatment to Email 1 (cropped band, no scaling distortion)
    st = Image.open(LOGO_DIR / "Logo_LucasBites_stripes-nobg.png").convert("RGBA")
    bbox = st.getchannel("A").point(lambda v: 255 if v > 40 else 0).getbbox()
    st = st.crop((0, bbox[1], st.width, bbox[3]))
    cx, half = st.width // 2, 1050
    st = st.crop((cx - half, 0, cx + half, st.height))
    w = 520                                                # displayed at 260px
    st = st.resize((w, round(st.height * w / st.width)), Image.LANCZOS)
    st.save(ASSETS / "logo-stripes.png", optimize=True)
    report.append(f"assets/logo-stripes.png  {w}x{st.height} (shown 260px)")
    sync_html_height("assets/logo-stripes.png", round(st.height / 2))


# ---------------------------------------------------------------- waves
def wave_divider(name, top, bottom, phase, periods=1.25, h=96, amp=20):
    img = Image.new("RGB", (1200, h), top)
    img.paste(Image.new("RGB", (1200, h), bottom), (0, 0), wave_mask(1200, h, h / 2, amp, periods, phase))
    save_png(img, ASSETS / name)


# ---------------------------------------------------------------- hero
def build_hero():
    """IMG1 cutout over a black block whose wave line crosses the lower part of
    the plate, so the cake 'breaks out' into the white story section.
    Baked into one opaque JPG: identical in Outlook, Gmail, Apple Mail."""
    W = 1200
    box_w, box_h = 960, 1200                               # shown at 480 x 600
    src, tag = load_cutout("img1-hero", lambda: placeholder_cutout(
        box_w, box_h, TURQ, "IMG1", "lava cake 4:5", food=ORANGE))
    src = ImageOps.contain(src, (box_w, box_h), Image.LANCZOS)
    top, bottom = 24, 40
    H = top + src.height + bottom
    wave_base = top + round(src.height * 0.74)
    canvas = Image.new("RGB", (W, H), BLACK)
    canvas.paste(Image.new("RGB", (W, H), WHITE), (0, 0), wave_mask(W, H, wave_base, 26, 1.1, 0.6))
    canvas = canvas.convert("RGBA")
    canvas.alpha_composite(src, ((W - src.width) // 2, top))
    save_jpg(canvas, ASSETS / "hero.jpg")
    report[-1] += f"  [{tag}]"
    sync_html_height("assets/hero.jpg", H // 2)


# ---------------------------------------------------------------- cutouts on a flat section colour
def build_on_colour(stem, out_name, size, pad, bg, plate, label, sub):
    """Cutout centred on a square of the section colour, opaque JPG."""
    src, tag = load_cutout(stem, lambda: placeholder_cutout(size, size, plate, label, sub))
    src = ImageOps.contain(src, (size - 2 * pad, size - 2 * pad), Image.LANCZOS)
    canvas = Image.new("RGBA", (size, size), bg + (255,))
    canvas.alpha_composite(src, ((size - src.width) // 2, (size - src.height) // 2))
    save_jpg(canvas, ASSETS / out_name, JPG_MAX_SMALL)
    report[-1] += f"  [{tag}]"


# ---------------------------------------------------------------- UI: arrows, ticks, icons
def stamp_path(d, pts, r, fill=255):
    """Draw a stroke by stamping discs along a polyline: round caps, marker feel."""
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        n = max(1, int(math.hypot(x1 - x0, y1 - y0) / (r * 0.35)))
        for i in range(n + 1):
            t = i / n
            x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
            d.ellipse((x - r, y - r, x + r, y + r), fill=fill)


def build_arrows():
    """Hand-drawn style arrows (Boustan ref): shown 80x48, exported 2x."""
    w, h = 160 * SS, 96 * SS
    m = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(m)
    # cubic bezier from upper right, dipping, ending left with a small upturn
    p0, p1, p2, p3 = (150, 18), (120, 92), (52, 86), (14, 46)
    pts = []
    for i in range(61):
        t = i / 60
        x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]
        y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]
        y += 1.6 * math.sin(t * 13)                       # slight hand wobble
        pts.append((x * SS, y * SS))
    r = 2.6 * SS
    stamp_path(d, pts, r)
    # arrowhead: two strokes at the tip, around the reversed tangent
    tx, ty = pts[-1]
    ax, ay = pts[-5]
    ang = math.atan2(ay - ty, ax - tx)
    for da, ln in ((0.62, 24), (-0.55, 20)):
        a = ang + da
        stamp_path(d, [(tx, ty), (tx + ln * SS * math.cos(a), ty + ln * SS * math.sin(a))], r)
    m = m.resize((w // SS, h // SS), Image.LANCZOS)
    left = Image.new("RGBA", m.size, BLACK + (0,))
    left.putalpha(m)
    save_png(left, ASSETS / "arrow-left.png")
    save_png(ImageOps.mirror(left), ASSETS / "arrow-right.png")


def build_tick():
    n = 48 * SS
    m = Image.new("L", (n, n), 0)
    d = ImageDraw.Draw(m)
    stamp_path(d, [(9 * SS, 25 * SS), (19 * SS, 36 * SS), (40 * SS, 11 * SS)], 3.4 * SS)
    m = m.resize((48, 48), Image.LANCZOS)
    img = Image.new("RGBA", m.size, BLACK + (0,))
    img.putalpha(m)
    save_png(img, ASSETS / "tick.png")


def icon_canvas(n=256):
    return Image.new("L", (n, n), 0), n


def finish_icon(mask, name, size=64):
    mask = mask.resize((size, size), Image.LANCZOS)
    img = Image.new("RGBA", (size, size), BLACK + (0,))
    img.putalpha(mask)
    save_png(img, ASSETS / name)


def build_icons():
    """Same social icons as Email 1 (footer must be identical)."""
    m, n = icon_canvas()
    d = ImageDraw.Draw(m)
    d.ellipse((0, 0, n - 1, n - 1), fill=255)
    d.rounded_rectangle((68, 68, 188, 188), radius=34, outline=0, width=16)
    d.ellipse((99, 99, 157, 157), outline=0, width=16)
    d.ellipse((156, 84, 174, 102), fill=0)
    finish_icon(m, "icon-instagram.png")

    m, n = icon_canvas()
    d = ImageDraw.Draw(m)
    d.ellipse((0, 0, n - 1, n - 1), fill=255)
    d.rectangle((128, 58, 150, 168), fill=0)
    d.ellipse((76, 134, 150, 200), outline=0, width=22)
    d.arc((128, 10, 214, 108), start=95, end=180, fill=0, width=22)
    finish_icon(m, "icon-tiktok.png")

    m, n = icon_canvas()
    d = ImageDraw.Draw(m)
    d.ellipse((0, 0, n - 1, n - 1), fill=255)
    f = font(190)
    tw = d.textlength("f", font=f)
    bb = d.textbbox((0, 0), "f", font=f)
    d.text(((n - tw) / 2 + 6, (n - (bb[3] - bb[1])) / 2 - bb[1] + 18), "f", font=f, fill=0)
    finish_icon(m, "icon-facebook.png")

    m, n = icon_canvas()
    d = ImageDraw.Draw(m)
    d.ellipse((0, 0, n - 1, n - 1), fill=255)
    d.rounded_rectangle((56, 80, 200, 176), radius=28, fill=0)
    d.polygon([(110, 104), (110, 152), (152, 128)], fill=255)
    finish_icon(m, "icon-youtube.png")


# ---------------------------------------------------------------- main
def main():
    ASSETS.mkdir(exist_ok=True)
    IMAGES.mkdir(exist_ok=True)
    build_logos()
    wave_divider("wave-white-black.png", WHITE, BLACK, phase=0.0)
    wave_divider("wave-white-pink.png", WHITE, PINK, phase=3.4, periods=1.4)
    wave_divider("wave-pink-turq.png", PINK, TURQ, phase=1.2, periods=1.2)
    wave_divider("wave-turq-orange.png", TURQ, ORANGE, phase=4.4, periods=1.3)
    wave_divider("wave-orange-white.png", ORANGE, WHITE, phase=1.6, periods=1.2)
    build_hero()
    cats = [
        ("img2-pancakes-crepes", "img2-pancakes-crepes.jpg", ORANGE, "IMG2", "pancakes + crêpes 1:1"),
        ("img3-budinca", "img3-budinca.jpg", TURQ, "IMG3", "budincă 1:1"),
        ("img4-banana-bread", "img4-banana-bread.jpg", ORANGE, "IMG4", "banana bread 1:1"),
        ("img5-pizza", "img5-pizza.jpg", WHITE, "IMG5", "pizza 1:1"),
    ]
    for stem, out, plate, label, sub in cats:                # 560px, shown 280px, on pink
        build_on_colour(stem, out, 560, 24, PINK, plate, label, sub)
    build_on_colour("img6-faina", "img6-faina.jpg", 400, 20, TURQ, BLACK, "IMG6", "făină 1:1")
    build_on_colour("img7-zahar", "img7-zahar.jpg", 400, 20, TURQ, BLACK, "IMG7", "zahăr 1:1")
    build_arrows()
    build_tick()
    build_icons()
    print("Built assets:")
    for line in report:
        print("  " + line)


if __name__ == "__main__":
    main()
