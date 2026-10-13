#!/usr/bin/env python3
"""Lucas Bites, Checkout Started Email 2: asset + HTML builder.

Based on ../email-01/build.py (same cutout, cart block, footer, preview method).

Usage:
  python3 build.py              build assets/ and index.html + index-esp.html
  python3 build.py --preview    same, then preview.png (600px) and preview-mobile.png (375px)
                                with headless Google Chrome (macOS path, see CHROME below)

Needs Pillow only (no network). If Pillow is missing:
  python3 -m venv .venv && .venv/bin/pip install Pillow && .venv/bin/python build.py

- Photos dropped into images/ (names from image-prompts.md, .png/.jpg/.jpeg) are cut
  out locally (plain white background removed, same method as Email 1) and
  pre-composited as opaque JPGs: the hero (orange, five drawn stars, overhead plate
  crossing the scalloped edge into white) and the closing cookies on black.
- Missing photos get a placeholder at the final size and final file name, so the
  layout never changes: add the photos, rerun, done.
- Texts come from copy.md (Email Marketing Strategist) and live in COPY below,
  verbatim. Change copy.md first, then COPY.
- index.html     = preview, cart block filled with 2 rows marked EXEMPLU.
  index-esp.html = theMarketer version: cart block holds a [FEED PRODUSE THEMARKETER]
                   placeholder, replaced by the product feed in the theMarketer editor.

Brand colours only: #FAA61A, #F7ACB4, #86D2DA, #000000, plus white.
Transition motif of this email: scalloped edge (biscuit edge), drawn here.
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
FONT_ANNOT = [ROOT / "Fonturi" / "Akrobat-Bold.otf",
              Path("/System/Library/Fonts/Supplemental/Arial Narrow Bold.ttf")]

UTM = "utm_source=email&amp;utm_medium=flow&amp;utm_campaign=checkout_02"

# ---------------------------------------------------------------- COPY (verbatim from copy.md)
COPY = {
    "title": "Nu ne crede pe cuvânt",
    "preheader": "Peste 1.100 de recenzii, media 4,9 din 5. Plus transport gratuit de la al 2-lea produs.",
    "greeting": "Hei, {{FIRST_NAME}}!",            # ESP: fallback „Hei!” (copy.md S1)
    "h1_l1": "NU NE CREDE",
    "h1_l2": "PE CUVÂNT.",
    "intro": "Ai ales deja. Înainte să termini comanda, uite ce spun cei care le-au făcut acasă.",
    "cart_label": "ÎN COȘUL TĂU",
    "qty_label": "Cantitate:",
    "total_label": "Total produse:",
    "cta_main": "Finalizează comanda",
    "rev_title": "CE SPUN CLIENȚII",
    "rev_score": "4,9",
    "rev_score_of": "din 5",
    "rev_count": "peste 1.100 de recenzii",
    # (quote, name, product); first one = wide card, next two = two columns
    "reviews": [
        ("„Au ieșit excelent și au fost foarte ușor de preparat. Mi-a plăcut în mod deosebit că nu au fost dulci.”",
         "Kinga L.", "Classic Pankees"),
        ("„Extraordinar de bune, se prepară rapid iar copilul le adoră!!!”", "Carmen N.", "Buttermilk Pankees"),
        ("„Aleg mereu mixul Pizza Crust pentru o pizza rapidă, cu ingrediente din frigider.”",
         "Luminița B.", "Pizza Crust Mix"),
    ],
    "usp_title": "CA SĂ COMANZI LINIȘTIT",
    # (icon, title, line); the support line is built from the contact links (email / phone)
    "usp": [("usp-suport.png", "ÎNTREBĂRI? SCRIE-NE.", None),
            ("usp-transport.png", "TRANSPORT GRATUIT", "Când pui al 2-lea produs în coș."),
            ("usp-ingrediente.png", "ȘTII CE E ÎN MIX", "Fără conservanți. Zahăr brun din trestie.")],
    "s6_title": "TE AȘTEPTĂM LA MASĂ.",
    "s6_line": "Finalizezi comanda, iar partea bună abia începe.",
    "cta_close": "Finalizează comanda",
    "signature": "eat what you love",
    "alt_logo": "Lucas Bites",
    "alt_hero": "Mini pancakes așezate în cerc pe o farfurie neagră, cu zmeură, sub cinci steluțe desenate",
    "alt_cookies": "Fursecuri cu bucăți de ciocolată, unul rupt în două",
    "alt_stars": "Rating 4,9 din 5",
    "alt_footer_logo": "Lucas Bites, eat what you love",
    "footer_why": "Primești acest email pentru că ai început o comandă pe lucasbites.ro și ai acceptat să primești emailuri de la noi.",
    "footer_unsub_pre": "Nu mai vrei emailuri de la noi?",
    "footer_unsub_link": "Dezabonează-te aici",
    "footer_unsub_post": "Durează un click.",
}
SUPPORT_EMAIL = "office@lucasbites.ro"
SUPPORT_PHONE = ("+40 731 399 399", "+40731399399")
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
NO_SHADOW = set()             # both photos keep their soft contact shadow


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
def placeholder_ring_plate(n):
    """Top-down black plate with mini pancakes in a ring and raspberries."""
    S = 2
    N = n * S
    img = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse((N * 0.02, N * 0.02, N * 0.98, N * 0.98), fill=PLATE + (255,), outline=BLACK + (255,), width=4 * S)
    c = N / 2
    for i in range(9):
        a = 2 * math.pi * i / 9 - math.pi / 2
        x, y, r = c + N * 0.30 * math.cos(a), c + N * 0.30 * math.sin(a), N * 0.105
        d.ellipse((x - r, y - r, x + r, y + r), fill=GOLD + (255,), outline=BLACK + (255,), width=4 * S)
        a2 = a + math.pi / 9
        x2, y2, r2 = c + N * 0.30 * math.cos(a2), c + N * 0.30 * math.sin(a2), N * 0.028
        d.ellipse((x2 - r2, y2 - r2, x2 + r2, y2 + r2), fill=PINK + (255,), outline=BLACK + (255,), width=3 * S)
    img = img.resize((n, n), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    centered_text(d, (0, n * 0.40, n, n * 0.60), [("IMG1", font(n // 11)), ("mini pancakes în cerc", font(n // 28, False))],
                  fill=WHITE)
    return img


def placeholder_cookies(w, h):
    """A few chocolate chip cookies, one broken (stylised)."""
    S = 2
    W, H = w * S, h * S
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for (fx, fy, fr) in ((0.30, 0.55, 0.20), (0.58, 0.42, 0.22), (0.80, 0.62, 0.15)):
        r = W * fr * 0.62
        d.ellipse((W * fx - r, H * fy - r, W * fx + r, H * fy + r), fill=GOLD + (255,), outline=BLACK + (255,), width=4 * S)
        for k in range(5):
            a = k * 1.3
            cx, cy = W * fx + r * 0.5 * math.cos(a), H * fy + r * 0.5 * math.sin(a)
            d.ellipse((cx - r * 0.09, cy - r * 0.09, cx + r * 0.09, cy + r * 0.09), fill=BLACK + (255,))
    img = img.resize((w, h), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    centered_text(d, (0, 0, w, h * 0.2), [("IMG2", font(h // 9)), ("fursecuri cu ciocolată", font(h // 22, False))],
                  fill=ORANGE)
    return img


# ---------------------------------------------------------------- decorative drawing
def star_points(cx, cy, r, inner=0.45, n=5, rot=-math.pi / 2):
    return [(cx + (r if i % 2 == 0 else r * inner) * math.cos(rot + i * math.pi / n),
             cy + (r if i % 2 == 0 else r * inner) * math.sin(rot + i * math.pi / n)) for i in range(2 * n)]


def scallop_mask(w, h, base, r, fill_below=True):
    """Mask of the lower colour: straight edge at `base` with semicircle bumps of
    radius r hanging down from the upper colour (biscuit edge). Supersampled."""
    W, H, R, B = w * SS, h * SS, r * SS, base * SS
    m = Image.new("L", (W, H), 255)
    d = ImageDraw.Draw(m)
    d.rectangle((0, 0, W, B), fill=0)
    n = round(w / (2 * r))
    step = W / n
    for i in range(n):
        cx = step * (i + 0.5)
        d.ellipse((cx - R, B - R, cx + R, B + R), fill=0)
    return m.resize((w, h), Image.LANCZOS)


def scallop_divider(name, top, bottom, h=44, r=30):
    """1200 x h (shown 600 x h/2): `top` colour with round bumps biting into `bottom`."""
    img = Image.new("RGB", (1200, h), top)
    img.paste(Image.new("RGB", (1200, h), bottom), (0, 0), scallop_mask(1200, h, h - r - 6, r))
    save_png(img, ASSETS / name)


def build_stars_row():
    """Five black stars for the 4,9 average: four full, the fifth filled 90% (4,9 of 5),
    black outline so the unfilled sliver still reads. 200 x 36 shown (400 x 72 export)."""
    W, H = 400 * SS, 72 * SS
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    r = 34 * SS
    lw = 4 * SS
    for i in range(5):
        cx = (40 + i * 80) * SS
        pts = star_points(cx, H / 2 + 2 * SS, r)
        if i < 4:
            ImageDraw.Draw(img).polygon(pts, fill=BLACK + (255,))
        else:
            fill = Image.new("L", (W, H), 0)
            ImageDraw.Draw(fill).polygon(pts, fill=255)
            clip = Image.new("L", (W, H), 0)
            ImageDraw.Draw(clip).rectangle((0, 0, cx - r + 2 * r * 0.9, H), fill=255)
            img.paste(Image.new("RGBA", (W, H), BLACK + (255,)), (0, 0), ImageChops.multiply(fill, clip))
            ImageDraw.Draw(img).line(pts + [pts[0]], fill=BLACK + (255,), width=lw, joint="curve")
    save_png(img.resize((400, 72), Image.LANCZOS), ASSETS / "stars-49.png")


def build_quote_mark():
    """Big black opening quote (two drawn commas), 44 x 34 shown (88 x 68 export)."""
    W, H = 88 * SS, 68 * SS
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for ox in (0, 46):
        x = ox * SS
        d.ellipse((x + 2 * SS, 30 * SS, x + 38 * SS, 66 * SS), fill=BLACK)
        d.polygon([(x + 4 * SS, 46 * SS), (x + 24 * SS, 2 * SS), (x + 36 * SS, 8 * SS), (x + 22 * SS, 40 * SS)], fill=BLACK)
    save_png(img.resize((88, 68), Image.LANCZOS), ASSETS / "quote.png")


# ---------------------------------------------------------------- hero
def build_hero():
    """1200 x 900 (shown 600 x 450), under the live H1 on orange: five black stars in
    an arc, the overhead plate below them; the orange ends in a scalloped edge at
    y~790 and the plate crosses it into the white (food 'out of frame')."""
    W, H = 1200, 900
    base, r = 800, 30
    canvas = Image.new("RGBA", (W, H), ORANGE + (255,))
    canvas.paste(Image.new("RGBA", (W, H), WHITE + (255,)), (0, 0), scallop_mask(W, H, base, r))

    deco = Image.new("RGBA", (W * 2, H * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(deco)
    for i in range(-2, 3):
        cx, cy = 600 + i * 92, 58 + abs(i) ** 2 * 9
        d.polygon(star_points(cx * 2, cy * 2, 34 * 2, rot=-math.pi / 2 + i * 0.12), fill=BLACK + (255,))
    for (x, y, s) in ((120, 260, 16), (1090, 210, 20), (150, 640, 22), (1070, 600, 14)):       # small outline sparkles
        d.line(star_points(x * 2, y * 2, s * 2, inner=0.3, n=4) + [star_points(x * 2, y * 2, s * 2, inner=0.3, n=4)[0]],
               fill=BLACK + (255,), width=8, joint="curve")
    canvas.alpha_composite(deco.resize((W, H), Image.LANCZOS))

    n = 740
    src, tag = load_cutout("img1-hero", lambda: placeholder_ring_plate(n))
    src = ImageOps.contain(src, (n, n), Image.LANCZOS)
    canvas.alpha_composite(src, ((W - src.width) // 2, 880 - src.height))
    save_jpg(canvas, ASSETS / "hero.jpg")
    report[-1] += f"  [{tag}]"


# ---------------------------------------------------------------- S6 cookies on black
def build_cookies():
    """720 x 440 (shown 360 x 220) on black, centred above the closing title."""
    W, H = 720, 440
    src, tag = load_cutout("img2-fursecuri", lambda: placeholder_cookies(660, 400))
    src = ImageOps.contain(src, (660, 410), Image.LANCZOS)
    canvas = Image.new("RGBA", (W, H), BLACK + (255,))
    canvas.alpha_composite(src, ((W - src.width) // 2, (H - src.height) // 2))
    save_jpg(canvas, ASSETS / "s6-fursecuri.jpg", JPG_MAX_SMALL)
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
    # support: speech bubble with three dots (email / phone help)
    img, d = base()
    d.rounded_rectangle((28 * u, 34 * u, 100 * u, 82 * u), radius=14 * u, outline=BLACK, width=lw)
    d.polygon([(44 * u, 80 * u), (40 * u, 100 * u), (62 * u, 80 * u)], fill=BLACK)
    for cx in (46, 64, 82):
        d.ellipse(((cx - 5) * u, 53 * u, (cx + 5) * u, 63 * u), fill=BLACK)
    done(img, "usp-suport.png")
    # wheat ear
    img, d = base()
    d.line([(64 * u, 104 * u), (64 * u, 40 * u)], fill=BLACK, width=lw)
    for i, y in enumerate((50, 64, 78)):
        for side in (-1, 1):
            d.polygon(rot_ellipse(64 * u + side * 12 * u, y * u, 13 * u, 6.5 * u, side * math.radians(-50)),
                      fill=BLACK)
    d.polygon(rot_ellipse(64 * u, 34 * u, 6.5 * u, 12 * u, 0), fill=BLACK)
    done(img, "usp-ingrediente.png")




# ---------------------------------------------------------------- logos, fonts, icons
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




# ---------------------------------------------------------------- HTML
def e(s):
    return html.escape(s, quote=False)


def nb(s):
    """Escaped text with a non-breaking space before the last word (no one-word orphan line)."""
    t = e(s)
    i = t.rfind(" ")
    return t if i < 0 else t[:i] + "&nbsp;" + t[i + 1:]


def button(href, label, utm_content, width=280, height=56, orange=False):
    """Bulletproof pill. Default: black fill, orange text (on white).
    orange=True: orange fill, black text (on the black closing section)."""
    url = f"{href}?{UTM}&amp;utm_content={utm_content}"
    r = height // 2
    fill, colour, cls = ("#FAA61A", "#000000", "tb") if orange else ("#000000", "#FAA61A", "to")
    vml = (f'<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" '
           f'href="{url}" style="height:{height}px;v-text-anchor:middle;width:{width}px;" arcsize="50%" '
           f'stroke="f" fillcolor="{fill}">')
    a = (f'<a href="{url}" target="_blank" class="{cls} btn-m" style="background-color:{fill};border-radius:{r}px;'
         f'color:{colour};display:inline-block;font-family:Arial,Helvetica,sans-serif;font-size:18px;'
         f'font-weight:bold;line-height:{height}px;text-align:center;text-decoration:none;width:{width}px;'
         f'max-width:100%;-webkit-text-size-adjust:none;">{e(label)}</a>')
    return (f'<div>\n        <!--[if mso]>\n        {vml}\n          <w:anchorlock/><center style="color:{colour};'
            f'font-family:Arial,Helvetica,sans-serif;font-size:18px;font-weight:bold;">{e(label)}</center>\n'
            f'        </v:roundrect>\n        <![endif]-->\n        <!--[if !mso]><!-- -->{a}<!--<![endif]-->\n      </div>')


def review_inner(quote, name, product, big):
    fs, lh = (18, 28) if big else (16, 24)
    return f'''<img src="assets/quote.png" width="44" height="34" alt="" style="display:block;width:44px;height:34px;border:0;margin:0 0 14px 0;">
                <p class="tb{' q-big' if big else ''}" style="margin:0 0 16px 0;font-family:Arial,Helvetica,sans-serif;font-size:{fs}px;line-height:{lh}px;color:#000000;">{nb(quote)}</p>
                <p class="tb" style="margin:0 0 2px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:20px;line-height:22px;font-weight:bold;color:#000000;">{e(name)}</p>
                <p class="tb" style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:20px;color:#000000;">{e(product)}</p>'''


def reviews_html():
    big, c1, c2 = COPY["reviews"]
    card = ("bgcolor=\"#FFFFFF\" style=\"background-color:#FFFFFF;border:2px solid #000000;border-radius:20px;"
            "padding:{p};text-align:left;\"")
    return f'''      <table role="presentation" class="inner" width="520" cellpadding="0" cellspacing="0" border="0" align="center" style="width:520px;border-collapse:separate;border-spacing:0;">
        <tr>
          <td class="rev-pad" valign="top" {card.format(p="26px 28px 26px 28px")}>
                {review_inner(*big, True)}
          </td>
        </tr>
      </table>
      <table role="presentation" class="inner" width="520" cellpadding="0" cellspacing="0" border="0" align="center" style="width:520px;border-collapse:separate;border-spacing:0;margin-top:20px;">
        <tr>
          <td class="stack rev-pad" width="250" valign="top" {card.format(p="22px 22px 22px 22px").replace('style="', 'style="width:250px;box-sizing:border-box;')}>
                {review_inner(*c1, False)}
          </td>
          <td class="stack rev-gap" width="20" style="width:20px;font-size:0;line-height:0;">&nbsp;</td>
          <td class="stack rev-pad" width="250" valign="top" {card.format(p="22px 22px 22px 22px").replace('style="', 'style="width:250px;box-sizing:border-box;')}>
                {review_inner(*c2, False)}
          </td>
        </tr>
      </table>'''


def nowrap_hyphen(s):
    """Escaped text where hyphenated words never split at the hyphen (e.g. SCRIE-NE.)."""
    return " ".join(f'<span style="white-space:nowrap;">{w}</span>' if "-" in w else w for w in e(s).split(" "))


def usp_col(icon, title, line):
    if line is None:          # support: email + phone, both links, fixed break
        body = (f'<a href="mailto:{SUPPORT_EMAIL}" class="tb" style="color:#000000;text-decoration:none;">{SUPPORT_EMAIL}</a><br>'
                f'<a href="tel:{SUPPORT_PHONE[1]}" class="tb" style="color:#000000;text-decoration:none;white-space:nowrap;">{SUPPORT_PHONE[0]}</a>')
    else:
        body = nb(line)
    return f'''<div class="usp" style="display:inline-block;width:100%;max-width:173px;vertical-align:top;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
          <tr><td align="center" style="padding:0 8px 24px 8px;">
            <img src="assets/{icon}" width="64" height="64" alt="" style="display:block;width:64px;height:64px;border:0;margin:0 auto 14px auto;">
            <p class="tb" style="margin:0 0 6px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:20px;line-height:22px;font-weight:bold;letter-spacing:0.5px;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">{nowrap_hyphen(title)}</p>
            <p class="tb" style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:20px;color:#000000;">{body}</p>
          </td></tr>
        </table>
      </div>'''


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
    .h-hero{font-size:44px!important;line-height:44px!important;}
    .h-xl{font-size:30px!important;line-height:30px!important;}
    .cart-pad{padding:14px 14px!important;}
    .cart-img{width:72px!important;height:72px!important;}
    .cart-name{font-size:19px!important;line-height:21px!important;}
    .cart-price{width:76px!important;font-size:15px!important;}
    .usp{max-width:300px!important;display:block!important;margin:0 auto!important;}
    .stack{display:block!important;width:100%!important;box-sizing:border-box!important;}
    .rev-gap{height:16px!important;}
    .rev-pad{padding:20px 20px!important;}
    .q-big{font-size:17px!important;line-height:26px!important;}
    .score{font-size:96px!important;line-height:96px!important;}
    .score-of{font-size:34px!important;}
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

  <!-- ============ S0 LOGO (orange) ============ -->
  <tr>
    <td align="center" bgcolor="#FAA61A" style="background-color:#FAA61A;padding:28px 20px 8px 20px;">
      <a href="https://lucasbites.ro" target="_blank" style="display:inline-block;"><img src="assets/logo.png" width="180" height="${logo_h}" alt="${alt_logo}" style="display:block;width:180px;height:auto;border:0;font-family:Arial,Helvetica,sans-serif;font-size:20px;font-weight:bold;color:#000000;"></a>
    </td>
  </tr>

  <!-- ============ S1 HERO TEXT (orange, live text) ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#FAA61A" style="background-color:#FAA61A;padding:24px 40px 4px 40px;">
      <!-- Greeting: ESP condition, fallback „Hei!” when FIRST_NAME is empty or longer than 19 characters (copy.md S1) -->
      <p class="tb" style="margin:0 0 8px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:22px;line-height:26px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:#000000;">${greeting}</p>
      <h1 class="tb h-hero" style="margin:0 0 16px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:56px;line-height:54px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">${h1_l1}<br>${h1_l2}</h1>
      <p class="tb" style="margin:0 auto;max-width:440px;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#000000;">${intro}</p>
    </td>
  </tr>

  <!-- ============ S1 HERO IMAGE: stars, overhead plate, scalloped edge orange -> white (baked) ============ -->
  <tr>
    <td bgcolor="#FFFFFF" style="background-color:#FFFFFF;font-size:0;line-height:0;">
      <a href="{{CHECKOUT_URL}}?${utm}&amp;utm_content=hero" target="_blank" style="display:block;"><img src="assets/hero.jpg" width="600" height="450" alt="${alt_hero}" class="fluid" style="display:block;width:600px;max-width:100%;height:auto;border:0;font-family:Arial,Helvetica,sans-serif;font-size:16px;color:#000000;"></a>
    </td>
  </tr>

  <!-- ============ S2 CART (white) ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:12px 40px 0 40px;">
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

  <!-- ============ S3 CTA (white) ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:28px 40px 40px 40px;">
      ${cta_main}
    </td>
  </tr>
  <tr>
    <td bgcolor="#F7ACB4" style="background-color:#F7ACB4;font-size:0;line-height:0;">
      <img src="assets/scallop-white-pink.png" width="600" height="22" alt="" class="fluid" style="display:block;width:600px;max-width:100%;height:auto;border:0;">
    </td>
  </tr>

  <!-- ============ S4 REVIEWS (pink): title, 4,9 din 5 + stars + count, 1 wide card + 2 cards ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#F7ACB4" style="background-color:#F7ACB4;padding:28px 40px 0 40px;">
      <h2 class="tb h-xl" style="margin:0 0 6px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:34px;line-height:34px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">${rev_title}</h2>
      <p class="tb" style="margin:0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-weight:900;color:#000000;mso-line-height-rule:exactly;"><span class="score" style="font-size:120px;line-height:118px;">${rev_score}</span><span class="score-of" style="font-size:40px;line-height:40px;">&nbsp;${rev_score_of}</span></p>
      <img src="assets/stars-49.png" width="200" height="36" alt="${alt_stars}" style="display:block;width:200px;height:36px;border:0;margin:0 auto 10px auto;font-family:Arial,Helvetica,sans-serif;font-size:14px;font-weight:bold;color:#000000;">
      <p class="tb" style="margin:0 0 28px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:20px;line-height:24px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:#000000;">${rev_count}</p>
    </td>
  </tr>
  <tr>
    <td class="px" align="center" bgcolor="#F7ACB4" style="background-color:#F7ACB4;padding:0 40px 44px 40px;">
${reviews}
    </td>
  </tr>
  <tr>
    <td bgcolor="#86D2DA" style="background-color:#86D2DA;font-size:0;line-height:0;">
      <img src="assets/scallop-pink-turq.png" width="600" height="22" alt="" class="fluid" style="display:block;width:600px;max-width:100%;height:auto;border:0;">
    </td>
  </tr>

  <!-- ============ S5 USP (turquoise, 3 columns desktop, stacked mobile) ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#86D2DA" style="background-color:#86D2DA;padding:28px 40px 16px 40px;">
      <h2 class="tb h-xl" style="margin:0 0 28px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:34px;line-height:34px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">${usp_title}</h2>
    </td>
  </tr>
  <tr>
    <td align="center" bgcolor="#86D2DA" style="background-color:#86D2DA;padding:0 40px 20px 40px;font-size:0;text-align:center;">
<!--[if mso]><table role="presentation" width="519" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td width="173" valign="top"><![endif]-->
      ${usp1}<!--[if mso]></td><td width="173" valign="top"><![endif]-->${usp2}<!--[if mso]></td><td width="173" valign="top"><![endif]-->${usp3}
<!--[if mso]></td></tr></table><![endif]-->
    </td>
  </tr>
  <tr>
    <td bgcolor="#000000" style="background-color:#000000;font-size:0;line-height:0;">
      <img src="assets/scallop-turq-black.png" width="600" height="22" alt="" class="fluid" style="display:block;width:600px;max-width:100%;height:auto;border:0;">
    </td>
  </tr>

  <!-- ============ S6 CLOSING (black, all text orange): cookies, title, line, orange pill, signature ============ -->
  <tr>
    <td align="center" bgcolor="#000000" style="background-color:#000000;padding:20px 20px 0 20px;font-size:0;line-height:0;">
      <img src="assets/s6-fursecuri.jpg" width="360" height="220" alt="${alt_cookies}" class="img-close" style="display:block;width:360px;max-width:100%;height:auto;border:0;margin:0 auto;font-family:Arial,Helvetica,sans-serif;font-size:14px;color:#FAA61A;">
    </td>
  </tr>
  <tr>
    <td class="px" align="center" bgcolor="#000000" style="background-color:#000000;padding:12px 40px 44px 40px;">
      <h2 class="to h-xl" style="margin:0 0 12px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:34px;line-height:34px;font-weight:900;text-transform:uppercase;color:#FAA61A;mso-line-height-rule:exactly;">${s6_title}</h2>
      <p class="to" style="margin:0 0 26px 0;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#FAA61A;">${s6_line}</p>
      ${cta_close}
      <p class="to" style="margin:24px 0 0 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:30px;line-height:32px;font-weight:bold;color:#FAA61A;">${signature}</p>
    </td>
  </tr>
  <tr>
    <td bgcolor="#FFFFFF" style="background-color:#FFFFFF;font-size:0;line-height:0;">
      <img src="assets/scallop-black-white.png" width="600" height="22" alt="" class="fluid" style="display:block;width:600px;max-width:100%;height:auto;border:0;">
    </td>
  </tr>

  <!-- ============ S7 FOOTER (same structure as welcome) ============ -->
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
    common = {k: e(v) for k, v in COPY.items() if isinstance(v, str)}
    for k in ("intro", "s6_line", "footer_why"):
        common[k] = nb(COPY[k])
    common.update(
        pad=pad, utm=UTM, logo_h=logo_h, stripes_h=stripes_h,
        cta_main=button("{{CHECKOUT_URL}}", COPY["cta_main"], "cta_main"),
        cta_close=button("{{CHECKOUT_URL}}", COPY["cta_close"], "cta_final", orange=True),
        reviews=reviews_html(),
        usp1=usp_col(*COPY["usp"][0]),
        usp2=usp_col(*COPY["usp"][1]),
        usp3=usp_col(*COPY["usp"][2]),
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
    scallop_divider("scallop-white-pink.png", WHITE, PINK)
    scallop_divider("scallop-pink-turq.png", PINK, TURQ)
    scallop_divider("scallop-turq-black.png", TURQ, BLACK)
    scallop_divider("scallop-black-white.png", BLACK, WHITE)
    build_hero()
    build_cookies()
    build_cart_examples()
    build_usp_icons()
    build_stars_row()
    build_quote_mark()
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
