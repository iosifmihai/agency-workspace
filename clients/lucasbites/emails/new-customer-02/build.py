#!/usr/bin/env python3
"""Lucas Bites, New Customer Email 2: asset builder (Pillow only, no network).

Run by Claude after the food photos land in images/ (names from image-prompts.md,
.png/.jpg/.jpeg). Missing photos get placeholders at the final size, so
index.html never changes.

- Food photos (Higgsfield, plain white background) are cut out locally with the
  same method as New Customer 1 (ROUND_PLATES / SIDE_PLATES fixes included).
- Packshots (packshots/, real client photos on white) are NOT cut out: the
  bottles and bags are white / translucent on white, colour-based removal
  leaves ragged edges. Each packshot is shown whole, unmodified, on a white
  rounded tile with a thin black outline. The photo covers the tile completely
  (the tile edge only crops white background), so there is no seam. The script
  checks that the product never touches the tile edge.
- Builds: the hero diagonal cut with the "flying ingredients" (img0), the 3
  recipe + product compositions, the diagonal cuts between sections, logos,
  social icons (same as Welcome 1-3 / NC1) and copies the Akrobat webfont
  from new-customer-01.

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
    sys.exit("Pillow missing.")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]                     # repo root (contains Logo/)
IMAGES = HERE / "images"
PACKSHOTS = HERE / "packshots"
ASSETS = HERE / "assets"
LOGO_DIR = ROOT / "Logo"
FONTS_SRC = HERE.parent / "new-customer-01" / "assets" / "fonts"

ORANGE = (250, 166, 26)
PINK = (247, 172, 180)
TURQ = (134, 210, 218)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SS = 4                                     # supersampling factor for smooth edges
JPG_MAX_HERO = 170_000                     # hero cut with ingredients
JPG_MAX_PAIR = 190_000                     # each recipe + product composition (copy.md: every image under 200 KB)
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

# Background removal thresholds (same as NC1 / Welcome 3)
WHITE_MIN = 225
SAT_MAX = 14
CHECKER_MIN = 170
WORK_MAX = 1600
THRESHOLDS = {}        # per-image overrides: {"stem": (white_min, sat_max)}
SHADOW_MIN = 120
SHADOW_SAT = 26
SHADOW_GAIN = 0.40
SHADOW_SAT_BY = {}
# Overhead round plates: clean ellipse alpha. None in this email (no top-down plates).
ROUND_PLATES = set()
# Side-view plates: convex-hull fill of the plate zone (fixes bites in the rim).
#   img1-ciocolata: short stack, eye level, on the beige plate
#   img3-lava-vanilie: lava cake, side 20 degrees, on the beige plate
# Not in either set: img2-pizza-felie (no plate; the hand enters from the right
# edge, a hull would fill the gap between hand and pizza) and
# img0-hero-ingrediente (loose pieces, no plate).
SIDE_PLATES = {"img1-ciocolata", "img3-lava-vanilie"}
PLATE_ROW_FRAC = 0.80
# Background pockets enclosed by the food (white between cheese strings): removed too.
HOLES = {"img2-pizza-felie"}

# Packshot tile (2x pixels): photo scaled to cover the tile, tile edge crops white only
TILE_W, TILE_H, TILE_R, TILE_LINE = 520, 680, 60, 5
PACK_WHITE = 249                           # packshot background test (only for the edge-margin check)
PACK_MIN_MARGIN = 14

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


def find_input(stem, folder=None):
    """<folder>/<stem>.png | .jpg | .jpeg (any case)."""
    folder = folder or IMAGES
    for p in sorted(folder.glob("*")):
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


def clip_paste(canvas, src, x, y):
    """alpha_composite at top-left (x, y); accepts positions partly outside the canvas (bleed)."""
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    layer.paste(src, (round(x), round(y)), src)
    canvas.alpha_composite(layer)


def poly_mask(size, pts):
    """Antialiased polygon mask."""
    w, h = size
    m = Image.new("L", (w * SS, h * SS), 0)
    ImageDraw.Draw(m).polygon([(x * SS, y * SS) for x, y in pts], fill=255)
    return m.resize((w, h), Image.LANCZOS)


def rrect_mask(size, box, r):
    w, h = size
    m = Image.new("L", (w * SS, h * SS), 0)
    ImageDraw.Draw(m).rounded_rectangle([v * SS for v in box], radius=r * SS, fill=255)
    return m.resize((w, h), Image.LANCZOS)


# ---------------------------------------------------------------- cutout (local, no network; from NC1)
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



def side_plate_mask(hard, rgb, dark=135, light=225):
    """Below the widest row of a side-view plate, replace the mask with a half
    ellipse: width = widest row, bottom = end of the dark plate underside on
    the centre column. Removes the photo's soft shadow under the plate."""
    w, h = hard.size
    small = hard.reduce(2).point(lambda v: 255 if v > 128 else 0)
    sw, sh = small.size
    px = small.load()
    spans = {}
    for y in range(sh):
        xs = [x for x in range(sw) if px[x, y]]
        if xs:
            spans[y] = (xs[0], xs[-1])
    widest = max(b - a for a, b in spans.values())
    rows = [y for y, (a, b) in spans.items() if b - a >= 0.985 * widest]
    yw = rows[len(rows) // 2]
    l, r = spans[yw]
    yw, l, r = yw * 2, l * 2, r * 2 + 1
    cx = (l + r) // 2
    lum = rgb.convert("L").load()
    yb = None
    y = yw
    while y < h - 1:
        if lum[cx, y] < dark:
            yb = y
        if yb is not None and lum[cx, y] > light:
            break
        y += 1
    if yb is None:
        return hard, None
    yb += 2
    S = 2
    ell = Image.new("L", (w * S, h * S), 0)
    ImageDraw.Draw(ell).ellipse((l * S, (2 * yw - yb) * S, r * S, yb * S), fill=255)
    ell = ell.resize((w, h), Image.LANCZOS)
    top = Image.new("L", (w, h), 0)
    top.paste(255, (0, 0, w, yw))
    lower = Image.new("L", (w, h), 0)
    lower.paste(255, (0, yw, w, h))
    out = ImageChops.lighter(ImageChops.multiply(hard, top), ImageChops.multiply(ell, lower))
    return out, (l, r, yw, yb)

def _enclosed_white(mn, sat, min_frac=0.0004):
    """Pure-white background pockets not connected to the border (e.g. between
    stretched cheese strings), larger than min_frac of the image."""
    k = 2
    white = _and(_binary(mn, lambda v: v > 246), _binary(sat, lambda v: v < 7))
    small = white.reduce(k).point(lambda v: 255 if v >= 190 else 0)
    w, h = small.size
    px = small.load()
    seen = bytearray(w * h)
    keep = Image.new("L", (w, h), 0)
    kp = keep.load()
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
            if len(pts) >= min_frac * w * h:
                for x, y in pts:
                    kp[x, y] = 255
    return _and(keep.resize(mn.size, Image.NEAREST).filter(ImageFilter.MaxFilter(3)), white)


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

    if stem in HOLES:      # after the shadow pass, which replaces bg
        bg = ImageChops.lighter(bg, _enclosed_white(mn, sat, 0.00005))
    hard = ImageOps.invert(bg).filter(ImageFilter.MinFilter(3))
    plates = 0
    if stem in ROUND_PLATES:
        ell, plates = _plate_ellipses(hard)
    if stem in SIDE_PLATES:
        zone = _plate_zone_hull(hard)
        if zone is not None:
            hard = ImageChops.lighter(hard, zone)
        # below the widest row: clean half ellipse, drops the photo's soft shadow
        hard, fit = side_plate_mask(hard, rgb)
        if fit is None:
            print(f"WARNING: {name}: plate bottom not found, kept the colour-based edge.")
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



def split_components(rgba, max_n=10, min_frac=0.002):
    """Loose pieces of a cutout (connected solid regions), largest first.
    Returns RGBA crops, each with its own soft shadow margin."""
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
            if len(pts) > min_frac * w * h:
                comps.append(pts)
    comps.sort(key=len, reverse=True)
    out = []
    for pts in comps[:max_n]:
        m = Image.new("L", (w, h), 0)
        mp = m.load()
        for x, y in pts:
            mp[x, y] = 255
        m = m.filter(ImageFilter.MaxFilter(5)).resize(rgba.size, Image.BILINEAR)
        piece = rgba.copy()
        piece.putalpha(ImageChops.multiply(rgba.getchannel("A"), m))
        bb = piece.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
        if bb:
            out.append(piece.crop(bb))
    return out


# ---------------------------------------------------------------- placeholders (no photo yet)
def _ph_finish(img, w, h, label, sub):
    img = img.resize((w, h), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    centered_text(d, (0, h * 0.36, w * 0.8, h * 0.60), [(label, font(max(18, w // 12))), (sub, font(max(12, w // 30), False))])
    return img


def ph_stack():
    """IMG1: short stack, eye level, on a plate."""
    w, h = 720, 600
    S = 2
    W, H = w * S, h * S
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse((W * 0.04, H * 0.66, W * 0.96, H * 0.96), fill=WHITE + (255,), outline=BLACK + (255,), width=4 * S)
    for i in range(3):
        y = H * (0.64 - i * 0.15)
        d.rounded_rectangle((W * 0.16, y, W * 0.84, y + H * 0.16), radius=int(H * 0.07),
                            fill=ORANGE + (255,), outline=BLACK + (255,), width=4 * S)
    return _ph_finish(img, w, h, "IMG1", "pankees cu ciocolată, frontal")


def ph_pizza():
    """IMG2: slice lifted by a hand that enters from the right edge (touches it)."""
    w, h = 640, 800
    S = 2
    W, H = w * S, h * S
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse((W * 0.02, H * 0.70, W * 0.90, H * 0.98), fill=ORANGE + (255,), outline=BLACK + (255,), width=4 * S)
    d.polygon([(W * 0.12, H * 0.62), (W * 0.70, H * 0.18), (W * 0.82, H * 0.40)],
              fill=ORANGE + (255,), outline=BLACK + (255,), width=4 * S)
    d.rounded_rectangle((W * 0.66, H * 0.16, W * 1.10, H * 0.38), radius=int(H * 0.06),
                        fill=PINK + (255,), outline=BLACK + (255,), width=4 * S)
    return _ph_finish(img, w, h, "IMG2", "felie ridicată, mâna din dreapta")


def ph_lava():
    """IMG3: whole lava cake, ice cream scoop on top, side 20 degrees."""
    w, h = 680, 600
    S = 2
    W, H = w * S, h * S
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse((W * 0.04, H * 0.70, W * 0.96, H * 0.97), fill=WHITE + (255,), outline=BLACK + (255,), width=4 * S)
    d.rounded_rectangle((W * 0.26, H * 0.36, W * 0.74, H * 0.84), radius=int(H * 0.05),
                        fill=PINK + (255,), outline=BLACK + (255,), width=4 * S)
    d.ellipse((W * 0.34, H * 0.10, W * 0.66, H * 0.44), fill=WHITE + (255,), outline=BLACK + (255,), width=4 * S)
    return _ph_finish(img, w, h, "IMG3", "lava cake + înghețată")


def ph_pieces():
    """IMG0 placeholder: loose 'ingredient' pieces in brand colours, black outline."""
    pieces = []
    specs = [("disc", 230, WHITE, "IMG0"), ("disc", 150, PINK, ""), ("sq", 120, TURQ, ""), ("disc", 130, PINK, ""),
             ("sq", 100, WHITE, ""), ("sq", 110, TURQ, ""), ("disc", 120, PINK, ""), ("sq", 90, WHITE, "")]
    for kind, d0, col, lab in specs:
        S = 2
        D = d0 * S
        img = Image.new("RGBA", (D, D), (0, 0, 0, 0))
        dr = ImageDraw.Draw(img)
        box = (4 * S, 4 * S, D - 4 * S, D - 4 * S)
        if kind == "disc":
            dr.ellipse(box, fill=col + (255,), outline=BLACK + (255,), width=4 * S)
        else:
            dr.rounded_rectangle(box, radius=D // 6, fill=col + (255,), outline=BLACK + (255,), width=4 * S)
        img = img.resize((d0, d0), Image.LANCZOS)
        if lab:
            centered_text(ImageDraw.Draw(img), (0, d0 * 0.3, d0, d0 * 0.7), [(lab, font(d0 // 6)), ("ingrediente", font(d0 // 12, False))])
        pieces.append(img)
    return pieces


def load_cutout(stem, ph):
    p = find_input(stem)
    if p is not None:
        return cutout(Image.open(p), p.name, stem), "real"
    return ph(), "placeholder"


# ---------------------------------------------------------------- packshot tile (no cutout, no edits)
def _product_mask(photo):
    """Rough product mask of a packshot (non-white region connected away from the border).
    Used only to check that the tile edge never touches the product."""
    rgb = photo.convert("RGB")
    r, g, b = rgb.split()
    mn = ImageChops.darker(ImageChops.darker(r, g), b)
    mx = ImageChops.lighter(ImageChops.lighter(r, g), b)
    sat = ImageChops.subtract(mx, mn)
    cand = _and(_binary(mn, lambda v: v >= PACK_WHITE), _binary(sat, lambda v: v <= 6))
    k = 2
    bg = _flood_from_border(cand.reduce(k).point(lambda v: 255 if v >= 250 else 0)).resize(cand.size, Image.NEAREST)
    return ImageOps.invert(bg)


def packshot_tile(name):
    """White rounded tile, thin black outline, packshot photo unmodified inside.
    Returns (RGBA tile, product bbox in tile coords)."""
    p = PACKSHOTS / name
    if not p.exists():
        print(f"WARNING: packshot {name} missing")
        t = Image.new("RGBA", (TILE_W, TILE_H), WHITE + (255,))
        return t, (60, 40, TILE_W - 60, TILE_H - 40)
    photo = Image.open(p).convert("RGB")
    prod = _product_mask(photo)
    inner = rrect_mask((TILE_W, TILE_H), (TILE_LINE + 2, TILE_LINE + 2, TILE_W - TILE_LINE - 2, TILE_H - TILE_LINE - 2),
                       TILE_R - TILE_LINE)
    # median border colour of the photo: fills any gap if the photo has to be shrunk
    border = [photo.getpixel((x, y)) for x in range(0, photo.width, 30) for y in (1, photo.height - 2)]
    fill = tuple(sorted(c[i] for c in border)[len(border) // 2] for i in range(3))
    pbb = prod.getbbox()
    pcx = (pbb[0] + pbb[2]) / 2
    scale = max(TILE_W, TILE_H) / max(photo.size)            # cover the tile
    for _ in range(12):
        sw, sh = round(photo.width * scale), round(photo.height * scale)
        # centre the product (not the photo) horizontally; keep the tile covered when possible
        ox = round(TILE_W / 2 - pcx * scale)
        ox = min(0, max(TILE_W - sw, ox)) if sw >= TILE_W else (TILE_W - sw) // 2
        oy = (TILE_H - sh) // 2
        pm = Image.new("L", (TILE_W, TILE_H), 0)
        pm.paste(prod.resize((sw, sh), Image.NEAREST), (ox, oy))
        outside = _and(pm, ImageOps.invert(inner.point(lambda v: 255 if v > 250 else 0)).filter(ImageFilter.MaxFilter(2 * PACK_MIN_MARGIN + 1)))
        if outside.getbbox() is None:
            break
        scale *= 0.96
    else:
        print(f"WARNING: {name}: product still touches the tile edge")
    tile = Image.new("RGBA", (TILE_W, TILE_H), fill + (255,))
    tile.paste(photo.resize((sw, sh), Image.LANCZOS), (ox, oy))
    outline = Image.new("RGBA", (TILE_W, TILE_H), BLACK + (255,))
    shape = rrect_mask((TILE_W, TILE_H), (0, 0, TILE_W, TILE_H), TILE_R)
    out = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
    out.paste(outline, (0, 0), shape)
    out.paste(tile, (0, 0), inner)
    pb = pm.getbbox()
    report.append(f"  packshot {name}: unmodified photo on white tile, scale {scale:.3f}, "
                  f"product margin L{pb[0]} T{pb[1]} R{TILE_W - pb[2]} B{TILE_H - pb[3]} px (2x)")
    return out, pb


# ---------------------------------------------------------------- diagonal cuts between sections (ref4)
def cut(name, top, bottom, rising):
    """Straight diagonal cut, 1200 x 96 shown 600 x 48. rising=True: the line goes
    up from left to right (the bottom colour is taller on the right)."""
    W, H = 1200, 96
    img = Image.new("RGB", (W, H), top)
    pts = [(0, 88), (W, 8), (W, H), (0, H)] if rising else [(0, 8), (W, 88), (W, H), (0, H)]
    img.paste(Image.new("RGB", (W, H), bottom), (0, 0), poly_mask((W, H), pts))
    save_png(img, ASSETS / name)


# ---------------------------------------------------------------- hero cut: orange -> black, ingredients flying across it
def build_hero_cut():
    W, H = 1200, 440
    canvas = Image.new("RGBA", (W, H), ORANGE + (255,))
    y_at = lambda x: 150 + 170 * x / W                   # line falls from left to right
    canvas.paste(Image.new("RGBA", (W, H), BLACK + (255,)), (0, 0),
                 poly_mask((W, H), [(0, y_at(0)), (W, y_at(W)), (W, H), (0, H)]))
    p = find_input("img0-hero-ingrediente")
    if p is not None:
        pieces = split_components(cutout(Image.open(p), p.name, "img0-hero-ingrediente"))
        tag = f"real, {len(pieces)} pieces"
        if not pieces:
            print("WARNING: img0: no separate pieces found, hero cut left without ingredients")
    else:
        pieces, tag = ph_pieces(), "placeholder"
    # (x centre, offset from the line, size, rotation) by piece rank: biggest piece in the middle
    slots = [(610, -20, 250, 0), (1110, 20, 170, -18), (110, -30, 170, 14), (860, -60, 140, 25),
             (360, 50, 140, -22), (-10, 70, 130, 30), (1000, 90, 120, -8), (480, -110, 110, 35),
             (740, 110, 120, -30), (240, -120, 100, 12)]
    for piece, (cx, dy, size, rot) in zip(pieces, slots):
        pc = ImageOps.contain(piece, (size, size), Image.LANCZOS)
        if rot:
            pc = pc.rotate(rot, resample=Image.BICUBIC, expand=True)
        clip_paste(canvas, pc, cx - pc.width / 2, y_at(cx) + dy - pc.height / 2)
    save_jpg(canvas, ASSETS / "hero-cut.jpg", JPG_MAX_HERO)
    report[-1] += f"  [{tag}]"
    sync_html_height("assets/hero-cut.jpg", H // 2)


# ---------------------------------------------------------------- recipe + product compositions (ref4 col. 2 + 3)
def build_pair(out_name, stem, ph, pack, bg, slab, food_side):
    """Block colour + diagonal slab; packshot tile on one side, the food cutout
    bursting off the opposite email edge and overlapping the tile margin.
    1200 x 880, shown 600 x 440."""
    W, H = 1200, 880
    canvas = Image.new("RGBA", (W, H), bg + (255,))
    if food_side == "left":
        pts = [(0, 520), (W, 250), (W, 560), (0, 830)]
    else:
        pts = [(0, 250), (W, 520), (W, 830), (0, 560)]
    canvas.paste(Image.new("RGBA", (W, H), slab + (255,)), (0, 0), poly_mask((W, H), pts))
    tile, pb = packshot_tile(pack)
    ty = (H - TILE_H) // 2
    tx = W - TILE_W - 44 if food_side == "left" else 44
    canvas.alpha_composite(tile, (tx, ty))
    food, tag = load_cutout(stem, ph)
    if food_side == "left":
        limit = tx + pb[0] - 14                           # food may cover the tile margin, never the product
        food = ImageOps.contain(food, (limit + 70, H - 50), Image.LANCZOS)
        x = limit - food.width
    else:
        limit = tx + pb[2] + 14
        food = ImageOps.contain(food, (W + 4 - limit, H - 40), Image.LANCZOS)
        x = W + 2 - food.width                            # the wrist always reaches the email edge
    y = (H - food.height) / 2 + 10
    clip_paste(canvas, food, x, y)
    save_jpg(canvas, ASSETS / out_name, JPG_MAX_PAIR)
    report[-1] += f"  [{tag}]"
    sync_html_height(f"assets/{out_name}", H // 2)


# ---------------------------------------------------------------- logos, fonts (same as NC1)
def build_logos():
    src = Image.open(LOGO_DIR / "Logo_LucasBites.png").convert("RGBA")
    w = 360                                                # displayed at 180px
    src = src.resize((w, round(src.height * w / src.width)), Image.LANCZOS)
    src.save(ASSETS / "logo.png", optimize=True)
    report.append(f"assets/logo.png  {w}x{src.height} (shown 180px)")
    sync_html_height("assets/logo.png", round(src.height / 2))

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
        report.append(f"assets/fonts/{f.name}  (copied from new-customer-01)")


# ---------------------------------------------------------------- social icons (same as Welcome 1-3 / NC1)
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
PAIRS = [   # out, food stem, placeholder, packshot, block colour, slab colour, side the food bleeds off
    ("pair1-ciocolata.jpg", "img1-ciocolata", ph_stack, "pr-choco.jpg", PINK, ORANGE, "left"),
    ("pair2-pizza.jpg", "img2-pizza-felie", ph_pizza, "pr-pizza.jpg", BLACK, TURQ, "right"),
    ("pair3-lava.jpg", "img3-lava-vanilie", ph_lava, "pr-lava.jpg", TURQ, PINK, "left"),
]


def main():
    ASSETS.mkdir(exist_ok=True)
    IMAGES.mkdir(exist_ok=True)
    build_logos()
    copy_fonts()
    # diagonal cuts, in email order (directions alternate: a zig-zag rhythm down the email)
    cut("cut-white-orange.png", WHITE, ORANGE, rising=True)      # header -> hero
    cut("cut-black-pink.png", BLACK, PINK, rising=True)          # S2 intro -> pair 1
    cut("cut-pink-black.png", PINK, BLACK, rising=False)         # pair 1 -> pair 2
    cut("cut-black-turq.png", BLACK, TURQ, rising=True)          # pair 2 -> pair 3
    cut("cut-turq-white.png", TURQ, WHITE, rising=False)         # pair 3 -> S3
    cut("cut-white-orange2.png", WHITE, ORANGE, rising=False)    # S3 -> S4
    cut("cut-orange-white.png", ORANGE, WHITE, rising=True)      # S4 -> footer
    build_hero_cut()
    for args in PAIRS:
        build_pair(*args)
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
