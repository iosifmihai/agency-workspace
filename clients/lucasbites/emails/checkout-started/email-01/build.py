#!/usr/bin/env python3
"""Lucas Bites, Checkout Started Email 1: asset + HTML builder.

Usage:
  python3 build.py              build assets/ and index.html + index-esp.html
  python3 build.py --preview    same, then preview.png (600px) and preview-mobile.png (375px)
                                with headless Google Chrome (macOS path, see CHROME below)

Needs Pillow only (no network). If Pillow is missing:
  python3 -m venv .venv && .venv/bin/pip install Pillow && .venv/bin/python build.py

- Photos dropped into images/ (names from image-prompts.md, .png/.jpg/.jpeg) are cut
  out locally (plain white background removed, same method as welcome-02/03) and
  pre-composited as opaque JPGs: the hero (pink, annotations, sparkles, white panel
  with rounded top corners) and the S5 crepes plate cut by the right edge on orange.
- Missing photos get a placeholder at the final size and final file name, so the
  layout never changes: add the photos, rerun, done.
- Texts come from copy.md (Email Marketing Strategist) and live in COPY below,
  verbatim. Change copy.md first, then COPY.
- index.html     = preview, cart block filled with 2 rows marked EXEMPLU.
  index-esp.html = theMarketer version: cart block holds a [FEED PRODUSE THEMARKETER]
                   placeholder, replaced by the product feed in the theMarketer editor.

Brand colours only: #FAA61A, #F7ACB4, #86D2DA, #000000, plus white.
"""
import html
import math
import shutil
import subprocess
import sys
import tempfile
from collections import deque
from io import BytesIO
from pathlib import Path
from string import Template

try:
    from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps
except ImportError:
    sys.exit("Pillow missing. Install it in a venv: python3 -m venv .venv && .venv/bin/pip install Pillow")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]                       # repo root (contains Logo/ and Fonturi/)
EMAILS = HERE.parents[1]                     # clients/lucasbites/emails
IMAGES = HERE / "images"
ASSETS = HERE / "assets"
LOGO_DIR = ROOT / "Logo"
FONTS_SRC = EMAILS / "welcome-02" / "assets" / "fonts"     # Akrobat webfont (read only)
ICONS_SRC = EMAILS / "welcome-03" / "assets"                # social icons (read only, identical footer)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

ORANGE = (250, 166, 26)
PINK = (247, 172, 180)
TURQ = (134, 210, 218)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLATE = (24, 24, 24)
GOLD = ORANGE                                # placeholder pancake colour (brand orange)

SS = 4
JPG_MAX = 300_000
JPG_MAX_SMALL = 120_000
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
# Annotation font in the hero image: Akrobat Bold (licence to be bought before launch,
# same status as the webfont). Plicata is NOT used (personal-use licence only).
FONT_ANNOT = [ROOT / "Fonturi" / "Akrobat-Bold.otf",
              Path("/System/Library/Fonts/Supplemental/Arial Narrow Bold.ttf")]

UTM = "utm_source=email&amp;utm_medium=flow&amp;utm_campaign=checkout_01"

# ---------------------------------------------------------------- COPY (verbatim from copy.md)
COPY = {
    "title": "Pofta ta e încă în coș",
    "preheader": "Mixurile alese sunt la un click distanță. Transport gratuit de la al 2-lea produs.",
    "greeting": "Hei, {{FIRST_NAME}}!",            # ESP: fallback „Hei!” (copy.md S1)
    "h1_l1": "POFTA TA E",
    "h1_l2": "ÎNCĂ ÎN COȘ.",
    "intro": "Ai ales deja ce-ți face poftă. Mai e un singur pas și mixurile pornesc spre tine.",
    "annot": [("APROAPE TOT", "E ÎN MIX"), ("REPEDE", "ȘI SIMPLU"), ("FĂRĂ", "CONSERVANȚI")],
    "cart_label": "ÎN COȘUL TĂU",
    "qty_label": "Cantitate:",
    "total_label": "Total produse:",
    "cta_main": "Finalizează comanda",
    "usp_title": "DE CE O SĂ-ȚI PLACĂ",
    "usp": [("TRANSPORT GRATUIT", "De la al 2-lea produs din coș."),
            ("REPEDE ȘI SIMPLU", "Mixul are deja aproape tot în el."),
            ("FĂRĂ CONSERVANȚI", "Ingrediente pe care le recunoști.")],
    "s5_title": "ÎNCĂ TE GÂNDEȘTI?",
    "s5_line": "Răsfoiește toată gama: pancakes, clătite, prăjituri și pizza.",
    "cta_shop": "Vezi toate mixurile",
    "signature": "eat what you love",
    "alt_logo": "Lucas Bites",
    "alt_hero": "Teanc de pancakes pufoase cu bucăți de ciocolată. Repede și simplu, fără conservanți.",
    "alt_crepes": "Clătite rulate cu cremă de ciocolată, alune și zahăr pudră",
    "alt_footer_logo": "Lucas Bites, eat what you love",
    "footer_why": "Primești acest email pentru că ai început o comandă pe lucasbites.ro și ai acceptat să primești emailuri de la noi.",
    "footer_unsub_pre": "Nu mai vrei emailuri de la noi?",
    "footer_unsub_link": "Dezabonează-te aici",
    "footer_unsub_post": "Durează un click.",
}
# Example cart rows (preview only, clearly marked). Product names exist in the range
# (discovery.md); quantities and prices are placeholders, NOT facts.
CART_EXAMPLE = [
    {"img": "assets/cart-example-1.png", "name": "Classic Pankees (EXEMPLU)", "qty": "1", "price": "XX,XX lei"},
    {"img": "assets/cart-example-2.png", "name": "Crêpes Traditional (EXEMPLU)", "qty": "2", "price": "XX,XX lei"},
]
CART_TOTAL_EXAMPLE = "XX,XX lei"

report = []


# ---------------------------------------------------------------- helpers
def font(size, bold=True):
    path = FONT_BOLD if bold else FONT_REG
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default(size=size)


def annot_font(size):
    for p in FONT_ANNOT:
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return font(size)


def save_jpg(img, path, max_bytes=JPG_MAX):
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
    for p in sorted(IMAGES.glob("*")):
        if p.stem.lower() == stem.lower() and p.suffix.lower() in (".png", ".jpg", ".jpeg"):
            return p
    return None


# ---------------------------------------------------------------- cutout (same method as welcome-03)
WHITE_MIN = 225
SAT_MAX = 14
CHECKER_MIN = 170
WORK_MAX = 1600
SHADOW_MIN = 120
SHADOW_SAT = 26
SHADOW_GAIN = 0.40
NO_SHADOW = {"img1-hero"}     # floating stack: no contact shadow wanted


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


def cutout(img, name="image", stem=""):
    """RGBA cutout cropped to content. Real transparency is kept; otherwise the
    near-white background connected to the border is removed (flood fill)."""
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
    neutral = _binary(sat, lambda v: v < SAT_MAX)
    w, h = rgb.size
    border = [(x, 0) for x in range(0, w, 4)] + [(x, h - 1) for x in range(0, w, 4)] + \
             [(0, y) for y in range(0, h, 4)] + [(w - 1, y) for y in range(0, h, 4)]
    mnp, satp = mn.load(), sat.load()
    grey = sum(1 for p in border if CHECKER_MIN < mnp[p] <= WHITE_MIN and satp[p] < SAT_MAX)
    checker = grey / len(border) > 0.08
    thr = CHECKER_MIN if checker else WHITE_MIN
    cand = _and(neutral, _binary(mn, lambda v: v > thr))
    k = 4
    small = cand.reduce(k).point(lambda v: 255 if v >= 250 else 0)
    bg = _and(_flood_from_border(small).resize(cand.size, Image.NEAREST), cand)
    bg = _grow(bg, cand, k)

    shadow = None
    if not checker and stem not in NO_SHADOW:
        loose = _and(_binary(sat, lambda v: v < SHADOW_SAT), _binary(mn, lambda v: v > SHADOW_MIN))
        lbg = _and(_flood_from_border(loose.reduce(k).point(lambda v: 255 if v >= 250 else 0))
                   .resize(loose.size, Image.NEAREST), loose)
        lbg = _grow(lbg, loose, 20)
        lum = rgb.convert("L")
        shade = lum.point(lambda v: max(0, min(255, int((250 - v) * 255 / 130 * SHADOW_GAIN))))
        shadow = ImageChops.multiply(shade, _and(lbg, ImageOps.invert(bg)))
        bg = lbg

    hard = ImageOps.invert(bg).filter(ImageFilter.MinFilter(3))
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
    report.append(f"  {name}: background removed ({'checkerboard' if checker else 'white'} mode)")
    return out.crop(bbox)


def load_cutout(stem, ph):
    p = find_input(stem)
    if p is not None:
        return cutout(Image.open(p), p.name, stem), "real"
    return ph(), "placeholder"


# ---------------------------------------------------------------- placeholders
def placeholder_stack(w, h):
    """Stylised floating pancake stack + strawberries, so the layout reads before photos exist."""
    S = 2
    W, H = w * S, h * S
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W / 2
    for i in range(4):                      # bottom to top
        y = H * (0.70 - i * 0.11)
        d.ellipse((cx - W * 0.36, y - H * 0.07, cx + W * 0.36, y + H * 0.07),
                  fill=GOLD + (255,), outline=BLACK + (255,), width=5 * S)
    for (fx, fy, fr) in ((0.12, 0.18, 0.06), (0.86, 0.26, 0.05), (0.10, 0.78, 0.05), (0.88, 0.82, 0.06)):
        d.ellipse((W * fx - W * fr, H * fy - W * fr, W * fx + W * fr, H * fy + W * fr),
                  fill=PINK + (255,), outline=BLACK + (255,), width=4 * S)
    img = img.resize((w, h), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    centered_text(d, (0, h * 0.02, w, h * 0.22), [("IMG1", font(w // 10)), ("pancakes plutind", font(w // 24, False))])
    return img


def placeholder_plate(n):
    """Top-down black plate with three rolled crepes."""
    S = 2
    N = n * S
    img = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse((N * 0.03, N * 0.03, N * 0.97, N * 0.97), fill=PLATE + (255,), outline=BLACK + (255,), width=4 * S)
    for i in range(3):
        y = N * (0.32 + i * 0.15)
        d.rounded_rectangle((N * 0.22, y, N * 0.78, y + N * 0.11), radius=int(N * 0.05),
                            fill=GOLD + (255,), outline=BLACK + (255,), width=4 * S)
    img = img.resize((n, n), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    centered_text(d, (0, n * 0.12, n, n * 0.28), [("IMG2", font(n // 12)), ("clătite rulate", font(n // 26, False))],
                  fill=WHITE)
    return img


# ---------------------------------------------------------------- decorative drawing
def sparkle(d, cx, cy, r, s=1):
    """4-point sparkle, orange with black outline (like the logo letters)."""
    pts = []
    for i in range(8):
        a = -math.pi / 2 + i * math.pi / 4
        rr = r if i % 2 == 0 else r * 0.28
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d.polygon(pts, fill=ORANGE + (255,), outline=BLACK + (255,), width=max(3, int(r * 0.06)))


def bezier(p0, p1, p2, n=60):
    return [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0],
             (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]) for t in (i / n for i in range(n + 1))]


def hand_arrow(d, p0, p1, p2, width, head):
    """Curved hand-drawn arrow (quadratic curve, round caps, open arrowhead)."""
    pts = bezier(p0, p1, p2)
    d.line(pts, fill=BLACK + (255,), width=width, joint="curve")
    for p in (pts[0], pts[-1]):
        d.ellipse((p[0] - width / 2, p[1] - width / 2, p[0] + width / 2, p[1] + width / 2), fill=BLACK + (255,))
    ex, ey = pts[-1]
    px, py = pts[-6]
    ang = math.atan2(ey - py, ex - px)
    for da in (math.radians(150), math.radians(-150)):
        hx, hy = ex + head * math.cos(ang + da), ey + head * math.sin(ang + da)
        d.line([(ex, ey), (hx, hy)], fill=BLACK + (255,), width=width)
        d.ellipse((hx - width / 2, hy - width / 2, hx + width / 2, hy + width / 2), fill=BLACK + (255,))


def text_block(lines, size, align="left", angle=0):
    """Two-line annotation rendered on its own layer, slightly rotated (hand-placed feel)."""
    f = annot_font(size)
    lh = int(size * 1.02)
    wmax = int(max(f.getlength(t) for t in lines)) + 8
    layer = Image.new("RGBA", (wmax, lh * len(lines) + 12), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for i, t in enumerate(lines):
        tw = f.getlength(t)
        x = 0 if align == "left" else wmax - tw if align == "right" else (wmax - tw) / 2
        d.text((x, i * lh), t, font=f, fill=BLACK)
    return layer.rotate(angle, resample=Image.BICUBIC, expand=True)


# ---------------------------------------------------------------- hero
def build_hero():
    """1200 x 1000 (shown 600 x 500): pink, floating stack rotated -10 deg, three
    annotations with hand-drawn arrows, sparkles, white panel with rounded top
    corners from y=860. The stack overlaps the panel edge (food 'out of frame')."""
    W, H = 1200, 1000
    panel_y, radius = 860, 64
    canvas = Image.new("RGBA", (W, H), PINK + (255,))

    # white panel, rounded top corners (supersampled)
    m = Image.new("L", (W * 2, H * 2), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, panel_y * 2, W * 2 - 1, (H + radius) * 2), radius=radius * 2, fill=255)
    canvas.paste(Image.new("RGBA", (W, H), WHITE + (255,)), (0, 0), m.resize((W, H), Image.LANCZOS))

    # decoration layer at 2x
    deco = Image.new("RGBA", (W * 2, H * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(deco)
    for (x, y, r) in ((560, 70, 30), (1110, 90, 22), (92, 470, 20), (1100, 690, 32), (330, 800, 18)):
        sparkle(d, x * 2, y * 2, r * 2, 2)
    # arrows: (start, control, end) in 1200x1000 space, pointing at the stack
    arrows = [((190, 300), (220, 390), (330, 400)),
              ((1065, 300), (1065, 370), (1000, 395)),
              ((200, 720), (260, 765), (330, 730))]
    for p0, p1, p2 in arrows:
        hand_arrow(d, [v * 2 for v in p0], [v * 2 for v in p1], [v * 2 for v in p2], width=12, head=40)
    canvas.alpha_composite(deco.resize((W, H), Image.LANCZOS))

    # annotations (texts from copy.md)
    a = COPY["annot"]
    for lines, pos, align, ang in ((a[0], (60, 150), "left", 5), (a[1], (1150, 150), "right", -5),
                                   (a[2], (50, 575), "left", 4)):
        layer = text_block(lines, 50, align, ang)
        x = pos[0] if align == "left" else pos[0] - layer.width
        canvas.alpha_composite(layer, (int(x), pos[1]))

    # stack cutout
    box = (720, 820)                         # real cutout is wide (floating pieces): bigger box so the stack reads at email size
    src, tag = load_cutout("img1-hero", lambda: placeholder_stack(*box))
    src = ImageOps.contain(src, box, Image.LANCZOS)
    src = src.rotate(10, resample=Image.BICUBIC, expand=True)       # +10 = counter-clockwise tilt
    canvas.alpha_composite(src, ((W - src.width) // 2 + 45, 930 - src.height))   # crosses the panel edge (~860)
    save_jpg(canvas, ASSETS / "hero.jpg")
    report[-1] += f"  [{tag}]"


# ---------------------------------------------------------------- S5 crepes plate
def build_crepes():
    """440 x 600 (shown 220 x 300) on orange; the plate is cut by the right edge
    (sits flush with the email's right edge)."""
    W, H = 440, 600
    n = 540
    src, tag = load_cutout("img2-clatite", lambda: placeholder_plate(n))
    src = ImageOps.contain(src, (n, n), Image.LANCZOS)
    canvas = Image.new("RGBA", (W, H), ORANGE + (255,))
    x = 40                                   # plate wider than the canvas: right part is cut
    canvas.alpha_composite(src.crop((0, 0, min(src.width, W - x), src.height)), (x, (H - src.height) // 2))
    save_jpg(canvas, ASSETS / "s5-clatite.jpg", JPG_MAX_SMALL)
    report[-1] += f"  [{tag}]"


# ---------------------------------------------------------------- cart example tiles (preview only)
def build_cart_examples():
    for i, colour in ((1, PINK), (2, TURQ)):
        n = 192
        img = Image.new("RGBA", (n, n), WHITE + (255,))
        m = Image.new("L", (n * SS, n * SS), 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, n * SS - 1, n * SS - 1), radius=24 * SS, fill=255)
        img.paste(Image.new("RGBA", (n, n), colour + (255,)), (0, 0), m.resize((n, n), Image.LANCZOS))
        d = ImageDraw.Draw(img)
        d.rounded_rectangle((10, 10, n - 11, n - 11), radius=18, outline=BLACK, width=3)
        centered_text(d, (0, 0, n, n), [("EXEMPLU", font(30)), ("imagine", font(20, False)), ("din coș", font(20, False))])
        save_png(img.convert("RGB"), ASSETS / f"cart-example-{i}.png")


# ---------------------------------------------------------------- USP icons
def rot_ellipse(cx, cy, rx, ry, ang, n=40):
    c, s = math.cos(ang), math.sin(ang)
    return [(cx + rx * math.cos(t) * c - ry * math.sin(t) * s, cy + rx * math.cos(t) * s + ry * math.sin(t) * c)
            for t in (2 * math.pi * i / n for i in range(n))]


def build_usp_icons():
    """64 x 64 shown (128 exported): white circle, black 3px ring, black pictogram."""
    N = 128 * SS
    lw = 6 * SS

    def base():
        img = Image.new("RGBA", (N, N), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        d.ellipse((lw / 2, lw / 2, N - lw / 2, N - lw / 2), fill=WHITE + (255,), outline=BLACK + (255,), width=lw)
        return img, d

    def done(img, name):
        save_png(img.resize((128, 128), Image.LANCZOS), ASSETS / name)

    u = N / 128
    # truck
    img, d = base()
    d.rounded_rectangle((26 * u, 44 * u, 76 * u, 82 * u), radius=4 * u, outline=BLACK, width=lw)
    d.polygon([(76 * u, 54 * u), (92 * u, 54 * u), (104 * u, 68 * u), (104 * u, 82 * u), (76 * u, 82 * u)],
              outline=BLACK, width=lw)
    for cx in (42, 90):
        d.ellipse(((cx - 9) * u, (82 - 9) * u, (cx + 9) * u, (82 + 9) * u), fill=WHITE, outline=BLACK, width=lw)
    done(img, "usp-transport.png")
    # timer with hands (no number: USP is "Repede și simplu", not a fixed time)
    img, d = base()
    d.ellipse((34 * u, 38 * u, 94 * u, 98 * u), outline=BLACK, width=lw)
    d.rounded_rectangle((56 * u, 24 * u, 72 * u, 32 * u), radius=3 * u, fill=BLACK)
    d.line([(64 * u, 32 * u), (64 * u, 38 * u)], fill=BLACK, width=lw)
    d.line([(64 * u, 68 * u), (64 * u, 50 * u)], fill=BLACK, width=lw)
    d.line([(64 * u, 68 * u), (77 * u, 75 * u)], fill=BLACK, width=lw)
    d.ellipse((60 * u, 64 * u, 68 * u, 72 * u), fill=BLACK)
    done(img, "usp-timp.png")
    # wheat ear
    img, d = base()
    d.line([(64 * u, 104 * u), (64 * u, 40 * u)], fill=BLACK, width=lw)
    for i, y in enumerate((50, 64, 78)):
        for side in (-1, 1):
            d.polygon(rot_ellipse(64 * u + side * 12 * u, y * u, 13 * u, 6.5 * u, side * math.radians(-50)),
                      fill=BLACK)
    d.polygon(rot_ellipse(64 * u, 34 * u, 6.5 * u, 12 * u, 0), fill=BLACK)
    done(img, "usp-ingrediente.png")


# ---------------------------------------------------------------- logos, fonts, icons, waves
def build_logos():
    src = Image.open(LOGO_DIR / "Logo_LucasBites.png").convert("RGBA")
    w = 360
    src = src.resize((w, round(src.height * w / src.width)), Image.LANCZOS)
    src.save(ASSETS / "logo.png", optimize=True)
    report.append(f"assets/logo.png  {w}x{src.height} (shown 180px)")
    st = Image.open(LOGO_DIR / "Logo_LucasBites_stripes-nobg.png").convert("RGBA")
    bbox = st.getchannel("A").point(lambda v: 255 if v > 40 else 0).getbbox()
    st = st.crop((0, bbox[1], st.width, bbox[3]))
    cx, half = st.width // 2, 1050
    st = st.crop((cx - half, 0, cx + half, st.height))
    w2 = 520
    st = st.resize((w2, round(st.height * w2 / st.width)), Image.LANCZOS)
    st.save(ASSETS / "logo-stripes.png", optimize=True)
    report.append(f"assets/logo-stripes.png  {w2}x{st.height} (shown 260px)")
    return round(src.height / 2), round(st.height / 2)


def copy_shared():
    dst = ASSETS / "fonts"
    dst.mkdir(exist_ok=True)
    for f in FONTS_SRC.glob("Akrobat-*.woff*"):
        shutil.copy2(f, dst / f.name)
    for name in ("icon-instagram.png", "icon-tiktok.png", "icon-facebook.png", "icon-youtube.png"):
        shutil.copy2(ICONS_SRC / name, ASSETS / name)
    report.append("assets/fonts/* (from welcome-02), assets/icon-*.png (from welcome-03)")


def wave_divider(name, top, bottom, phase, periods=1.25, h=96, amp=20):
    img = Image.new("RGB", (1200, h), top)
    img.paste(Image.new("RGB", (1200, h), bottom), (0, 0), wave_mask(1200, h, h / 2, amp, periods, phase))
    save_png(img, ASSETS / name)


# ---------------------------------------------------------------- HTML
def e(s):
    return html.escape(s, quote=False)


def nb(s):
    """Escaped text with a non-breaking space before the last word (no one-word orphan line)."""
    t = e(s)
    i = t.rfind(" ")
    return t if i < 0 else t[:i] + "&nbsp;" + t[i + 1:]


def button(href, label, utm_content, width=280, height=56, outline=False, bg="#FFFFFF"):
    url = f"{href}?{UTM}&amp;utm_content={utm_content}"
    r = height // 2
    if outline:
        vml = (f'<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" '
               f'href="{url}" style="height:{height}px;v-text-anchor:middle;width:{width}px;" arcsize="50%" '
               f'strokecolor="#000000" strokeweight="2px" fillcolor="{bg}">')
        a = (f'<a href="{url}" target="_blank" class="tb" style="background-color:{bg};border:2px solid #000000;'
             f'border-radius:{r}px;color:#000000;display:inline-block;font-family:Arial,Helvetica,sans-serif;'
             f'font-size:16px;font-weight:bold;line-height:{height - 4}px;text-align:center;text-decoration:none;'
             f'width:{width - 4}px;max-width:100%;-webkit-text-size-adjust:none;">{e(label)}</a>')
        colour, fs = "#000000", 16
    else:
        vml = (f'<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" '
               f'href="{url}" style="height:{height}px;v-text-anchor:middle;width:{width}px;" arcsize="50%" '
               f'stroke="f" fillcolor="#000000">')
        a = (f'<a href="{url}" target="_blank" class="to btn-m" style="background-color:#000000;border-radius:{r}px;'
             f'color:#FAA61A;display:inline-block;font-family:Arial,Helvetica,sans-serif;font-size:18px;'
             f'font-weight:bold;line-height:{height}px;text-align:center;text-decoration:none;width:{width}px;'
             f'max-width:100%;-webkit-text-size-adjust:none;">{e(label)}</a>')
        colour, fs = "#FAA61A", 18
    return (f'<div>\n        <!--[if mso]>\n        {vml}\n          <w:anchorlock/><center style="color:{colour};'
            f'font-family:Arial,Helvetica,sans-serif;font-size:{fs}px;font-weight:bold;">{e(label)}</center>\n'
            f'        </v:roundrect>\n        <![endif]-->\n        <!--[if !mso]><!-- -->{a}<!--<![endif]-->\n      </div>')


def cart_row(img, name, qty, price, url):
    return f'''          <tr>
            <td class="cart-pad" style="padding:16px 20px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td class="cart-img" width="96" valign="middle" style="width:96px;">
                    <a href="{url}" target="_blank" style="display:block;"><img src="{img}" width="96" height="96" alt="{e(name)}" class="cart-img" style="display:block;width:96px;height:96px;border:0;border-radius:12px;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#000000;"></a>
                  </td>
                  <td valign="middle" style="padding:0 12px 0 16px;text-align:left;">
                    <p class="tb cart-name" style="margin:0 0 4px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:22px;line-height:24px;font-weight:bold;color:#000000;">{e(name)}</p>
                    <p class="tb" style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:20px;color:#000000;">{e(COPY["qty_label"])} {e(qty)}</p>
                  </td>
                  <td class="cart-price" width="90" align="right" valign="middle" style="width:90px;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:22px;font-weight:bold;color:#000000;text-align:right;white-space:nowrap;"><span class="tb" style="color:#000000;">{e(price)}</span></td>
                </tr>
              </table>
            </td>
          </tr>'''


CART_DIVIDER = '''          <tr><td style="padding:0 20px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td height="1" bgcolor="#000000" style="height:1px;font-size:1px;line-height:1px;background-color:#000000;">&nbsp;</td></tr></table></td></tr>'''


# theMarketer: the abandoned-cart product feed block is inserted by hand in the
# theMarketer editor, in place of this row (it renders products, qty, price itself).
THEMARKETER_FEED = '''          <!-- THEMARKETER_FEED: inlocuieste acest rand cu blocul de produse din cos (feed theMarketer) -->
          <tr>
            <td style="padding:16px 20px 20px 20px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;">
                <tr><td align="center" style="border:2px dashed #000000;border-radius:12px;padding:28px 16px;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:22px;color:#000000;">
                  <span style="font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:20px;font-weight:bold;">[FEED PRODUSE THEMARKETER]</span><br>
                  Inserează aici blocul cu produsele din coș.
                </td></tr>
              </table>
            </td>
          </tr>
          <!-- /THEMARKETER_FEED -->'''


def cart_rows(esp):
    if esp:
        return THEMARKETER_FEED, None
    rows = []
    for i, it in enumerate(CART_EXAMPLE):
        rows.append(f"          <!-- CART_ITEM_ROW (EXEMPLU {i + 1}: preview only, replaced by the ESP loop; see index-esp.html) -->")
        rows.append(cart_row(it["img"], it["name"], it["qty"], it["price"], "{{CHECKOUT_URL}}"))
        if i < len(CART_EXAMPLE) - 1:
            rows.append(CART_DIVIDER)
    return "\n".join(rows), CART_TOTAL_EXAMPLE


CART_TOTAL_ROW = """          <!-- CART_TOTAL_ROW (optional: delete if the ESP gives no cart total; total excludes shipping) -->
          <tr>
            <td bgcolor="#000000" style="background-color:#000000;border-radius:0 0 18px 18px;padding:14px 20px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td class="to" align="left" style="font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:22px;font-weight:bold;color:#FAA61A;">{total_label}</td>
                  <td class="to" align="right" style="font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:22px;font-weight:bold;color:#FAA61A;text-align:right;white-space:nowrap;">{cart_total}</td>
                </tr>
              </table>
            </td>
          </tr>
          <!-- /CART_TOTAL_ROW -->"""


def usp_col(icon, title, line):
    return f'''<div class="usp" style="display:inline-block;width:100%;max-width:173px;vertical-align:top;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
          <tr><td align="center" style="padding:0 8px 24px 8px;">
            <img src="assets/{icon}" width="64" height="64" alt="" style="display:block;width:64px;height:64px;border:0;margin:0 auto 14px auto;">
            <p class="tb" style="margin:0 0 6px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:20px;line-height:22px;font-weight:bold;letter-spacing:0.5px;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">{e(title)}</p>
            <p class="tb" style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:20px;color:#000000;">{nb(line)}</p>
          </td></tr>
        </table>
      </div>'''


HTML = Template(r'''<!DOCTYPE html>
<html lang="ro" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="x-apple-disable-message-reformatting">
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>${title}</title>
<!-- GENERATED by build.py: edit COPY in build.py (texts from copy.md), not this file. -->
<!--[if mso]>
<noscript><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript>
<style>td,th,div,p,a,h1,h2,h3{font-family:Arial,Helvetica,sans-serif;}</style>
<![endif]-->
<!-- Akrobat webfont: licenta comerciala (inclusiv webfont) obligatorie inainte de trimitere. La upload in ESP, inlocuieste assets/ cu URL-uri absolute HTTPS. -->
<!--[if !mso]><!-->
<style>
  @font-face{font-family:'Akrobat';font-style:normal;font-weight:700;src:url('assets/fonts/Akrobat-Bold.woff2') format('woff2'),url('assets/fonts/Akrobat-Bold.woff') format('woff');}
  @font-face{font-family:'Akrobat';font-style:normal;font-weight:900;src:url('assets/fonts/Akrobat-Black.woff2') format('woff2'),url('assets/fonts/Akrobat-Black.woff') format('woff');}
</style>
<!--<![endif]-->
<style>
  :root{color-scheme:light;supported-color-schemes:light;}
  body{margin:0;padding:0;width:100%!important;background-color:#FFFFFF;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;}
  table{border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt;}
  img{border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;display:block;}
  p,h1,h2,h3{margin:0;}
  a[x-apple-data-detectors]{color:inherit!important;text-decoration:none!important;font-size:inherit!important;font-family:inherit!important;font-weight:inherit!important;line-height:inherit!important;}
  u + #body a{color:inherit;text-decoration:none;font-size:inherit;font-family:inherit;font-weight:inherit;line-height:inherit;}
  #MessageViewBody a{color:inherit;text-decoration:none;font-size:inherit;font-family:inherit;font-weight:inherit;line-height:inherit;}
  .ul{text-decoration:underline!important;}
  @media only screen and (max-width:599px){
    .wrap{width:100%!important;max-width:100%!important;}
    .px{padding-left:20px!important;padding-right:20px!important;}
    .fluid{width:100%!important;max-width:100%!important;height:auto!important;}
    .inner{width:100%!important;}
    .btn-m{width:100%!important;max-width:335px!important;}
    .h-hero{font-size:40px!important;line-height:40px!important;}
    .h-xl{font-size:30px!important;line-height:30px!important;}
    .cart-pad{padding:14px 14px!important;}
    .cart-img{width:72px!important;height:72px!important;}
    .cart-name{font-size:19px!important;line-height:21px!important;}
    .cart-price{width:76px!important;font-size:15px!important;}
    .usp{max-width:300px!important;display:block!important;margin:0 auto!important;}
    .stack{display:block!important;width:100%!important;box-sizing:border-box!important;}
    .s5-text{padding:8px 20px 8px 20px!important;text-align:center!important;}
    .s5-btn{margin:0 auto!important;}
  }
  [data-ogsc] .tb{color:#000000!important;}
  [data-ogsc] .to{color:#FAA61A!important;}
</style>
</head>
<body id="body" style="margin:0;padding:0;background-color:#FFFFFF;">

<!-- Preheader (subiect A recomandat: „${title}”) -->
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">${preheader}${pad}</div>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;">
<tr><td align="center" valign="top">

<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td><![endif]-->
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" align="center" style="width:600px;max-width:600px;">

  <!-- ============ S0 LOGO (pink) ============ -->
  <tr>
    <td align="center" bgcolor="#F7ACB4" style="background-color:#F7ACB4;padding:24px 20px 4px 20px;">
      <a href="https://lucasbites.ro" target="_blank" style="display:inline-block;"><img src="assets/logo.png" width="180" height="${logo_h}" alt="${alt_logo}" style="display:block;width:180px;height:auto;border:0;font-family:Arial,Helvetica,sans-serif;font-size:20px;font-weight:bold;color:#000000;"></a>
    </td>
  </tr>

  <!-- ============ S1 HERO: pink, floating stack, annotations (baked), white panel with rounded top corners (baked) ============ -->
  <tr>
    <td bgcolor="#F7ACB4" style="background-color:#F7ACB4;font-size:0;line-height:0;">
      <a href="{{CHECKOUT_URL}}?${utm}&amp;utm_content=hero" target="_blank" style="display:block;"><img src="assets/hero.jpg" width="600" height="500" alt="${alt_hero}" class="fluid" style="display:block;width:600px;max-width:100%;height:auto;border:0;font-family:Arial,Helvetica,sans-serif;font-size:16px;color:#000000;"></a>
    </td>
  </tr>

  <!-- ============ S1 TEXT + S2 CART + S3 CTA (white panel) ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:0 40px 0 40px;">
      <!-- Greeting: ESP condition, fallback „Hei!” when FIRST_NAME is empty or longer than 19 characters (copy.md S1) -->
      <p class="tb" style="margin:0 0 8px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:22px;line-height:26px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:#000000;">${greeting}</p>
      <h1 class="tb h-hero" style="margin:0 0 16px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:52px;line-height:50px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">${h1_l1}<br>${h1_l2}</h1>
      <p class="tb" style="margin:0 0 28px 0;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#000000;">${intro}</p>

      <!-- ===================== CART_ITEMS START ({{CART_ITEMS}}) ===================== -->
      <table role="presentation" class="inner" width="520" cellpadding="0" cellspacing="0" border="0" align="center" style="width:520px;border:2px solid #000000;border-radius:20px;border-collapse:separate;border-spacing:0;">
          <tr>
            <td align="left" style="padding:20px 20px 4px 20px;">
              <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;">
                <tr><td class="to" bgcolor="#000000" style="background-color:#000000;border-radius:16px;padding:6px 14px;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:16px;line-height:18px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:#FAA61A;">${cart_label}</td></tr>
              </table>
            </td>
          </tr>
${cart_rows}
${cart_total_row}
      </table>
      <!-- ===================== CART_ITEMS END ===================== -->
    </td>
  </tr>
  <tr>
    <td class="px" align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:28px 40px 36px 40px;">
      ${cta_main}
    </td>
  </tr>
  <tr>
    <td bgcolor="#86D2DA" style="background-color:#86D2DA;font-size:0;line-height:0;">
      <img src="assets/wave-white-turq.png" width="600" height="48" alt="" class="fluid" style="display:block;width:600px;max-width:100%;height:auto;border:0;">
    </td>
  </tr>

  <!-- ============ S4 USP (turquoise, 3 columns desktop, stacked mobile) ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#86D2DA" style="background-color:#86D2DA;padding:12px 40px 16px 40px;">
      <h2 class="tb h-xl" style="margin:0 0 28px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:34px;line-height:34px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">${usp_title}</h2>
    </td>
  </tr>
  <tr>
    <td align="center" bgcolor="#86D2DA" style="background-color:#86D2DA;padding:0 40px 16px 40px;font-size:0;text-align:center;">
<!--[if mso]><table role="presentation" width="519" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td width="173" valign="top"><![endif]-->
      ${usp1}<!--[if mso]></td><td width="173" valign="top"><![endif]-->${usp2}<!--[if mso]></td><td width="173" valign="top"><![endif]-->${usp3}
<!--[if mso]></td></tr></table><![endif]-->
    </td>
  </tr>
  <tr>
    <td bgcolor="#FAA61A" style="background-color:#FAA61A;font-size:0;line-height:0;">
      <img src="assets/wave-turq-orange.png" width="600" height="48" alt="" class="fluid" style="display:block;width:600px;max-width:100%;height:auto;border:0;">
    </td>
  </tr>

  <!-- ============ S5 CLOSING (orange): text left, crepes plate cut by the right edge ============ -->
  <tr>
    <td bgcolor="#FAA61A" style="background-color:#FAA61A;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td class="stack s5-text" width="380" valign="middle" align="left" style="width:380px;padding:8px 0 8px 40px;text-align:left;">
            <h2 class="tb h-xl" style="margin:0 0 12px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:34px;line-height:34px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">${s5_title}</h2>
            <p class="tb" style="margin:0 0 22px 0;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#000000;">${s5_line}</p>
            <table role="presentation" class="s5-btn" cellpadding="0" cellspacing="0" border="0"><tr><td>
      ${cta_shop}
            </td></tr></table>
            <p class="tb" style="margin:20px 0 0 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:30px;line-height:32px;font-weight:bold;color:#000000;">${signature}</p>
          </td>
          <td class="stack" width="220" valign="middle" align="right" style="width:220px;font-size:0;line-height:0;">
            <img src="assets/s5-clatite.jpg" width="220" height="300" alt="${alt_crepes}" align="right" style="display:block;width:220px;height:300px;border:0;margin-left:auto;font-family:Arial,Helvetica,sans-serif;font-size:14px;color:#000000;">
          </td>
        </tr>
      </table>
    </td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" style="background-color:#FFFFFF;font-size:0;line-height:0;">
      <img src="assets/wave-orange-white.png" width="600" height="48" alt="" class="fluid" style="display:block;width:600px;max-width:100%;height:auto;border:0;">
    </td>
  </tr>

  <!-- ============ S6 FOOTER (same structure as welcome) ============ -->
  <tr>
    <td class="px" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:8px 40px 0 40px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td height="1" bgcolor="#000000" style="height:1px;font-size:1px;line-height:1px;background-color:#000000;">&nbsp;</td></tr></table>
    </td>
  </tr>
  <tr>
    <td align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:32px 20px 0 20px;">
      <img src="assets/logo-stripes.png" width="260" height="${stripes_h}" alt="${alt_footer_logo}" style="display:block;width:260px;height:auto;border:0;margin:0 auto;font-family:Arial,Helvetica,sans-serif;font-size:16px;font-weight:bold;color:#000000;">
    </td>
  </tr>
  <tr>
    <td align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:24px 20px 24px 20px;">
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center">
        <tr>
          <td style="padding:0 7px;"><a href="https://www.instagram.com/lucas_bites/" target="_blank"><img src="assets/icon-instagram.png" width="32" height="32" alt="Instagram" style="display:block;width:32px;height:32px;border:0;font-family:Arial,Helvetica,sans-serif;font-size:11px;color:#000000;"></a></td>
          <td style="padding:0 7px;"><a href="https://www.tiktok.com/@lucas.bites.ro" target="_blank"><img src="assets/icon-tiktok.png" width="32" height="32" alt="TikTok" style="display:block;width:32px;height:32px;border:0;font-family:Arial,Helvetica,sans-serif;font-size:11px;color:#000000;"></a></td>
          <td style="padding:0 7px;"><a href="https://www.facebook.com/Lucas-Bites-101759484548844" target="_blank"><img src="assets/icon-facebook.png" width="32" height="32" alt="Facebook" style="display:block;width:32px;height:32px;border:0;font-family:Arial,Helvetica,sans-serif;font-size:11px;color:#000000;"></a></td>
          <td style="padding:0 7px;"><a href="https://www.youtube.com/@lucasbites2267" target="_blank"><img src="assets/icon-youtube.png" width="32" height="32" alt="YouTube" style="display:block;width:32px;height:32px;border:0;font-family:Arial,Helvetica,sans-serif;font-size:11px;color:#000000;"></a></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr>
    <td class="px tb" align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:0 48px 40px 48px;font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:20px;color:#000000;">
      <p class="tb" style="margin:0 0 4px 0;color:#000000;">Lucas Bites &middot; Roșu, Chiajna, Ilfov</p>
      <p class="tb" style="margin:0 0 4px 0;color:#000000;">[DE CONFIRMAT: denumire juridică SRL] &middot; CUI [DE CONFIRMAT]</p>
      <p class="tb" style="margin:0 0 16px 0;color:#000000;"><a href="mailto:office@lucasbites.ro" class="tb" style="color:#000000;text-decoration:none;">office@lucasbites.ro</a> &middot; <a href="tel:+40731399399" class="tb" style="color:#000000;text-decoration:none;">+40 731 399 399</a></p>
      <p class="tb" style="margin:0 0 16px 0;color:#000000;">${footer_why}</p>
      <p class="tb" style="margin:0 0 16px 0;color:#000000;">${footer_unsub_pre} <a href="{{UNSUBSCRIBE_URL}}" target="_blank" class="tb ul" style="color:#000000;text-decoration:underline;">${footer_unsub_link}</a>. ${footer_unsub_post}</p>
      <p class="tb" style="margin:0;color:#000000;">&copy; 2026 Lucas Bites</p>
    </td>
  </tr>

</table>
<!--[if mso]></td></tr></table><![endif]-->

</td></tr>
</table>
</body>
</html>
''')


def build_html(logo_h, stripes_h):
    pad = "&#847;&zwnj;&nbsp;" * 40
    usp_icons = ("usp-transport.png", "usp-timp.png", "usp-ingrediente.png")
    common = {k: e(v) for k, v in COPY.items() if isinstance(v, str)}
    for k in ("intro", "s5_line", "footer_why"):
        common[k] = nb(COPY[k])
    common.update(
        pad=pad, utm=UTM, logo_h=logo_h, stripes_h=stripes_h,
        cta_main=button("{{CHECKOUT_URL}}", COPY["cta_main"], "cta_main"),
        cta_shop=button("{{SHOP_URL}}", COPY["cta_shop"], "cta_shop", width=260, height=48, outline=True, bg="#FAA61A"),
        usp1=usp_col(usp_icons[0], *COPY["usp"][0]),
        usp2=usp_col(usp_icons[1], *COPY["usp"][1]),
        usp3=usp_col(usp_icons[2], *COPY["usp"][2]),
    )
    for name, esp in (("index.html", False), ("index-esp.html", True)):
        rows, total = cart_rows(esp)
        total_row = "" if total is None else CART_TOTAL_ROW.format(total_label=common["total_label"], cart_total=e(total))
        out = HTML.substitute(common, cart_rows=rows, cart_total_row=total_row)
        (HERE / name).write_text(out, encoding="utf-8")
        report.append(f"{name}  {len(out.encode('utf-8')) // 1024}KB")


# ---------------------------------------------------------------- previews (optional, headless Chrome)
def trim_bottom(img):
    """Remove the empty white canvas below the email (footer is white too, keep 0 margin)."""
    rgb = img.convert("RGB")
    bg = Image.new("RGB", rgb.size, WHITE)
    bbox = ImageChops.difference(rgb, bg).getbbox()
    return rgb.crop((0, 0, rgb.width, min(rgb.height, bbox[3] + 40))) if bbox else rgb


def build_previews():
    if not Path(CHROME).exists():
        print(f"Preview skipped: Chrome not found at {CHROME}")
        return
    # Headless Chrome enforces a minimum window width (~500px), so the email is
    # rendered inside an iframe of the exact width (its own viewport, media
    # queries apply) and the screenshot is cropped to that width.
    with tempfile.TemporaryDirectory() as tmp:
        for w, out in ((600, "preview.png"), (375, "preview-mobile.png")):
            shot = Path(tmp) / out
            frame = Path(tmp) / f"frame-{w}.html"
            frame.write_text(f'<!DOCTYPE html><html><body style="margin:0;background:#FFFFFF;">'
                             f'<iframe src="{(HERE / "index.html").as_uri()}" width="{w}" height="7000" '
                             f'style="border:0;display:block;"></iframe></body></html>', encoding="utf-8")
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                            "--allow-file-access-from-files",
                            f"--window-size={max(w, 800)},7000", f"--screenshot={shot}", frame.as_uri()],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
            img = Image.open(shot)
            img = trim_bottom(img.crop((0, 0, w, img.height)))
            img.save(HERE / out, optimize=True)
            report.append(f"{out}  {img.width}x{img.height}")


# ---------------------------------------------------------------- main
def main():
    ASSETS.mkdir(exist_ok=True)
    IMAGES.mkdir(exist_ok=True)
    logo_h, stripes_h = build_logos()
    copy_shared()
    wave_divider("wave-white-turq.png", WHITE, TURQ, phase=1.3, periods=1.2)
    wave_divider("wave-turq-orange.png", TURQ, ORANGE, phase=3.6, periods=1.3)
    wave_divider("wave-orange-white.png", ORANGE, WHITE, phase=5.0, periods=1.15)
    build_hero()
    build_crepes()
    build_cart_examples()
    build_usp_icons()
    build_html(logo_h, stripes_h)
    if "--preview" in sys.argv:
        build_previews()
    print("Built:")
    for line in report:
        print("  " + line)
    # self-contained copies for Figma import (images + fonts embedded)
    sys.path.insert(0, str(HERE.parent.parent / "tools"))
    from figma_export import export
    export(HERE)


if __name__ == "__main__":
    main()
