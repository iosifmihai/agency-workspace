#!/usr/bin/env python3
"""Lucas Bites, New Customer Email 3: asset builder (Pillow only, no network).

Base: new-customer-02/build.py (same cutout pipeline and plate-fixing helpers).
Run by Claude after the food photos land in images/ (names from image-prompts.md,
.png/.jpg/.jpeg). Missing photos get placeholders at the final size, so
index.html never changes.

- IMG1-IMG3 (cutouts on plain white) are cut out locally and placed over the
  bottom-right corner of a white packshot tile: 3 product cards for S2.
- Packshots (packshots/) are NOT cut out or edited: shown whole on a white
  rounded tile with a thin black outline (same as NC2).
- IMG4-IMG6 (UGC phone-photo squares) are NOT cut out: centre-cropped 1:1,
  rounded corners baked on black for the S4 grid.
- Builds: wavy cuts between sections, 4 USP line icons, logos, social icons,
  Akrobat webfont (copied from new-customer-01).

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
JPG_MAX_CARD = 110_000                     # each S2 product card (copy.md: every image under 200 KB)
JPG_MAX_UGC = 90_000                       # each S4 phone-photo square
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
# Plate fixes kept from NC2; empty for now (IMG1-IMG3 have no plate). Fill in after checking the real photos.
# Overhead round plates: clean ellipse alpha.
ROUND_PLATES = set()
# Side-view plates: convex-hull fill of the plate zone (fixes bites in the rim).
SIDE_PLATES = set()
PLATE_ROW_FRAC = 0.80
# Background pockets enclosed by the food (white between cheese strings): removed too.
HOLES = set()

# Packshot tile (2x pixels) for the S2 cards
TILE_W, TILE_H, TILE_R, TILE_LINE = 300, 340, 40, 4
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



# ---------------------------------------------------------------- placeholders (no photo yet)
def _ph_label(img, label, sub):
    d = ImageDraw.Draw(img)
    w, h = img.size
    centered_text(d, (0, h * 0.3, w, h * 0.7), [(label, font(max(18, w // 8))), (sub, font(max(12, w // 20), False))])
    return img


def ph_food(label, sub, col):
    """Cutout placeholder: soft blob in a brand colour, black outline."""
    w, h = 420, 340
    S = 2
    img = Image.new("RGBA", (w * S, h * S), (0, 0, 0, 0))
    ImageDraw.Draw(img).ellipse((8 * S, 30 * S, (w - 8) * S, (h - 8) * S), fill=col + (255,),
                                outline=BLACK + (255,), width=5 * S)
    return _ph_label(img.resize((w, h), Image.LANCZOS), label, sub)


# ---------------------------------------------------------------- wavy cuts between sections (ref4 col. 1)
def wave(name, top, bottom, phase=0.0, waves=2.0):
    """Soft wave, 1200 x 80 shown 600 x 40. Top colour above the wave, bottom colour below."""
    W, H = 1200, 80
    img = Image.new("RGB", (W, H), top)
    pts = [(x, 40 + 22 * math.sin(phase + 2 * math.pi * waves * x / W)) for x in range(0, W + 1, 6)]
    pts += [(W, H), (0, H)]
    img.paste(Image.new("RGB", (W, H), bottom), (0, 0), poly_mask((W, H), pts))
    save_png(img, ASSETS / name)


# ---------------------------------------------------------------- S2 product cards (ref4 col. 3)
CARD_W, CARD_H = 360, 500                  # shown 180 x 250


def build_card(out_name, stem, ph, pack, bg):
    """Packshot tile at the top; the food cutout bursts out of its lower-right
    corner and off the card's right edge. Food may cover the tile margin and the
    lowest strip of the packshot photo, never the product's upper 85%."""
    canvas = Image.new("RGBA", (CARD_W, CARD_H), bg + (255,))
    tile, pb = packshot_tile(pack)
    tx, ty = 14, 8
    canvas.alpha_composite(tile, (tx, ty))
    food, tag = load_cutout(stem, ph)
    top_limit = ty + pb[1] + int(0.85 * (pb[3] - pb[1]))
    food = ImageOps.contain(food, (CARD_W - 40, CARD_H - top_limit - 4), Image.LANCZOS)
    x = CARD_W - food.width - 6                           # stays fully inside the card (no clipped edge)
    y = CARD_H - food.height - 4
    clip_paste(canvas, food, x, y)
    save_jpg(canvas, ASSETS / out_name, JPG_MAX_CARD)
    report[-1] += f"  [{tag}]"
    sync_html_height(f"assets/{out_name}", CARD_H // 2)


# ---------------------------------------------------------------- S4 phone-photo squares (no cutout)
UGC = 352                                  # shown 176


def build_ugc(out_name, stem, label, sub, bg=BLACK):
    p = find_input(stem)
    if p is not None:
        photo = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
        photo = ImageOps.fit(photo, (UGC, UGC), Image.LANCZOS)
        tag = "real"
    else:
        photo = _ph_label(Image.new("RGB", (UGC, UGC), TURQ), label, sub)
        tag = "placeholder"
    out = Image.new("RGB", (UGC, UGC), bg)
    out.paste(photo, (0, 0), rrect_mask((UGC, UGC), (0, 0, UGC, UGC), 28))
    save_jpg(out, ASSETS / out_name, JPG_MAX_UGC)
    report[-1] += f"  [{tag}]"


# ---------------------------------------------------------------- S3 USP line icons (black on transparent)
def usp_icons():
    n, lw = 192, 12
    def save(m, name):
        finish_icon(m, name, size=112)                    # shown 56px
    # box / parcel
    m = Image.new("L", (n, n), 0); d = ImageDraw.Draw(m)
    d.polygon([(96, 30), (166, 62), (96, 94), (26, 62)], outline=255, width=lw)
    d.line([(26, 62), (26, 136), (96, 168), (166, 136), (166, 62)], fill=255, width=lw, joint="curve")
    d.line([(96, 94), (96, 168)], fill=255, width=lw)
    d.line([(61, 46), (131, 78)], fill=255, width=lw)
    save(m, "usp-box.png")
    # clock
    m = Image.new("L", (n, n), 0); d = ImageDraw.Draw(m)
    d.ellipse((24, 24, 168, 168), outline=255, width=lw)
    d.line([(96, 96), (96, 54)], fill=255, width=lw)
    d.line([(96, 96), (128, 112)], fill=255, width=lw)
    d.ellipse((88, 88, 104, 104), fill=255)
    save(m, "usp-clock.png")
    # card
    m = Image.new("L", (n, n), 0); d = ImageDraw.Draw(m)
    d.rounded_rectangle((20, 46, 172, 146), radius=16, outline=255, width=lw)
    d.rectangle((20, 70, 172, 88), fill=255)
    d.line([(42, 120), (90, 120)], fill=255, width=lw)
    save(m, "usp-card.png")
    # chat bubble
    m = Image.new("L", (n, n), 0); d = ImageDraw.Draw(m)
    d.rounded_rectangle((22, 30, 170, 128), radius=30, outline=255, width=lw)
    d.polygon([(54, 122), (54, 166), (96, 124)], fill=255)
    for cx in (62, 96, 130):
        d.ellipse((cx - 9, 70, cx + 9, 88), fill=255)
    save(m, "usp-chat.png")


# ---------------------------------------------------------------- main
CARDS = [   # out, food stem, placeholder, packshot, card colour (= S2 band)
    ("card1-brownie.jpg", "img1-brownie", lambda: ph_food("IMG1", "brownie + fructe de pădure", ORANGE), "pr-brownie.jpg", PINK),
    ("card2-cookies.jpg", "img2-cookies", lambda: ph_food("IMG2", "cookies ciocolată neagră", ORANGE), "pr-cookie450.jpg", PINK),
    ("card3-crepes.jpg", "img3-crepes", lambda: ph_food("IMG3", "clătite în triunghi", ORANGE), "pr-crepes.jpg", PINK),
]
UGCS = [
    ("ugc1-pancakes.jpg", "img4-ugc-pancakes", "IMG4", "pancakes, de sus"),
    ("ugc2-brownie.jpg", "img5-ugc-brownie", "IMG5", "brownie în tavă"),
    ("ugc3-crepes.jpg", "img6-ugc-crepes", "IMG6", "clătite rulate"),
]


def main():
    ASSETS.mkdir(exist_ok=True)
    IMAGES.mkdir(exist_ok=True)
    build_logos()
    copy_fonts()
    # wavy cuts, in email order
    wave("wave-white-turq.png", WHITE, TURQ, phase=0.0)          # header -> hero
    wave("wave-turq-pink.png", TURQ, PINK, phase=math.pi)        # hero -> S2
    wave("wave-pink-orange.png", PINK, ORANGE, phase=0.0)        # S2 -> S3
    wave("wave-orange-black.png", ORANGE, BLACK, phase=math.pi)  # S3 -> S4
    wave("wave-black-white.png", BLACK, WHITE, phase=0.0)        # S4 -> footer
    for args in CARDS:
        build_card(*args)
    for args in UGCS:
        build_ugc(*args)
    usp_icons()
    build_icons()
    print("Built assets:")
    for line in report:
        print("  " + line)


if __name__ == "__main__":
    main()
