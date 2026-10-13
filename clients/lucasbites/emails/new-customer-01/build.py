#!/usr/bin/env python3
"""Lucas Bites, New Customer Email 1: asset builder.

Usage:  python3 build.py        (needs Pillow only, no network)

- Photos dropped into images/ (names from image-prompts.md, .png/.jpg/.jpeg) are
  cut out locally (plain white background removed, same method as Welcome 3),
  then pre-composited into opaque JPGs:
    * img1-hero: the 3 plates are separated automatically and placed so they
      bleed off the email frame (ref3): pancakes + crepes in the top band
      (under the white header curve), brownie in the bottom band, crossing the
      big pink-to-orange curve.
    * img2 (recipe of the week): stack on black, over a turquoise disc.
    * img3-img5 (recipe cards): overhead plates on black, cut by the email edge
      (zig-zag, ref3).
- Missing photos get placeholders at the final size, so index.html never
  changes: rerun this script after adding photos and the email updates.
- Also builds the big curved section transitions, logos, social icons (same as
  Welcome 1-3) and copies the Akrobat webfont from Welcome 3.
- Ordered-product images are NOT built here: they come from the theMarketer
  product feed ({{ORDER_PRODUCT_IMAGE}}).

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
FONTS_SRC = HERE.parent / "welcome-03" / "assets" / "fonts"

ORANGE = (250, 166, 26)
PINK = (247, 172, 180)
TURQ = (134, 210, 218)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SS = 4                                     # supersampling factor for smooth edges
JPG_MAX_HERO = 200_000                     # bytes per hero band (2 bands, copy.md: hero under 300 KB in total is the aim)
JPG_MAX_ROTW = 260_000                     # recipe of the week (copy.md: under 300 KB)
JPG_MAX_CARD = 120_000                     # recipe card plates (copy.md: circles under 150 KB)
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

# Background removal thresholds (same as Welcome 3; tune here if a photo needs it)
WHITE_MIN = 225
SAT_MAX = 14
CHECKER_MIN = 170
WORK_MAX = 1600
THRESHOLDS = {}        # per-image overrides: {"stem": (white_min, sat_max)}
SHADOW_MIN = 120
SHADOW_SAT = 26
SHADOW_GAIN = 0.40
SHADOW_SAT_BY = {}
# Overhead round plates: the light rim is close to white, so colour-based removal
# eats into it. For these stems the alpha is a clean ellipse fitted to each plate.
ROUND_PLATES = {"img1-hero", "img3-afine", "img4-teanc", "img5-clatite"}
# Side-view plates (convex): bites in the rim are filled with the convex hull of
# the plate zone only (rows at least PLATE_ROW_FRAC of the widest row), not the food.
SIDE_PLATES = {"img2-banane-nuci"}
PLATE_ROW_FRAC = 0.80

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


def save_jpg(img, path, max_bytes):
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
    """L-mode mask (w x h): 255 on one side of a sine curve, antialiased."""
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
    gap = 8
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


def paste_center(canvas, src, cx, cy):
    canvas.alpha_composite(src, (round(cx - src.width / 2), round(cy - src.height / 2)))


def clip_paste(canvas, src, cx, cy):
    """alpha_composite that accepts positions partly outside the canvas (bleed)."""
    x, y = round(cx - src.width / 2), round(cy - src.height / 2)
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    layer.paste(src, (x, y), src)
    canvas.alpha_composite(layer)


def disc_mask(size, box):
    """Antialiased ellipse mask on a canvas of `size`."""
    w, h = size
    m = Image.new("L", (w * SS, h * SS), 0)
    ImageDraw.Draw(m).ellipse([v * SS for v in box], fill=255)
    return m.resize((w, h), Image.LANCZOS)


# ---------------------------------------------------------------- cutout (local, no network)
def _and(a, b):
    return ImageChops.multiply(a, b)


def _binary(img, test):
    return img.point(lambda v: 255 if test(v) else 0)


def _flood_from_border(cand):
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


def _hull(points):
    """Convex hull (monotone chain) of (x, y) points."""
    pts = sorted(set(points))
    if len(pts) < 3:
        return pts
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, up = [], []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def _plate_zone_hull(hard):
    """Mask of the convex hull of the plate zone of a side-view plate."""
    k = 2
    small = hard.reduce(k).point(lambda v: 255 if v > 128 else 0)
    w, h = small.size
    px = small.load()
    spans = {}
    for y in range(h):
        xs = [x for x in range(w) if px[x, y]]
        if xs:
            spans[y] = (xs[0], xs[-1])
    if not spans:
        return None
    widest = max(b - a for a, b in spans.values())
    rows = [y for y, (a, b) in spans.items() if b - a >= PLATE_ROW_FRAC * widest]
    y0 = min(rows)
    pts = []
    for y, (a, b) in spans.items():
        if y >= y0:
            pts += [(a, y), (b, y)]
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).polygon(_hull(pts), fill=255)
    return m.resize(hard.size, Image.NEAREST)


def _plate_ellipses(hard):
    """Clean antialiased ellipse per plate (connected solid region of `hard`).

    The ellipse is the bounding box of the region: rim bites from the colour
    threshold sit inside it, while the extreme points of the rim survive."""
    k = 4
    small = hard.reduce(k).point(lambda v: 255 if v > 128 else 0)
    w, h = small.size
    px = small.load()
    seen = bytearray(w * h)
    W, H = hard.size
    m = Image.new("L", (W * 2, H * 2), 0)
    dr = ImageDraw.Draw(m)
    found = 0
    for y0 in range(h):
        for x0 in range(w):
            if not px[x0, y0] or seen[y0 * w + x0]:
                continue
            q = deque([(x0, y0)])
            seen[y0 * w + x0] = 1
            x1 = x2 = x0
            y1 = y2 = y0
            n = 0
            while q:
                x, y = q.popleft()
                n += 1
                x1, x2, y1, y2 = min(x1, x), max(x2, x), min(y1, y), max(y2, y)
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= nx < w and 0 <= ny < h and px[nx, ny] and not seen[ny * w + nx]:
                        seen[ny * w + nx] = 1
                        q.append((nx, ny))
            if n < 0.02 * w * h:
                continue
            # exact bbox at full resolution inside this region's window
            win = (max(0, x1 * k - k), max(0, y1 * k - k), min(W, (x2 + 1) * k + k), min(H, (y2 + 1) * k + k))
            bb = hard.crop(win).point(lambda v: 255 if v > 128 else 0).getbbox()
            ex1, ey1, ex2, ey2 = win[0] + bb[0], win[1] + bb[1], win[0] + bb[2], win[1] + bb[3]
            dr.ellipse((ex1 * 2 + 2, ey1 * 2 + 2, ex2 * 2 - 2, ey2 * 2 - 2), fill=255)
            found += 1
    return m.resize((W, H), Image.LANCZOS), found


def cutout(img, name="image", stem=""):
    """RGBA cutout cropped to content (same method as Welcome 2 and 3).

    1. Real transparency in the file is kept.
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

    shadow = None
    if not checker:
        ssat = SHADOW_SAT_BY.get(stem, SHADOW_SAT)
        loose = _and(_binary(sat, lambda v: v < ssat), _binary(mn, lambda v: v > SHADOW_MIN))
        lbg = _and(_flood_from_border(loose.reduce(k).point(lambda v: 255 if v >= 250 else 0))
                   .resize(loose.size, Image.NEAREST), loose)
        lbg = _grow(lbg, loose, 20)
        lum = rgb.convert("L")
        shade = lum.point(lambda v: max(0, min(255, int((250 - v) * 255 / 130 * SHADOW_GAIN))))
        shadow = ImageChops.multiply(shade, _and(lbg, ImageOps.invert(bg)))
        bg = lbg

    hard = ImageOps.invert(bg).filter(ImageFilter.MinFilter(3))
    plates = 0
    if stem in ROUND_PLATES:
        ell, plates = _plate_ellipses(hard)
    if stem in SIDE_PLATES:
        zone = _plate_zone_hull(hard)
        if zone is not None:
            hard = ImageChops.lighter(hard, zone)
    if plates:
        # original pixels inside the fitted ellipse, no edge erosion
        hard = ell.point(lambda v: 255 if v > 128 else 0)
        alpha = ell
    else:
        alpha = hard.filter(ImageFilter.GaussianBlur(0.9))
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
    report.append(f"  {name}: background removed ({'checkerboard' if checker else 'white'} mode"
                  f"{f', {plates} round plate(s)' if plates else ''}, "
                  f"bbox {bbox[2] - bbox[0]}x{bbox[3] - bbox[1]})")
    if removed < 0.02:
        print(f"WARNING: {name}: almost no background found. Is it shot on plain white?")
    return out.crop(bbox)


def split_plates(rgba, n=3):
    """Separate the hero cutout into its plates (connected solid regions).

    Returns up to n RGBA crops (largest first), each with its centroid in the
    source image, or [] if the plates touch and cannot be separated."""
    k = 4
    solid = rgba.getchannel("A").reduce(k).point(lambda v: 255 if v > 160 else 0)
    w, h = solid.size
    px = solid.load()
    seen = bytearray(w * h)
    comps = []
    for y0 in range(h):
        for x0 in range(w):
            if not px[x0, y0] or seen[y0 * w + x0]:
                continue
            q = deque([(x0, y0)])
            seen[y0 * w + x0] = 1
            pts = []
            while q:
                x, y = q.popleft()
                pts.append((x, y))
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= nx < w and 0 <= ny < h and px[nx, ny] and not seen[ny * w + nx]:
                        seen[ny * w + nx] = 1
                        q.append((nx, ny))
            comps.append(pts)
    comps = [c for c in comps if len(c) > 0.02 * w * h]
    comps.sort(key=len, reverse=True)
    if len(comps) != n:
        return []
    out = []
    for pts in comps:
        m = Image.new("L", (w, h), 0)
        mp = m.load()
        for x, y in pts:
            mp[x, y] = 255
        m = m.filter(ImageFilter.MaxFilter(9)).resize(rgba.size, Image.BILINEAR)   # ~16px margin for the shadow
        piece = rgba.copy()
        piece.putalpha(ImageChops.multiply(rgba.getchannel("A"), m))
        bb = piece.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
        cx = sum(p[0] for p in pts) / len(pts) * k
        cy = sum(p[1] for p in pts) / len(pts) * k
        out.append((piece.crop(bb), (cx, cy)))
    return out


# ---------------------------------------------------------------- placeholders (no photo yet)
def placeholder_plate_top(d, label, sub, food=ORANGE, plate=WHITE):
    """Overhead plate: light plate, black outline, food disc in a brand colour."""
    S = 2
    D = d * S
    img = Image.new("RGBA", (D, D), (0, 0, 0, 0))
    dr = ImageDraw.Draw(img)
    dr.ellipse((4 * S, 4 * S, D - 4 * S, D - 4 * S), fill=plate + (255,), outline=BLACK + (255,), width=4 * S)
    dr.ellipse((D * 0.22, D * 0.22, D * 0.78, D * 0.78), fill=food + (255,), outline=BLACK + (255,), width=4 * S)
    img = img.resize((d, d), Image.LANCZOS)
    dr = ImageDraw.Draw(img)
    centered_text(dr, (d * 0.2, d * 0.36, d * 0.8, d * 0.64),
                  [(label, font(max(16, d // 11))), (sub, font(max(11, d // 26), False))])
    return img


def placeholder_stack(w, h, label, sub):
    """Side view: plate + stack, so the layout is visible before the photo exists."""
    S = 2
    W, H = w * S, h * S
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse((W * 0.04, H * 0.62, W * 0.96, H * 0.96), fill=WHITE + (255,), outline=BLACK + (255,), width=4 * S)
    for i in range(4):
        y = H * (0.60 - i * 0.12)
        d.rounded_rectangle((W * 0.22, y, W * 0.78, y + H * 0.13), radius=int(H * 0.06),
                            fill=ORANGE + (255,), outline=BLACK + (255,), width=4 * S)
    img = img.resize((w, h), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    centered_text(d, (0, h * 0.30, w, h * 0.62), [(label, font(max(18, w // 16))), (sub, font(max(12, w // 34), False))])
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

    # Stripes logo: identical treatment to Welcome 1-3 (footer must match)
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
    found = list(FONTS_SRC.glob("Akrobat-*.woff*"))
    if not found:
        print(f"WARNING: no Akrobat webfont found in {FONTS_SRC}")
    for f in found:
        shutil.copy2(f, dst / f.name)
        report.append(f"assets/fonts/{f.name}  (copied from welcome-03)")


# ---------------------------------------------------------------- big curves (ref3)
def curve(name, top, bottom, phase, periods=0.5, h=128, amp=40):
    """Section transition: one big curve (half a sine period), not the short
    waves of Welcome 1-3. 1200 x 128, shown 600 x 64."""
    img = Image.new("RGB", (1200, h), top)
    img.paste(Image.new("RGB", (1200, h), bottom), (0, 0), wave_mask(1200, h, h / 2, amp, periods, phase))
    save_png(img, ASSETS / name)


# ---------------------------------------------------------------- hero (img1 split in two bands)
HERO_PH = {
    "A": ("IMG1 A", "pancakes cu afine", ORANGE),
    "B": ("IMG1 B", "clătite rulate", TURQ),
    "C": ("IMG1 C", "brownie cu fructe", PINK),
}


def hero_plates():
    """Return {'A': pancakes, 'B': crepes, 'C': brownie} RGBA plates and a tag."""
    p = find_input("img1-hero")
    if p is None:
        return {k: placeholder_plate_top(420, *v) for k, v in HERO_PH.items()}, "placeholder"
    cut = cutout(Image.open(p), p.name, "img1-hero")
    parts = split_plates(cut, 3)
    if not parts:
        print("WARNING: img1-hero: could not separate exactly 3 plates (do they touch?). "
              "Using the whole photo in the bottom band; top band left without plates.")
        return {"C": cut}, "real, not split"
    left = min(parts, key=lambda t: t[1][0])                  # leftmost plate = pancakes (A)
    rest = sorted([t for t in parts if t is not left], key=lambda t: t[1][1])
    return {"A": left[0], "B": rest[0][0], "C": rest[1][0]}, "real"


def build_hero(plates, tag):
    # Top band: header white curve over the pink hero; plates A and B bleed off
    # the top corners and the email sides, "under" the header curve.
    W, H = 1200, 440
    top = Image.new("RGBA", (W, H), PINK + (255,))
    for key, d, cx, cy in (("A", 420, 60, 170), ("B", 400, 1150, 200)):
        if key in plates:
            clip_paste(top, ImageOps.contain(plates[key], (d, d), Image.LANCZOS), cx, cy)
    white = Image.new("RGBA", (W, H), WHITE + (255,))
    top.paste(white, (0, 0), wave_mask(W, H, 46, 44, 0.5, 0.0, fill_below=False))
    save_jpg(top, ASSETS / "hero-top.jpg", JPG_MAX_HERO)
    report[-1] += f"  [{tag}]"
    sync_html_height("assets/hero-top.jpg", H // 2)

    # Bottom band: big pink-to-orange curve; brownie plate C crosses it and
    # bleeds off the right edge, flowing into the orange products section.
    W, H = 1200, 600
    bot = Image.new("RGBA", (W, H), PINK + (255,))
    bot.paste(Image.new("RGBA", (W, H), ORANGE + (255,)), (0, 0), wave_mask(W, H, 350, 90, 0.5, math.pi / 2))
    if "C" in plates:
        d = 520 if tag != "real, not split" else 560
        clip_paste(bot, ImageOps.contain(plates["C"], (d, d), Image.LANCZOS), 1010, 300)
    save_jpg(bot, ASSETS / "hero-bottom.jpg", JPG_MAX_HERO)
    report[-1] += f"  [{tag}]"
    sync_html_height("assets/hero-bottom.jpg", H // 2)


# ---------------------------------------------------------------- recipe of the week (img2)
def build_rotw():
    """Stack (side view) on black over a turquoise disc. 1200 x 800, shown 600 x 400."""
    W, H = 1200, 800
    canvas = Image.new("RGBA", (W, H), BLACK + (255,))
    canvas.paste(Image.new("RGBA", (W, H), TURQ + (255,)), (0, 0), disc_mask((W, H), (450, 50, 1150, 750)))
    src, tag = load_cutout("img2-banane-nuci", lambda: placeholder_stack(640, 600, "IMG2", "banane și nuci, lateral"))
    src = ImageOps.contain(src, (720, 640), Image.LANCZOS)
    paste_center(canvas, src, 700, 430)
    save_jpg(canvas, ASSETS / "rotw.jpg", JPG_MAX_ROTW)
    report[-1] += f"  [{tag}]"
    sync_html_height("assets/rotw.jpg", H // 2)


# ---------------------------------------------------------------- zig-zag recipe cards (img3-img5)
def build_card(stem, out_name, side, label, sub, food):
    """Overhead plate on black, cut by the email edge on `side` (ref3 zig-zag).
    560 x 520, shown 280 x 260."""
    W, H = 560, 520
    canvas = Image.new("RGBA", (W, H), BLACK + (255,))
    src, tag = load_cutout(stem, lambda: placeholder_plate_top(480, label, sub, food))
    src = ImageOps.contain(src, (480, 480), Image.LANCZOS)
    clip_paste(canvas, src, 170 if side == "left" else W - 170, H / 2)
    save_jpg(canvas, ASSETS / out_name, JPG_MAX_CARD)
    report[-1] += f"  [{tag}]"
    sync_html_height(f"assets/{out_name}", H // 2)


# ---------------------------------------------------------------- social icons (same as Welcome 1-3)
def icon_canvas(n=256):
    return Image.new("L", (n, n), 0), n


def finish_icon(mask, name, size=64):
    mask = mask.resize((size, size), Image.LANCZOS)
    img = Image.new("RGBA", (size, size), BLACK + (0,))
    img.putalpha(mask)
    save_png(img, ASSETS / name)


def build_icons():
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
    # big curves between sections (S2 -> S3 -> S4 -> S5 -> S6 -> footer)
    curve("curve-orange-white.png", ORANGE, WHITE, phase=0.0)
    curve("curve-white-black.png", WHITE, BLACK, phase=math.pi)
    curve("curve-black-pink.png", BLACK, PINK, phase=math.pi / 2, periods=0.5)
    curve("curve-pink-turq.png", PINK, TURQ, phase=0.0)
    curve("curve-turq-white.png", TURQ, WHITE, phase=-math.pi / 2, periods=0.5)
    plates, tag = hero_plates()
    build_hero(plates, tag)
    build_rotw()
    cards = [   # side = edge the plate bleeds off; zig-zag left, right, left
        ("img3-afine", "card1-afine.jpg", "left", "IMG3", "pancakes cu afine", TURQ),
        ("img4-teanc", "card2-teanc.jpg", "right", "IMG4", "teanc, de sus", ORANGE),
        ("img5-clatite", "card3-clatite.jpg", "left", "IMG5", "clătite rulate", PINK),
    ]
    for stem, out, side, label, sub, food in cards:
        build_card(stem, out, side, label, sub, food)
    build_icons()
    print("Built assets:")
    for line in report:
        print("  " + line)


if __name__ == "__main__":
    main()
