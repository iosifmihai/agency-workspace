#!/usr/bin/env python3
"""Lucas Bites, Welcome Email 3: asset builder.

Usage:  python3 build.py        (needs Pillow only, no network)

- Photos dropped into images/ (names from image-prompts.md, .png/.jpg/.jpeg) are
  cut out locally (white or fake-checkerboard background removed), then
  pre-composited as opaque images: the hero over the turquoise-to-white wave,
  the product photos on rounded colour tiles (corners baked in, white outside,
  so they stay rounded in Outlook).
- Missing photos get a brand-colour placeholder at the final size, so index.html
  never changes: rerun this script after adding photos and the email updates.
- Also builds wave dividers, logos, social icons and star rows (full + empty
  stars, so a 4-star review shows 4), and copies the Akrobat webfont from Email 2.
- UGC photos are NOT built here: they are HTML placeholders in index.html until
  real customer photos (with consent) replace them.

Brand colours only: #FAA61A, #F7ACB4, #86D2DA, #000000, plus white.
"""
import math
import re
import shutil
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
FONTS_SRC = HERE.parent / "welcome-02" / "assets" / "fonts"

ORANGE = (250, 166, 26)
PINK = (247, 172, 180)
TURQ = (134, 210, 218)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLATE = (24, 24, 24)                       # placeholder plate (matte black look)

SS = 4                                     # supersampling factor for smooth edges
JPG_MAX = 300_000                          # bytes, hero (copy.md: hero under 300 KB)
JPG_MAX_SMALL = 120_000                    # bytes, product tiles (copy.md: under 250 KB)
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

# Background removal thresholds (tune here if a photo needs it)
WHITE_MIN = 225        # min channel above this = near-white
SAT_MAX = 14           # max-min channel below this = neutral (no colour)
CHECKER_MIN = 170      # looser "light neutral" threshold when a fake checkerboard is detected
WORK_MAX = 1600        # longest side processed (inputs are 2K)
THRESHOLDS = {}        # per-image overrides: {"stem": (white_min, sat_max)}
# Images where the white background is also enclosed by the subject (the gap in
# the middle of the four hero plates): large white areas not connected to the
# border are removed too. Only blobs wider than ~ENCLOSED_MIN px count, so small
# highlights on butter or syrup survive.
ENCLOSED = {"img1-hero"}
ENCLOSED_MIN = 15
# Soft shadows under the plate are rebuilt as a semi-transparent black layer,
# so they darken the tile colour instead of showing as a white/grey blob.
SHADOW_MIN = 120
SHADOW_SAT = 26
SHADOW_GAIN = 0.40
# Warm-tinted shadows (hero: beige bands beside the plates) need a looser neutral test.
SHADOW_SAT_BY = {"img1-hero": 44}

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
    gap = 10
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
    """Pixels of binary mask `cand` connected to the image border (4-connectivity)."""
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


def _grow(seed, through, k=4):
    for _ in range(2 * k + 2):
        grown = _and(seed.filter(ImageFilter.MaxFilter(3)), through)
        if ImageChops.difference(grown, seed).getbbox() is None:
            break
        seed = grown
    return seed


def _enclosed(cand):
    """Large candidate-background blobs anywhere in the image (not only at the border)."""
    core = cand.filter(ImageFilter.MinFilter(ENCLOSED_MIN))       # survives only in big blobs
    grown = core
    for _ in range(ENCLOSED_MIN):                                  # grow back inside the blob
        nxt = _and(grown.filter(ImageFilter.MaxFilter(3)), cand)
        if ImageChops.difference(nxt, grown).getbbox() is None:
            break
        grown = nxt
    return grown


def cutout(img, name="image", stem=""):
    """Return an RGBA cutout cropped to its content (same method as Email 2).

    1. If the file already has real transparency, keep it.
    2. Otherwise background = near-white, low-saturation pixels connected to the
       border (flood fill). Fake grey/white checkerboards are detected too.
    3. Soft shadow kept as semi-transparent black; erode 1px, feather ~1px, crop.
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

    w, h = rgb.size
    border = [(x, 0) for x in range(0, w, 4)] + [(x, h - 1) for x in range(0, w, 4)] + \
             [(0, y) for y in range(0, h, 4)] + [(w - 1, y) for y in range(0, h, 4)]
    mnp, satp = mn.load(), sat.load()
    grey = sum(1 for p in border if CHECKER_MIN < mnp[p] <= WHITE_MIN and satp[p] < SAT_MAX)
    checker = grey / len(border) > 0.08
    thr = CHECKER_MIN if checker else white_min
    cand = _and(neutral, _binary(mn, lambda v: v > thr))

    k = 4
    small = cand.reduce(k).point(lambda v: 255 if v >= 250 else 0)
    bg = _and(_flood_from_border(small).resize(cand.size, Image.NEAREST), cand)
    bg = _grow(bg, cand, k)
    if stem in ENCLOSED:
        bg = ImageChops.lighter(bg, _enclosed(cand))

    shadow = None
    if not checker:
        ssat = SHADOW_SAT_BY.get(stem, SHADOW_SAT)
        loose = _and(_binary(sat, lambda v: v < ssat), _binary(mn, lambda v: v > SHADOW_MIN))
        lbg = _and(_flood_from_border(loose.reduce(k).point(lambda v: 255 if v >= 250 else 0))
                   .resize(loose.size, Image.NEAREST), loose)
        lbg = _grow(lbg, loose, 20)   # long reach: wide soft shadows are thin in the 1/4 flood
        if stem in ENCLOSED:
            lbg = ImageChops.lighter(lbg, _enclosed(loose))
        lum = rgb.convert("L")
        shade = lum.point(lambda v: max(0, min(255, int((250 - v) * 255 / 130 * SHADOW_GAIN))))
        shadow = ImageChops.multiply(shade, _and(lbg, ImageOps.invert(bg)))
        bg = lbg

    hard = ImageOps.invert(bg).filter(ImageFilter.MinFilter(3))   # erode 1px
    alpha = hard.filter(ImageFilter.GaussianBlur(0.9))            # feather ~1px
    band = ImageChops.subtract(hard, hard.filter(ImageFilter.MinFilter(7)))
    rgb = Image.composite(rgb.filter(ImageFilter.MinFilter(5)), rgb, band)   # de-halo
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


# ---------------------------------------------------------------- placeholders (no photo yet)
def placeholder_plate(w, h, label, sub, food=ORANGE):
    """One stylised black plate seen from the side, so layout is visible before photos exist."""
    S = 2
    W, H = w * S, h * S
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse((W * 0.04, H * 0.52, W * 0.96, H * 0.94), fill=PLATE + (255,), outline=BLACK + (255,), width=4 * S)
    d.rounded_rectangle((W * 0.26, H * 0.20, W * 0.74, H * 0.70), radius=int(W * 0.08),
                        fill=food + (255,), outline=BLACK + (255,), width=5 * S)
    img = img.resize((w, h), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    centered_text(d, (0, h * 0.30, w, h * 0.60),
                  [(label, font(max(18, w // 14))), (sub, font(max(12, w // 28), False))])
    return img


def placeholder_hero(n):
    """Four black plates 2 x 2, seen from above."""
    S = 2
    N = n * S
    img = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    r = N * 0.245
    foods = [ORANGE, PINK, TURQ, ORANGE]
    for i, (cx, cy) in enumerate(((0.26, 0.26), (0.74, 0.26), (0.26, 0.74), (0.74, 0.74))):
        x, y = cx * N, cy * N
        d.ellipse((x - r, y - r, x + r, y + r), fill=PLATE + (255,), outline=BLACK + (255,), width=4 * S)
        d.ellipse((x - r * 0.55, y - r * 0.55, x + r * 0.55, y + r * 0.55), fill=foods[i] + (255,),
                  outline=BLACK + (255,), width=4 * S)
    img = img.resize((n, n), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    centered_text(d, (0, n * 0.44, n, n * 0.56), [("IMG1", font(n // 18)), ("4 farfurii, de sus", font(n // 40, False))],
                  fill=BLACK)
    return img


def load_cutout(stem, ph):
    p = find_input(stem)
    if p is not None:
        return cutout(Image.open(p), p.name, stem), "real"
    return ph(), "placeholder"


# ---------------------------------------------------------------- logos, fonts
def build_logos():
    src = Image.open(LOGO_DIR / "Logo_LucasBites.png").convert("RGBA")
    w = 360                                                # displayed at 180px
    src = src.resize((w, round(src.height * w / src.width)), Image.LANCZOS)
    src.save(ASSETS / "logo.png", optimize=True)
    report.append(f"assets/logo.png  {w}x{src.height} (shown 180px)")
    sync_html_height("assets/logo.png", round(src.height / 2))

    # Stripes logo: identical treatment to Email 1 and 2 (footer must match)
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


def copy_fonts():
    dst = ASSETS / "fonts"
    dst.mkdir(exist_ok=True)
    for f in FONTS_SRC.glob("Akrobat-*.woff*"):
        shutil.copy2(f, dst / f.name)
        report.append(f"assets/fonts/{f.name}  (copied from welcome-02)")


# ---------------------------------------------------------------- waves
def wave_divider(name, top, bottom, phase, periods=1.25, h=96, amp=20):
    img = Image.new("RGB", (1200, h), top)
    img.paste(Image.new("RGB", (1200, h), bottom), (0, 0), wave_mask(1200, h, h / 2, amp, periods, phase))
    save_png(img, ASSETS / name)


# ---------------------------------------------------------------- hero
def build_hero():
    """IMG1 (4 plates, top-down) over turquoise; the turquoise-to-white wave crosses
    the lower third of the plates, so they 'flow' into the white bestsellers section.
    One opaque JPG 1200 x 1040 (shown 600 x 520)."""
    W, H = 1200, 1040
    box = 940
    src, tag = load_cutout("img1-hero", lambda: placeholder_hero(box))
    src = ImageOps.contain(src, (box, box), Image.LANCZOS)
    top = 20
    wave_base = top + round(src.height * 0.70)
    canvas = Image.new("RGB", (W, H), TURQ)
    canvas.paste(Image.new("RGB", (W, H), WHITE), (0, 0), wave_mask(W, H, wave_base, 28, 1.1, 0.9))
    canvas = canvas.convert("RGBA")
    canvas.alpha_composite(src, ((W - src.width) // 2, top))
    save_jpg(canvas, ASSETS / "hero.jpg")
    report[-1] += f"  [{tag}]"


# ---------------------------------------------------------------- product tiles
def build_tile(stem, out_name, tile_colour, label, sub, size=492, radius=28, pad=34):
    """Cutout centred on a rounded colour tile; outside the corners is white (card
    background), so the rounding survives Outlook. Opaque JPG, shown 246 x 246."""
    src, tag = load_cutout(stem, lambda: placeholder_plate(size - 2 * pad, size - 2 * pad, label, sub))
    src = ImageOps.contain(src, (size - 2 * pad, size - 2 * pad), Image.LANCZOS)
    canvas = Image.new("RGBA", (size, size), WHITE + (255,))
    m = Image.new("L", (size * SS, size * SS), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, size * SS - 1, size * SS - 1), radius=radius * SS, fill=255)
    canvas.paste(Image.new("RGBA", (size, size), tile_colour + (255,)), (0, 0), m.resize((size, size), Image.LANCZOS))
    canvas.alpha_composite(src, ((size - src.width) // 2, (size - src.height) // 2))
    save_jpg(canvas, ASSETS / out_name, JPG_MAX_SMALL)
    report[-1] += f"  [{tag}]"


# ---------------------------------------------------------------- stars
def star_points(cx, cy, r_out, r_in, n=5):
    pts = []
    for i in range(2 * n):
        r = r_out if i % 2 == 0 else r_in
        a = -math.pi / 2 + i * math.pi / n
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def build_stars(name, colour, full, total=5, star=36, gap=5, halo=None):
    """Row of `total` stars, the first `full` filled, the rest outlined (empty).
    Exported at 2x. `halo`: thin outline colour around each star (white on the
    black stars, so they survive a dark-mode inversion of the white cards)."""
    w = total * star + (total - 1) * gap
    h = star
    W, H = w * SS, h * SS
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for i in range(total):
        cx = (i * (star + gap) + star / 2) * SS
        cy = (h / 2 + star * 0.04) * SS
        ro, ri = star * 0.48 * SS, star * 0.20 * SS
        if halo:
            d.polygon(star_points(cx, cy, ro + 2 * SS, ri + 1.2 * SS), fill=halo + (255,))
        pts = star_points(cx, cy, ro, ri)
        d.polygon(pts, fill=colour + (255,))
        if i >= full:   # empty star: punch the inside out, leaving a ~3px outline
            d.polygon(star_points(cx, cy, ro - 3.4 * SS, ri - 1.5 * SS), fill=(0, 0, 0, 0))
    img = img.resize((w, h), Image.LANCZOS)
    save_png(img, ASSETS / name)


# ---------------------------------------------------------------- social icons
def icon_canvas(n=256):
    return Image.new("L", (n, n), 0), n


def finish_icon(mask, name, size=64):
    mask = mask.resize((size, size), Image.LANCZOS)
    img = Image.new("RGBA", (size, size), BLACK + (0,))
    img.putalpha(mask)
    save_png(img, ASSETS / name)


def build_icons():
    """Same social icons as Email 1 and 2 (footer must be identical)."""
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
    copy_fonts()
    wave_divider("wave-white-turq.png", WHITE, TURQ, phase=2.2, periods=1.15)
    wave_divider("wave-white-black.png", WHITE, BLACK, phase=4.1, periods=1.35)
    wave_divider("wave-black-orange.png", BLACK, ORANGE, phase=0.8, periods=1.2)
    wave_divider("wave-orange-pink.png", ORANGE, PINK, phase=3.0, periods=1.4)
    wave_divider("wave-pink-white.png", PINK, WHITE, phase=5.2, periods=1.1)
    build_hero()
    tiles = [   # tile colour travels with the product, whatever the card order
        ("img2-buttermilk", "img2-buttermilk.jpg", PINK, "IMG2", "Buttermilk, lateral"),
        ("img3-classic", "img3-classic.jpg", ORANGE, "IMG3", "Classic, 45 grade"),
        ("img4-pizza", "img4-pizza.jpg", TURQ, "IMG4", "pizza, 30 grade"),
        ("img5-brownie", "img5-brownie.jpg", PINK, "IMG5", "brownie, lateral"),
    ]
    for stem, out, colour, label, sub in tiles:
        build_tile(stem, out, colour, label, sub)
    # star rows (2x): product rating + review stars on white cards, big row on black
    build_stars("stars-black-5.png", BLACK, 5, halo=WHITE)
    build_stars("stars-black-4.png", BLACK, 4, halo=WHITE)
    build_stars("stars-orange-5.png", ORANGE, 5, star=50, gap=7)
    build_icons()
    print("Built assets:")
    for line in report:
        print("  " + line)
    # self-contained copies for Figma import (images + fonts embedded)
    sys.path.insert(0, str(HERE.parent / "tools"))
    from figma_export import export
    export(HERE)


if __name__ == "__main__":
    main()
