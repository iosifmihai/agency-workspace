#!/usr/bin/env python3
"""Lucas Bites, Browse Abandonment Email 1: asset + HTML builder.

Usage:
  .venv/bin/python build.py              build assets/, index.html, index-esp.html, Figma copies
  .venv/bin/python build.py --preview    same, then preview.png (600px) and preview-mobile.png (375px)
                                         with headless Google Chrome (macOS path, see CHROME below)

Needs Pillow only (no network). If Pillow is missing:
  python3 -m venv .venv && .venv/bin/pip install Pillow && .venv/bin/python build.py

- Photos dropped into images/ (names from image-prompts.md, .png/.jpg/.jpeg) are cropped
  into arch frames (recipes) or cut out (S5 crepes, plain white background removed with
  the same method as welcome-03 / checkout-started) and pre-composited on the section colour.
- Recipe 2 (pizza) is an animated GIF. Input, first match wins:
    images/rec2-pizza.gif  -> frames read with Pillow
    images/rec2-pizza.mp4  -> frames extracted with ffmpeg (only if `ffmpeg` is on PATH)
    images/rec2-pizza.png  -> still first frame only (static GIF)
  Every frame is put in the arch frame, then the GIF is written under GIF_MAX bytes
  (scale, colours and frame rate are reduced step by step until it fits).
- Missing photos get a placeholder at the final size and final file name, so the
  layout never changes: add the photos, rerun, done.
- Texts come from copy.md (Copywriter) and live in COPY below, verbatim.
  Change copy.md first, then COPY.
- index.html     = preview, viewed-product card filled with an example marked EXEMPLU.
  index-esp.html = theMarketer version: the card holds [PRODUS VIZUALIZAT THEMARKETER]
                   between THEMARKETER_FEED comments, replaced by hand in the theMarketer editor.

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
    from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps, ImageSequence
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

SS = 4
JPG_MAX = 300_000
JPG_MAX_SMALL = 120_000
GIF_MAX = 1_000_000                          # strategy.md: GIF max 1 MB
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_NUM = [ROOT / "Fonturi" / "Akrobat-Black.otf", Path(FONT_BOLD)]

UTM = "utm_source=email&amp;utm_medium=flow&amp;utm_campaign=browse_01"

# The optional "craving" line on the recipe cards (copy.md S3, open question 2).
# Set to False to keep the cards strictly title / product / info / CTA.
SHOW_CRAVING_LINE = True

# ---------------------------------------------------------------- COPY (verbatim from copy.md)
COPY = {
    "title": "Trei idei pentru pofta de azi",
    "preheader": "Pankees de post, pizza cu pepperoni sau brownie cu fructe de pădure?",
    "greeting": "Hei, {{FIRST_NAME}}!",            # ESP: fallback „Hei!” (copy.md S1)
    "h1_l1": "CE FACI CU",
    "h1_l2": "POFTA ASTA?",
    "intro": "Pentru fiecare poftă există un moment. Uite trei idei de pus pe masă, când ai chef.",
    "chip": "PE LISTA DE POFTE",
    "cta_product": "Vezi produsul",
    "fallback_line": "Toate mixurile Lucas Bites, într-un singur loc.",
    "fallback_cta": "Răsfoiește gama",
    "s3_eyebrow": "trei momente, trei mixuri",
    "s3_h2_l1": "CE IESE",
    "s3_h2_l2": "DINTR-UN MIX",
    "s3_intro": "Una de post, una sărată și una dulce. Tu alegi ordinea.",
    "cta_recipe": "Vezi rețeta",
    "all_recipes": "Toate rețetele",
    "usp_title": "DE CE LUCAS BITES?",
    "usp": [("4,9 DIN 5", "Din peste 1.100 de recenzii ale clienților."),
            ("CE E ÎN MIX", "Ingrediente pe care le recunoști, puse la cântar."),
            ("TRANSPORT GRATUIT", "De la al 2-lea mix, ca să încerci două rețete.")],
    "s5_title_l1": "POFTA NU",
    "s5_title_l2": "SE GRĂBEȘTE.",
    "s5_line": "Când ești gata: pancakes, clătite, prăjituri și pizza, toate aici.",
    "cta_shop": "Alege-ți pofta",
    "signature": "eat what you love",
    "alt_logo": "Lucas Bites",
    "alt_footer_logo": "Lucas Bites, eat what you love",
    # copy.md section 3 says the S5 alt is written after the image is chosen: UI proposal, to approve
    "alt_s5": "Teanc de clătite subțiri, aurii, cu zahăr pudră",
    "footer_why": "Primești acest email pentru că ai acceptat să primești emailuri de la Lucas Bites.",
    "footer_unsub_pre": "Nu mai vrei emailuri de la noi?",
    "footer_unsub_link": "Dezabonează-te aici",
    "footer_unsub_post": "Durează un click.",
}
RECIPES = [
    {"stem": "rec1-pankees", "out": "rec1-pankees.jpg", "num": "01", "badge": ORANGE,
     "moment": "vegan / de post", "t1": "PANKEES DE POST", "t2": "CU FRUCTE",
     "product": "Cu Vegan Classic Pankees", "info": "De post · 15 min",
     "craving": "Tu adaugi apă, agiți și gătești.",
     "url": "{{URL_RETETA_POST}}", "utm": "reteta_1",
     "alt": "Teanc scurt de Pankees de post cu fructe proaspete", "ph": PINK, "ph_sub": "pankees de post"},
    {"stem": "rec2-pizza", "out": "rec2-pizza.gif", "num": "02", "badge": PINK,
     "moment": "movie night", "t1": "PIZZA DE CASĂ", "t2": "CU PEPPERONI",
     "product": "Cu Pizza Crust Mix", "info": "Familie · 30 min",
     "craving": "Pizza de casă la începutul filmului.",
     "url": "{{URL_RETETA_PIZZA}}", "utm": "reteta_2",
     "alt": "Pizza de casă cu pepperoni, abia scoasă, din care ies aburi", "ph": ORANGE, "ph_sub": "GIF pizza, cadrul 1"},
    {"stem": "rec3-brownie", "out": "rec3-brownie.jpg", "num": "03", "badge": TURQ,
     "moment": "pauza de la birou", "t1": "BROWNIE CU FRUCTE", "t2": "DE PĂDURE",
     "product": "Cu Brownie Mix", "info": "Desert · 35 min",
     "craving": "De adus colegilor, la cafeaua de la 11.",
     "url": "{{URL_RETETA_BROWNIE}}", "utm": "reteta_3",
     "alt": "Brownie cu fructe de pădure deasupra", "ph": TURQ, "ph_sub": "brownie, 30-45 grade"},
]
# Example viewed product (preview only, clearly marked). No real product, no real price.
PRODUCT_EXAMPLE = {"img": "assets/product-example.png", "name": "Nume produs", "price": "XX,XX lei"}

# Display geometry of the recipe arch images (px, email size)
ARCH_CANVAS = (220, 290)                     # whole image incl. the number badge margin
ARCH_BOX = (6, 22, 202, 286)                 # arch frame: x0, y0 (top of the curve), x1, y1

report = []


# ---------------------------------------------------------------- helpers
def font(size, bold=True):
    path = FONT_BOLD if bold else FONT_REG
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default(size=size)


def num_font(size):
    for p in FONT_NUM:
        if Path(p).exists():
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


def find_input(stem, exts=(".png", ".jpg", ".jpeg")):
    for p in sorted(IMAGES.glob("*")):
        if p.stem.lower() == stem.lower() and p.suffix.lower() in exts:
            return p
    return None


def cover(img, size):
    """Scale and centre-crop to fill `size` exactly (like CSS object-fit: cover)."""
    return ImageOps.fit(ImageOps.exif_transpose(img).convert("RGB"), size, Image.LANCZOS, centering=(0.5, 0.5))


# ---------------------------------------------------------------- cutout (same method as welcome-03 / checkout-started)
WHITE_MIN = 225
SAT_MAX = 14
CHECKER_MIN = 170
WORK_MAX = 1600
SHADOW_MIN = 120
SHADOW_SAT = 26
SHADOW_GAIN = 0.40
NO_SHADOW = set()


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


# ---------------------------------------------------------------- decorative drawing
def sparkle(d, cx, cy, r, fill=ORANGE):
    """4-point sparkle with black outline (like the logo letters)."""
    pts = []
    for i in range(8):
        a = -math.pi / 2 + i * math.pi / 4
        rr = r if i % 2 == 0 else r * 0.28
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d.polygon(pts, fill=fill + (255,), outline=BLACK + (255,), width=max(3, int(r * 0.08)))


def arch_mask(size, box, s=SS):
    """Mask (at `size`) of an arch: semicircular top, straight sides, flat bottom."""
    W, H = size[0] * s, size[1] * s
    x0, y0, x1, y1 = (v * s for v in box)
    r = (x1 - x0) / 2
    m = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(m)
    d.ellipse((x0, y0, x1, y0 + 2 * r), fill=255)
    d.rectangle((x0, y0 + r, x1, y1), fill=255)
    return m.resize(size, Image.LANCZOS)


def arch_outline(layer, box, width, s=SS):
    """Draw a black arch outline on an RGBA layer of the same size (supersampled)."""
    W, H = layer.size
    big = Image.new("RGBA", (W * s, H * s), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)
    x0, y0, x1, y1 = (v * s for v in box)
    r = (x1 - x0) / 2
    lw = int(width * s)
    d.arc((x0, y0, x1, y0 + 2 * r), 180, 360, fill=BLACK + (255,), width=lw)
    d.line([(x0 + lw / 2, y0 + r), (x0 + lw / 2, y1 - lw / 2)], fill=BLACK + (255,), width=lw)
    d.line([(x1 - lw / 2, y0 + r), (x1 - lw / 2, y1 - lw / 2)], fill=BLACK + (255,), width=lw)
    d.line([(x0, y1 - lw / 2), (x1, y1 - lw / 2)], fill=BLACK + (255,), width=lw)
    layer.alpha_composite(big.resize((W, H), Image.LANCZOS))


def number_badge(layer, cx, cy, r, fill, text):
    """Round badge with black outline and the recipe number (decorative, alt in HTML)."""
    s = SS
    W, H = layer.size
    big = Image.new("RGBA", (W * s, H * s), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)
    d.ellipse(((cx - r) * s, (cy - r) * s, (cx + r) * s, (cy + r) * s), fill=fill + (255,),
              outline=BLACK + (255,), width=int(max(3, r * 0.12) * s))
    f = num_font(int(r * 0.95 * s))
    bb = d.textbbox((0, 0), text, font=f)
    d.text((cx * s - (bb[0] + bb[2]) / 2, cy * s - (bb[1] + bb[3]) / 2), text, font=f, fill=BLACK + (255,))
    layer.alpha_composite(big.resize((W, H), Image.LANCZOS))


# ---------------------------------------------------------------- transitions: arch ("boltă")
def dome_divider(name, top, bottom, h=40):
    """1200 x 2h (shown 600 x h): `top` colour; `bottom` colour rises as one wide
    elliptical arch spanning the full width (echo of the arch photo frames)."""
    W, H = 1200, h * 2
    m = Image.new("L", (W * SS, H * SS), 0)
    ImageDraw.Draw(m).ellipse((-W * 0.04 * SS, 0, W * 1.04 * SS, H * 2 * SS), fill=255)
    img = Image.new("RGB", (W, H), top)
    img.paste(Image.new("RGB", (W, H), bottom), (0, 0), m.resize((W, H), Image.LANCZOS))
    save_png(img, ASSETS / name)


# ---------------------------------------------------------------- hero ornament + S2 card cap
def build_sparkles():
    """140 x 40 shown (280 x 80): three sparkles in brand colours, on turquoise."""
    W, H = 280, 80
    big = Image.new("RGBA", (W * SS, H * SS), TURQ + (255,))
    d = ImageDraw.Draw(big)
    for (x, y, r, c) in ((60, 46, 22, ORANGE), (140, 34, 30, PINK), (220, 48, 20, ORANGE)):
        sparkle(d, x * SS, y * SS, r * SS, c)
    save_png(big.resize((W, H), Image.LANCZOS).convert("RGB"), ASSETS / "sparkles.png")


def build_card_cap():
    """520 x 96 shown (1040 x 192): turquoise outside, pink arch (the top of the
    viewed-product card), round orange badge with a sparkle at top left (Bello badge)."""
    W, H = 1040, 192
    img = Image.new("RGBA", (W, H), TURQ + (255,))
    m = Image.new("L", (W * SS, H * SS), 0)
    ImageDraw.Draw(m).ellipse((0, 0, W * SS - 1, H * 2 * SS), fill=255)
    img.paste(Image.new("RGBA", (W, H), PINK + (255,)), (0, 0), m.resize((W, H), Image.LANCZOS))
    big = Image.new("RGBA", (W * SS, H * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)
    cx, cy, r = 176, 112, 56
    d.ellipse(((cx - r) * SS, (cy - r) * SS, (cx + r) * SS, (cy + r) * SS), fill=ORANGE + (255,),
              outline=BLACK + (255,), width=6 * SS)
    sparkle(d, cx * SS, cy * SS, 34 * SS, WHITE)
    sparkle(d, 880 * SS, 118 * SS, 22 * SS, ORANGE)
    img.alpha_composite(big.resize((W, H), Image.LANCZOS))
    save_png(img.convert("RGB"), ASSETS / "card-cap.png")


def build_product_example():
    """Preview only: 160 x 160 shown (320 x 320). White tile with an arch in light
    turquoise, label EXEMPLU / produs vizualizat, round orange EXEMPLU badge."""
    n = 320
    img = Image.new("RGBA", (n, n), WHITE + (255,))
    box = (60, 24, 260, 300)
    img.paste(Image.new("RGBA", (n, n), TURQ + (255,)), (0, 0), arch_mask((n, n), box))
    arch_outline(img, box, 4)
    d = ImageDraw.Draw(img)
    centered_text(d, (60, 120, 260, 260), [("EXEMPLU", font(30)), ("produs", font(22, False)),
                                            ("vizualizat", font(22, False))])
    save_png(img.convert("RGB"), ASSETS / "product-example.png")


# ---------------------------------------------------------------- recipe arch images
def arch_canvas(scale):
    w, h = ARCH_CANVAS
    return (round(w * scale), round(h * scale)), tuple(round(v * scale) for v in ARCH_BOX)


def placeholder_photo(size, colour, label, sub):
    img = Image.new("RGB", size, colour)
    d = ImageDraw.Draw(img)
    w, h = size
    # a simple round "plate" so the arch reads as food
    d.ellipse((w * 0.12, h * 0.42, w * 0.88, h * 0.42 + w * 0.76), fill=WHITE, outline=BLACK, width=max(3, w // 90))
    d.ellipse((w * 0.26, h * 0.42 + w * 0.14, w * 0.74, h * 0.42 + w * 0.62), fill=colour, outline=BLACK,
              width=max(3, w // 90))
    centered_text(d, (0, h * 0.14, w, h * 0.38), [(label, font(w // 9)), (sub, font(w // 20, False))])
    return img


def compose_arch(photo, scale, num, badge):
    """Photo (RGB) covered into the arch, white outside, black outline, number badge."""
    size, box = arch_canvas(scale)
    canvas = Image.new("RGBA", size, WHITE + (255,))
    inner = cover(photo, (box[2] - box[0], box[3] - box[1]))
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    layer.paste(inner, (box[0], box[1]))
    canvas.paste(layer, (0, 0), arch_mask(size, box))
    arch_outline(canvas, box, 3 * scale)
    number_badge(canvas, size[0] - 28 * scale, 34 * scale, 25 * scale, badge, num)
    return canvas.convert("RGB")


def build_recipe_still(rec):
    p = find_input(rec["stem"])
    photo = Image.open(p) if p else placeholder_photo((392, 528), rec["ph"], "REC" + rec["num"][-1], rec["ph_sub"])
    img = compose_arch(photo, 2, rec["num"], rec["badge"])
    save_jpg(img, ASSETS / rec["out"], JPG_MAX_SMALL)
    report[-1] += f"  [{'real' if p else 'placeholder'}]"


def gif_frames():
    """Return (frames as RGB, durations in ms, source tag) for recipe 2."""
    gif = find_input("rec2-pizza", (".gif",))
    if gif:
        im = Image.open(gif)
        frames, durs = [], []
        for fr in ImageSequence.Iterator(im):
            frames.append(fr.convert("RGB"))
            durs.append(fr.info.get("duration", im.info.get("duration", 80)) or 80)
        return frames, durs, f"gif {gif.name}"
    mp4 = find_input("rec2-pizza", (".mp4", ".mov"))
    if mp4:
        ff = shutil.which("ffmpeg")
        if not ff:
            try:  # ffmpeg bundled in .venv (pip install imageio-ffmpeg)
                import imageio_ffmpeg
                ff = imageio_ffmpeg.get_ffmpeg_exe()
            except ImportError:
                pass
        if ff:
            with tempfile.TemporaryDirectory() as tmp:
                # 12 frames/second, max 4 seconds (strategy.md: 2-4 s, max ~15 fps)
                subprocess.run([ff, "-v", "error", "-i", str(mp4), "-t", "4", "-vf", "fps=12",
                                str(Path(tmp) / "f_%03d.png")], check=True)
                files = sorted(Path(tmp).glob("f_*.png"))
                frames = [Image.open(f).convert("RGB") for f in files]
            return frames, [83] * len(frames), f"mp4 {mp4.name} via ffmpeg"
        print(f"NOTE: {mp4.name} found but ffmpeg is not installed: convert it to images/rec2-pizza.gif "
              "by hand (see image-prompts.md), or install ffmpeg. Using the still frame for now.")
    still = find_input("rec2-pizza")
    if still:
        return [Image.open(still).convert("RGB")], [1000], f"still {still.name}"
    rec = RECIPES[1]
    return [placeholder_photo((392, 528), rec["ph"], "REC2", rec["ph_sub"])], [1000], "placeholder"


def write_gif(frames, durs, scale, colours, step, path):
    rec = RECIPES[1]
    frames, durs = frames[::step], [sum(durs[i:i + step]) for i in range(0, len(durs), step)]
    comp = [compose_arch(f, scale, rec["num"], rec["badge"]) for f in frames]
    # one global palette taken from the first frame (it is the Outlook frame, keep it best)
    pal = comp[0].quantize(colors=colours, method=Image.Quantize.MEDIANCUT)
    # median cut averages colours: snap the nearest entries back to exact white, black and
    # the badge colour, so the GIF edges match the white section and the other arches
    p = pal.getpalette()[:colours * 3]
    for target in (WHITE, BLACK, rec["badge"]):
        i = min(range(len(p) // 3), key=lambda k: sum((p[3 * k + j] - target[j]) ** 2 for j in range(3)))
        p[3 * i:3 * i + 3] = list(target)
    pal.putpalette(p)
    # frame 1 = the median-cut image itself (exact mapping; Pillow's quantize(palette=...)
    # lookup is approximate). Later frames keep frame 1's pixels wherever the picture did
    # not change, so static areas never flicker and the GIF stays small (cinemagraph).
    first = pal
    q = [first]
    for c in comp[1:]:
        moved = ImageChops.difference(c, comp[0]).convert("L").point(lambda v: 255 if v > 10 else 0)
        fr = first.copy()
        fr.paste(c.quantize(palette=pal, dither=Image.Dither.NONE), (0, 0), moved)
        q.append(fr)
    buf = BytesIO()
    if len(q) == 1:
        q[0].save(buf, "GIF", optimize=True)
    else:
        q[0].save(buf, "GIF", save_all=True, append_images=q[1:], duration=durs, loop=0, optimize=True,
                  disposal=1)
    return buf.getvalue(), len(q), comp[0].size


def build_recipe_gif():
    frames, durs, tag = gif_frames()
    data = None
    for scale in (1.5, 1.25, 1.0):
        for colours in (160, 128, 96, 64):
            for step in ((1, 2) if len(frames) > 1 else (1,)):
                data, n, size = write_gif(frames, durs, scale, colours, step, None)
                if len(data) <= GIF_MAX:
                    break
            if len(data) <= GIF_MAX:
                break
        if len(data) <= GIF_MAX:
            break
    out = ASSETS / RECIPES[1]["out"]
    out.write_bytes(data)
    flag = "" if len(data) <= GIF_MAX else "  !! OVER 1 MB, shorten the clip"
    report.append(f"assets/{out.name}  {size[0]}x{size[1]}  {n} frame(s)  {colours} colours  "
                  f"{len(data) // 1024}KB  [{tag}]{flag}")


# ---------------------------------------------------------------- S5 crepes in a circle
def placeholder_crepes(n):
    S = 2
    N = n * S
    img = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for i in range(6):                                      # flat stack, bottom to top
        y = N * (0.78 - i * 0.07)
        d.ellipse((N * 0.08, y - N * 0.12, N * 0.92, y + N * 0.12), fill=ORANGE + (255,),
                  outline=BLACK + (255,), width=4 * S)
    img = img.resize((n, n), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    centered_text(d, (0, n * 0.04, n, n * 0.26), [("IMG S5", font(n // 10)), ("teanc de clătite", font(n // 22, False))])
    return img


def build_s5_plate():
    """360 x 280 shown (720 x 560) on pink: orange circle with black outline, the
    crepes cutout overlaps its top edge (food breaking out of the frame, Bello)."""
    W, H = 720, 560
    canvas = Image.new("RGBA", (W, H), PINK + (255,))
    big = Image.new("RGBA", (W * SS, H * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)
    cx, cy, r = 360, 330, 220
    d.ellipse(((cx - r) * SS, (cy - r) * SS, (cx + r) * SS, (cy + r) * SS), fill=ORANGE + (255,),
              outline=BLACK + (255,), width=6 * SS)
    for (x, y, rr) in ((96, 120, 26), (630, 96, 20), (650, 430, 16)):
        sparkle(d, x * SS, y * SS, rr * SS, ORANGE)
    canvas.alpha_composite(big.resize((W, H), Image.LANCZOS))
    p = find_input("s5-clatite")
    src = cutout(Image.open(p), p.name, "s5-clatite") if p else placeholder_crepes(440)
    src = ImageOps.contain(src, (470, 420), Image.LANCZOS)
    canvas.alpha_composite(src, ((W - src.width) // 2, 500 - src.height))   # top pokes out above the circle
    save_jpg(canvas, ASSETS / "s5-clatite.jpg", JPG_MAX_SMALL)
    report[-1] += f"  [{'real' if p else 'placeholder'}]"


# ---------------------------------------------------------------- USP icons (new set: star, bowl + whisk, parcel)
def build_usp_icons():
    """64 x 64 shown (128 exported): white circle, black 3px ring, black pictogram."""
    N = 128 * SS
    lw = 6 * SS
    u = N / 128

    def base():
        img = Image.new("RGBA", (N, N), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        d.ellipse((lw / 2, lw / 2, N - lw / 2, N - lw / 2), fill=WHITE + (255,), outline=BLACK + (255,), width=lw)
        return img, d

    def done(img, name):
        save_png(img.resize((128, 128), Image.LANCZOS), ASSETS / name)

    # star (reviews)
    img, d = base()
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = 34 if i % 2 == 0 else 15
        pts.append((64 * u + rr * u * math.cos(a), 67 * u + rr * u * math.sin(a)))
    d.polygon(pts, fill=BLACK)
    done(img, "usp-recenzii.png")
    # bowl + whisk (what is in the mix)
    img, d = base()
    d.line([(78 * u, 26 * u), (62 * u, 58 * u)], fill=BLACK, width=lw)               # handle
    for dx in (-9, 0, 9):                                                             # whisk loops
        d.ellipse(((54 + dx * 0.6) * u, 52 * u, (70 + dx * 0.6 + abs(dx) * 0.4) * u, 78 * u), outline=BLACK,
                  width=int(lw * 0.7))
    d.chord((28 * u, 40 * u, 100 * u, 104 * u), 0, 180, fill=WHITE, outline=BLACK, width=lw)
    d.line([(24 * u, 72 * u), (104 * u, 72 * u)], fill=BLACK, width=lw)
    done(img, "usp-mix.png")
    # parcel (free shipping; the truck is used in checkout)
    img, d = base()
    d.polygon([(64 * u, 30 * u), (98 * u, 46 * u), (64 * u, 62 * u), (30 * u, 46 * u)], outline=BLACK, width=lw)
    d.polygon([(30 * u, 46 * u), (64 * u, 62 * u), (64 * u, 100 * u), (30 * u, 84 * u)], outline=BLACK, width=lw)
    d.polygon([(98 * u, 46 * u), (64 * u, 62 * u), (64 * u, 100 * u), (98 * u, 84 * u)], fill=BLACK)
    d.line([(47 * u, 38 * u), (81 * u, 54 * u)], fill=BLACK, width=lw)
    done(img, "usp-colet.png")


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


def nowrap_hyphen(s):
    """Keep hyphenated words whole (DINTR-UN, ALEGE-ȚI): browsers may break after a hyphen."""
    return " ".join(f'<span style="white-space:nowrap;">{e(w)}</span>' if "-" in w else e(w) for w in s.split(" "))


def button(href, label, utm_content, width=280, height=56, outline=False, bg="#FFFFFF", fs=None, cls="btn-m"):
    url = f"{href}?{UTM}&amp;utm_content={utm_content}"
    r = height // 2
    if outline:
        fs = fs or 16
        vml = (f'<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" '
               f'href="{url}" style="height:{height}px;v-text-anchor:middle;width:{width}px;" arcsize="50%" '
               f'strokecolor="#000000" strokeweight="2px" fillcolor="{bg}">')
        a = (f'<a href="{url}" target="_blank" class="tb" style="background-color:{bg};border:2px solid #000000;'
             f'border-radius:{r}px;color:#000000;display:inline-block;font-family:Arial,Helvetica,sans-serif;'
             f'font-size:{fs}px;font-weight:bold;line-height:{height - 4}px;text-align:center;text-decoration:none;'
             f'width:{width - 4}px;max-width:100%;-webkit-text-size-adjust:none;">{e(label)}</a>')
        colour = "#000000"
    else:
        fs = fs or 18
        vml = (f'<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" '
               f'href="{url}" style="height:{height}px;v-text-anchor:middle;width:{width}px;" arcsize="50%" '
               f'stroke="f" fillcolor="#000000">')
        a = (f'<a href="{url}" target="_blank" class="to {cls}" style="background-color:#000000;border-radius:{r}px;'
             f'color:#FAA61A;display:inline-block;font-family:Arial,Helvetica,sans-serif;font-size:{fs}px;'
             f'font-weight:bold;line-height:{height}px;text-align:center;text-decoration:none;width:{width}px;'
             f'max-width:100%;-webkit-text-size-adjust:none;">{e(label)}</a>')
        colour = "#FAA61A"
    return (f'<div>\n        <!--[if mso]>\n        {vml}\n          <w:anchorlock/><center style="color:{colour};'
            f'font-family:Arial,Helvetica,sans-serif;font-size:{fs}px;font-weight:bold;">{e(label)}</center>\n'
            f'        </v:roundrect>\n        <![endif]-->\n        <!--[if !mso]><!-- -->{a}<!--<![endif]-->\n      </div>')


# Preview example inside the white panel of the viewed-product card
PRODUCT_EXAMPLE_HTML = '''              <!-- PRODUS EXEMPLU (doar preview; in index-esp.html aici e placeholder-ul THEMARKETER_FEED) -->
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td class="pe-img" width="160" valign="middle" style="width:160px;padding:16px 0 16px 16px;">
                    <a href="{url}" target="_blank" style="display:block;"><img src="{img}" width="160" height="160" alt="{alt}" class="pe-img" style="display:block;width:160px;height:160px;border:0;font-family:Arial,Helvetica,sans-serif;font-size:12px;color:#000000;"></a>
                  </td>
                  <td valign="middle" style="padding:16px 20px 16px 20px;text-align:left;">
                    <p class="tb pe-name" style="margin:0 0 8px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:28px;line-height:30px;font-weight:bold;color:#000000;">{name}</p>
                    <p class="tb" style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:18px;line-height:24px;font-weight:bold;color:#000000;">{price}</p>
                  </td>
                </tr>
              </table>'''

THEMARKETER_FEED = '''              <!-- THEMARKETER_FEED START: inlocuieste acest bloc cu blocul de produs vizualizat din theMarketer (latime utila 476px desktop, 100% mobil) -->
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;">
                <tr><td align="center" style="padding:16px;">
                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;">
                    <tr><td align="center" style="border:2px dashed #000000;border-radius:12px;padding:32px 16px;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:22px;color:#000000;">
                      <span style="font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:20px;font-weight:bold;">[PRODUS VIZUALIZAT THEMARKETER]</span><br>
                      Inserează aici blocul cu produsul vizualizat.
                    </td></tr>
                  </table>
                </td></tr>
              </table>
              <!-- THEMARKETER_FEED END -->'''


def recipe_row(rec, first):
    url = f'{rec["url"]}?{UTM}&amp;utm_content={rec["utm"]}'
    w, h = ARCH_CANVAS
    craving = (f'\n            <p class="tb" style="margin:0 0 16px 0;font-family:Arial,Helvetica,sans-serif;font-size:15px;'
               f'line-height:22px;color:#000000;">{nb(rec["craving"])}</p>') if SHOW_CRAVING_LINE else ""
    gif_note = ("\n      <!-- GIF animat: Outlook desktop arata doar primul cadru (cadrul 1 = fotografie completa). -->"
                if rec["out"].endswith(".gif") else "")
    return f'''  <!-- RETETA {rec["num"]} -->
  <tr>
    <td class="px rec-pad" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:{8 if first else 28}px 40px 0 40px;">{gif_note}
      <!--[if mso]><table role="presentation" width="520" cellpadding="0" cellspacing="0" border="0"><tr><td width="220" valign="middle"><![endif]-->
      <div class="rec-col rec-img" style="display:inline-block;width:100%;max-width:220px;vertical-align:middle;">
        <a href="{url}" target="_blank" style="display:block;"><img src="assets/{rec["out"]}" width="{w}" height="{h}" alt="{e(rec["alt"])}" style="display:block;width:{w}px;height:{h}px;border:0;margin:0 auto;font-family:Arial,Helvetica,sans-serif;font-size:14px;color:#000000;"></a>
      </div><!--[if mso]></td><td width="300" valign="middle"><![endif]--><div class="rec-col rec-text" style="display:inline-block;width:100%;max-width:300px;vertical-align:middle;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
          <tr><td class="rec-tx" align="left" style="padding:0 0 0 24px;text-align:left;">
            <table role="presentation" class="rec-chip" cellpadding="0" cellspacing="0" border="0" align="left" style="border-collapse:separate;margin:0 0 12px 0;">
              <tr><td class="tb" style="border:2px solid #000000;border-radius:14px;padding:4px 12px;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:16px;line-height:18px;font-weight:bold;letter-spacing:0.5px;color:#000000;">{e(rec["moment"])}</td></tr>
            </table>
            <div style="clear:both;font-size:0;line-height:0;">&nbsp;</div>
            <h3 class="tb rec-title" style="margin:0 0 10px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:24px;line-height:26px;font-weight:bold;letter-spacing:0.5px;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;"><a href="{url}" target="_blank" class="tb" style="color:#000000;text-decoration:none;">{e(rec["t1"])}<br>{e(rec["t2"])}</a></h3>
            <p class="tb" style="margin:0 0 4px 0;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:22px;font-weight:bold;color:#000000;">{e(rec["product"])}</p>
            <p class="tb" style="margin:0 0 {10 if SHOW_CRAVING_LINE else 18}px 0;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:20px;color:#000000;">{e(rec["info"]).replace(" · ", " &middot; ")}</p>{craving}
            <table role="presentation" class="rec-btn" cellpadding="0" cellspacing="0" border="0" align="left"><tr><td>
      {button(rec["url"], COPY["cta_recipe"], rec["utm"], width=150, height=40, outline=True, fs=15)}
            </td></tr></table>
          </td></tr>
        </table>
      </div>
      <!--[if mso]></td></tr></table><![endif]-->
    </td>
  </tr>'''


def usp_col(icon, title, line):
    return f'''<div class="usp" style="display:inline-block;width:100%;max-width:173px;vertical-align:top;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
          <tr><td align="center" style="padding:0 8px 24px 8px;">
            <img src="assets/{icon}" width="64" height="64" alt="" style="display:block;width:64px;height:64px;border:0;margin:0 auto 14px auto;">
            <p class="tb" style="margin:0 0 6px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:20px;line-height:22px;font-weight:bold;letter-spacing:0.5px;text-transform:uppercase;white-space:nowrap;color:#000000;mso-line-height-rule:exactly;">{e(title)}</p>
            <p class="tb" style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:20px;color:#000000;">{nb(line)}</p>
          </td></tr>
        </table>
      </div>'''


def dome(name, colour):
    return f'''  <tr>
    <td bgcolor="{colour}" style="background-color:{colour};font-size:0;line-height:0;">
      <img src="assets/{name}" width="600" height="40" alt="" class="fluid" style="display:block;width:600px;max-width:100%;height:auto;border:0;">
    </td>
  </tr>'''


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
    .h-hero{font-size:46px!important;line-height:44px!important;}
    .h-xl{font-size:32px!important;line-height:32px!important;}
    .card-pad{padding-left:12px!important;padding-right:12px!important;}
    .pe-img{width:112px!important;height:112px!important;padding-left:10px!important;}
    .pe-name{font-size:22px!important;line-height:24px!important;}
    .rec-col{display:block!important;max-width:100%!important;width:100%!important;}
    .rec-img{margin:0 auto 14px auto!important;max-width:220px!important;}
    .rec-tx{padding:0!important;text-align:center!important;}
    .rec-chip{float:none!important;margin:0 auto 12px auto!important;}
    .rec-btn{float:none!important;margin:0 auto!important;}
    .rec-pad{padding-top:36px!important;}
    .usp{max-width:300px!important;display:block!important;margin:0 auto!important;}
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

  <!-- ============ S0 LOGO (turquoise) ============ -->
  <tr>
    <td align="center" bgcolor="#86D2DA" style="background-color:#86D2DA;padding:28px 20px 12px 20px;">
      <a href="https://lucasbites.ro" target="_blank" style="display:inline-block;"><img src="assets/logo.png" width="180" height="${logo_h}" alt="${alt_logo}" style="display:block;width:180px;height:auto;border:0;font-family:Arial,Helvetica,sans-serif;font-size:20px;font-weight:bold;color:#000000;"></a>
    </td>
  </tr>

  <!-- ============ S1 HERO (turquoise, text-led, no button) ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#86D2DA" style="background-color:#86D2DA;padding:4px 40px 28px 40px;text-align:center;">
      <img src="assets/sparkles.png" width="140" height="40" alt="" style="display:block;width:140px;height:40px;border:0;margin:0 auto 10px auto;">
      <!-- Greeting: ESP condition, fallback „Hei!” when FIRST_NAME is empty or longer than 19 characters (copy.md S1) -->
      <p class="tb" style="margin:0 0 8px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:22px;line-height:26px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:#000000;">${greeting}</p>
      <h1 class="tb h-hero" style="margin:0 0 16px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:60px;line-height:56px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">${h1_l1}<br>${h1_l2}</h1>
      <p class="tb" style="margin:0 auto;max-width:440px;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#000000;">${intro}</p>
    </td>
  </tr>

  <!-- ============ S2 VIEWED PRODUCT (pink arch card on turquoise) ============ -->
  <!-- VIEWED_PRODUCT START: daca blocul theMarketer nu randeaza (feed gol / produs scos), ascunde tot pana la VIEWED_PRODUCT END (copy.md S2, fallback recomandat) -->
  <tr>
    <td class="px" align="center" bgcolor="#86D2DA" style="background-color:#86D2DA;padding:0 40px 36px 40px;">
      <table role="presentation" class="inner" width="520" cellpadding="0" cellspacing="0" border="0" align="center" style="width:520px;border-collapse:separate;border-spacing:0;">
        <tr><td bgcolor="#86D2DA" style="background-color:#86D2DA;font-size:0;line-height:0;">
          <img src="assets/card-cap.png" width="520" height="96" alt="" class="fluid" style="display:block;width:520px;max-width:100%;height:auto;border:0;">
        </td></tr>
        <tr><td class="card-pad" align="center" bgcolor="#F7ACB4" style="background-color:#F7ACB4;border-radius:0 0 24px 24px;padding:0 20px 24px 20px;">
          <table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center" style="border-collapse:separate;margin:0 auto 16px auto;">
            <tr><td class="to" bgcolor="#000000" style="background-color:#000000;border-radius:16px;padding:6px 14px;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:16px;line-height:18px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:#FAA61A;">${chip}</td></tr>
          </table>
          <!-- Panou alb pentru blocul de produs: 480px exterior, 476px util (bordura 2px) -->
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:2px solid #000000;border-radius:16px;border-collapse:separate;">
            <tr><td align="left">
${product_block}
            </td></tr>
          </table>
          <!-- Buton sub bloc: STERGE-L daca blocul theMarketer are buton propriu (copy.md S2). {{PRODUCT_URL}} = linkul produsului din bloc. -->
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="padding:20px 0 0 0;">
      ${cta_product}
          </td></tr></table>
        </td></tr>
      </table>
    </td>
  </tr>
  <!-- VIEWED_PRODUCT END -->
${dome_turq_white}

  <!-- ============ S3 RECIPES (white): numbered list, arch photo left, text right ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:16px 40px 20px 40px;text-align:center;">
      <p class="tb" style="margin:0 0 8px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:22px;line-height:26px;font-weight:bold;letter-spacing:1px;color:#000000;">${s3_eyebrow}</p>
      <h2 class="tb h-xl" style="margin:0 0 12px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:40px;line-height:40px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">${s3_h2}</h2>
      <p class="tb" style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#000000;">${s3_intro}</p>
    </td>
  </tr>
${recipes}
  <tr>
    <td class="px" align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:36px 40px 36px 40px;">
      <a href="{{SHOP_URL}}/retete?${utm}&amp;utm_content=retete_toate" target="_blank" class="tb ul" style="font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:22px;line-height:26px;font-weight:bold;letter-spacing:0.5px;color:#000000;text-decoration:underline;">${all_recipes}</a>
    </td>
  </tr>
${dome_white_orange}

  <!-- ============ S4 USP (orange, 3 columns desktop, stacked mobile) ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#FAA61A" style="background-color:#FAA61A;padding:12px 40px 16px 40px;">
      <h2 class="tb h-xl" style="margin:0 0 28px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:34px;line-height:34px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">${usp_title}</h2>
    </td>
  </tr>
  <tr>
    <td align="center" bgcolor="#FAA61A" style="background-color:#FAA61A;padding:0 40px 20px 40px;font-size:0;text-align:center;">
<!--[if mso]><table role="presentation" width="519" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td width="173" valign="top"><![endif]-->
      ${usp1}<!--[if mso]></td><td width="173" valign="top"><![endif]-->${usp2}<!--[if mso]></td><td width="173" valign="top"><![endif]-->${usp3}
<!--[if mso]></td></tr></table><![endif]-->
    </td>
  </tr>
${dome_orange_pink}

  <!-- ============ S5 CLOSING (pink, centred): title, line, button, signature, crepes in an orange circle ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#F7ACB4" style="background-color:#F7ACB4;padding:16px 40px 8px 40px;text-align:center;">
      <h2 class="tb h-xl" style="margin:0 0 12px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:40px;line-height:40px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">${s5_title}</h2>
      <p class="tb" style="margin:0 auto 24px auto;max-width:400px;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#000000;">${s5_line}</p>
      ${cta_shop}
      <p class="tb" style="margin:20px 0 0 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:30px;line-height:32px;font-weight:bold;color:#000000;">${signature}</p>
    </td>
  </tr>
  <tr>
    <td align="center" bgcolor="#F7ACB4" style="background-color:#F7ACB4;padding:4px 20px 0 20px;font-size:0;line-height:0;">
      <a href="{{SHOP_URL}}?${utm}&amp;utm_content=cta_shop" target="_blank" style="display:inline-block;"><img src="assets/s5-clatite.jpg" width="360" height="280" alt="${alt_s5}" class="fluid" style="display:block;width:360px;max-width:100%;height:auto;border:0;margin:0 auto;font-family:Arial,Helvetica,sans-serif;font-size:14px;color:#000000;"></a>
    </td>
  </tr>
${dome_pink_white}

  <!-- ============ S6 FOOTER (same structure as welcome / checkout) ============ -->
  <tr>
    <td align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:24px 20px 0 20px;">
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
      <p class="tb" style="margin:0 0 4px 0;color:#000000;">[DE PRIMIT DE LA CLIENT: denumire juridică SRL] &middot; CUI [DE PRIMIT DE LA CLIENT]</p>
      <p class="tb" style="margin:0 0 16px 0;color:#000000;"><a href="mailto:office@lucasbites.ro" class="tb" style="color:#000000;text-decoration:none;">office@lucasbites.ro</a> &middot; <a href="tel:+40731399399" class="tb" style="color:#000000;text-decoration:none;">+40 731 399 399</a></p>
      <!-- Fraza „de ce primesti”: [DE CONFIRMAT CU ANDREEA] (copy.md S6). Daca o adauga Andreea in theMarketer, aici ramane markerul [ADAUGĂ UTILIZATORUL]. -->
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
    for k in ("intro", "s3_intro", "s5_line", "footer_why"):
        common[k] = nb(COPY[k])
    common.update(
        pad=pad, utm=UTM, logo_h=logo_h, stripes_h=stripes_h,
        s3_h2=f'{e(COPY["s3_h2_l1"])} {nowrap_hyphen(COPY["s3_h2_l2"])}',
        s5_title=f'{e(COPY["s5_title_l1"])}<br>{e(COPY["s5_title_l2"])}',
        cta_product=button("{{PRODUCT_URL}}", COPY["cta_product"], "cta_product", width=260, height=52),
        cta_shop=button("{{SHOP_URL}}", COPY["cta_shop"], "cta_shop"),
        recipes="\n".join(recipe_row(r, i == 0) for i, r in enumerate(RECIPES)),
        usp1=usp_col("usp-recenzii.png", *COPY["usp"][0]),
        usp2=usp_col("usp-mix.png", *COPY["usp"][1]),
        usp3=usp_col("usp-colet.png", *COPY["usp"][2]),
        dome_turq_white=dome("dome-turq-white.png", "#FFFFFF"),
        dome_white_orange=dome("dome-white-orange.png", "#FAA61A"),
        dome_orange_pink=dome("dome-orange-pink.png", "#F7ACB4"),
        dome_pink_white=dome("dome-pink-white.png", "#FFFFFF"),
    )
    example = PRODUCT_EXAMPLE_HTML.format(url="{{PRODUCT_URL}}", img=PRODUCT_EXAMPLE["img"],
                                          alt=e(PRODUCT_EXAMPLE["name"]) + " (EXEMPLU)",
                                          name=e(PRODUCT_EXAMPLE["name"]), price=e(PRODUCT_EXAMPLE["price"]))
    for name, block in (("index.html", example), ("index-esp.html", THEMARKETER_FEED)):
        out = HTML.substitute(common, product_block=block)
        (HERE / name).write_text(out, encoding="utf-8")
        kb = len(out.encode("utf-8")) / 1024
        report.append(f"{name}  {kb:.1f}KB" + ("  !! over 102 KB (Gmail clipping)" if kb > 102 else ""))


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
    dome_divider("dome-turq-white.png", TURQ, WHITE)
    dome_divider("dome-white-orange.png", WHITE, ORANGE)
    dome_divider("dome-orange-pink.png", ORANGE, PINK)
    dome_divider("dome-pink-white.png", PINK, WHITE)
    build_sparkles()
    build_card_cap()
    build_product_example()
    build_recipe_still(RECIPES[0])
    build_recipe_gif()
    build_recipe_still(RECIPES[2])
    build_s5_plate()
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
