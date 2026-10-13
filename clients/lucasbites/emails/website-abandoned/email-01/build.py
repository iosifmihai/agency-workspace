#!/usr/bin/env python3
"""Lucas Bites, Website Abandoned Email 1: asset + HTML builder.

Usage:
  .venv/bin/python build.py              build assets/, index.html, index-esp.html, Figma copies
  .venv/bin/python build.py --preview    same, then preview.png (600px) and preview-mobile.png (375px)
                                         with headless Google Chrome (macOS path, see CHROME below)

Needs Pillow only (no network). If Pillow is missing:
  python3 -m venv .venv && .venv/bin/pip install Pillow && .venv/bin/python build.py

- Photos dropped into images/ (names from image-prompts.md, .png/.jpg/.jpeg) are cropped
  square and framed as "torn recipe clippings": rounded top corners, torn bottom edge,
  composited on the white card. All 5 are full photos (no cutouts).
- Missing photos get a placeholder at the final size and final file name, so the
  layout never changes: add the photos, rerun, done.
- Texts come from copy.md (Copywriter) and live in COPY / CATS / REVIEWS below, verbatim.
  Change copy.md first, then these.
- index.html     = preview.
  index-esp.html = theMarketer version: same email (no dynamic product feed here), plus
                   ESP-MARKER comments where Andreea sets something by hand in theMarketer.

Helpers (save_jpg/png, find_input, cover, button, footer, previews, logos, fonts) are
copied from ../../browse-abandonment/email-01/build.py and adapted (that file is not
importable as a module: its paths point to its own folder).

Brand colours only: #FAA61A, #F7ACB4, #86D2DA, #000000, plus white.
"""
import html
import math
import random
import shutil
import subprocess
import sys
import tempfile
from io import BytesIO
from pathlib import Path
from string import Template

try:
    from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps
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
JPG_MAX_SMALL = 110_000
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

UTM = "utm_source=email&amp;utm_medium=flow&amp;utm_campaign=website_01"

# ---------------------------------------------------------------- COPY (verbatim from copy.md)
COPY = {
    "title": "Un tur scurt prin mixurile noastre",
    "preheader": "Pancakes, prăjituri, budinci și pizza, plus ce spun cei care le-au încercat.",
    "greeting": "Hei, {{FIRST_NAME}}!",            # ESP: fallback „Hei!” (copy.md S1)
    "h1_l1": "CE PUNEM AZI",
    "h1_l2": "PE MASĂ?",
    "intro": "Mixuri în care e deja aproape tot, de la micul dejun la movie night. Le luăm pe rând.",
    "s2_eyebrow": "cinci feluri de poftă",
    "s2_h2": "CE GĂSEȘTI LA NOI",
    "s2_intro": "Alege o categorie și vezi toate mixurile din ea.",
    "all_products": "Vezi toate produsele",
    "s3_title": "ÎNCERCATE ȘI NOTATE",
    "rating": "4,9",
    "rating_of": "din 5",
    "rating_sub": "peste 1.100 de recenzii",
    "all_reviews": "Vezi toate recenziile",
    "usp_title": "BINE DE ȘTIUT",
    "usp": [("APROAPE TOT E ÎN MIX", "Tu adaugi doar ce scrie pe ambalaj."),
            ("ȘI ÎN MAGAZINE", "Kaufland, Carrefour, Dr. Max, eMAG și altele."),
            ("TRANSPORT GRATUIT", "Când combini două mixuri, livrarea e pe noi.")],
    "s5_title_l1": "NU ȘTII DE UNDE",
    "s5_title_l2": "SĂ ÎNCEPI?",
    "s5_line": "Începe cu pancakes. Sau cu pizza. Sau cu amândouă.",
    "cta_shop": "Vezi toată gama",
    "signature": "eat what you love",
    "pro_line": "Ai cafenea, restaurant sau patiserie? Aceeași rețetă, porții constante, preparare rapidă în bucătărie.",
    "pro_link": "Vezi gama Professional",
    "alt_logo": "Lucas Bites",
    "alt_footer_logo": "Lucas Bites, eat what you love",
    "alt_stars": "Rating 4,9 din 5",
    "footer_why": "Primești acest email pentru că ai acceptat să primești emailuri de la Lucas Bites.",
    "footer_unsub_pre": "Nu mai vrei emailuri de la noi?",
    "footer_unsub_link": "Dezabonează-te aici",
    "footer_unsub_post": "Durează un click.",
}
# Category cards (copy.md S2, order from strategy.md). Card 5 is a single product
# (client answer 13.10.2026): CTA „Vezi produsul”, placeholder stays {{CATEGORY_URL_5}}.
CATS = [
    {"stem": "cat1-pancakes", "moment": "micul dejun în familie", "name": "PANCAKES & CRÊPES",
     "line": "Pancakes pufoase și clătite subțiri.", "cta": "Vezi categoria",
     "url": "{{CATEGORY_URL_1}}", "utm": "cat_pancakes", "ph": PINK, "ph_sub": "clătite cu lămâie",
     "alt": "Clătite împăturite cu lămâie și zahăr, cu pancakes în spate"},
    {"stem": "cat2-prajituri", "moment": "pauza de la birou", "name": "PRĂJITURI",
     "line": "Patru mixuri, dintre care două noi în gamă.", "cta": "Vezi categoria",
     "url": "{{CATEGORY_URL_2}}", "utm": "cat_prajituri", "ph": ORANGE, "ph_sub": "carrot cake",
     "alt": "Felie de carrot cake cu morcov ras și nuci"},
    {"stem": "cat3-budinci", "moment": "nou în gamă", "name": "BUDINCI",
     "line": "Un desert de lingură, nou la Lucas Bites.", "cta": "Vezi categoria",
     "url": "{{CATEGORY_URL_3}}", "utm": "cat_budinci", "ph": TURQ, "ph_sub": "lingură de budincă",
     "alt": "Lingură plină cu budincă cremoasă, dintr-un bol negru"},
    {"stem": "cat4-pizza", "moment": "movie night", "name": "PIZZA",
     "line": "Blatul îl faci tu, topping-ul îl alegi tot tu.", "cta": "Vezi categoria",
     "url": "{{CATEGORY_URL_4}}", "utm": "cat_pizza", "ph": PINK, "ph_sub": "pizza mici",
     "alt": "Pizza mici de casă, fiecare cu alt topping"},
    {"stem": "cat5-post", "moment": "vegan / de post", "name": "DE POST",
     "line": "Vegan Classic Pankees, pentru zilele de post.", "cta": "Vezi produsul",
     "url": "{{CATEGORY_URL_5}}", "utm": "cat_post", "ph": ORANGE, "ph_sub": "pancakes cu pară",
     "alt": "Pancakes de post cu felii de pară și scorțișoară"},
]
# Reviews (copy.md S3, quotes verbatim, Romanian quotation marks kept). No stars or dates per card.
REVIEWS = [
    {"quote": "„Am folosit amestecul pentru blat de pizza, Pizza Crust Mix, 500g și mi-au ieșit două pizza delicioase!”",
     "name": "Irina A.", "product": "Pizza Crust Mix"},
    {"quote": "„Clătitele ies foarte pufoase și gustoase. O adevărată plăcere să le faci și să le mănânci”",
     "name": "Andreea H.", "product": "Classic Pankees"},
    {"quote": "„Bun. Rețeta este foarte bună”", "name": "Liliana F.", "product": "Brownie Mix"},
]

BIG_PHOTO = 238          # displayed px (export 2x), big card (Pancakes & Crêpes)
SMALL_PHOTO = 232        # displayed px (export 2x), 2 x 2 grid

report = []


# ---------------------------------------------------------------- helpers (from browse-abandonment/email-01)
def font(size, bold=True):
    try:
        return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)
    except OSError:
        return ImageFont.load_default(size=size)


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


# ---------------------------------------------------------------- torn edge (new transition)
def torn_points(width, base, amp, seed, step=14):
    """Ragged polyline across `width`: small random jitter plus a few deeper notches,
    like the torn pink band of the 'stripes' logo. Deterministic (seeded)."""
    rnd = random.Random(seed)
    pts, x = [], 0
    while x <= width + step:
        dy = rnd.uniform(-amp, amp)
        if rnd.random() < 0.12:
            dy += rnd.choice((-1, 1)) * amp * 1.6
        pts.append((x, base + dy))
        x += rnd.uniform(step * 0.5, step * 1.4)
    return pts


def torn_divider(name, top, accent, bottom, seed, h=28):
    """1200 x 2h (shown 600 x h). `top` colour above a torn edge, then a thin torn
    band of `accent` (the 'stripe' of the logo band), then `bottom` colour."""
    W, H = 1200, h * 2
    big_w, big_h = W * SS, H * SS
    img = Image.new("RGB", (big_w, big_h), top)
    d = ImageDraw.Draw(img)
    l1 = [(x * SS, y * SS) for x, y in torn_points(W, H * 0.38, 5, seed)]
    l2 = [(x * SS, y * SS) for x, y in torn_points(W, H * 0.62, 4, seed + 101)]
    d.polygon(l1 + [(big_w + 40, big_h + 40), (-40, big_h + 40)], fill=accent)
    d.polygon(l2 + [(big_w + 40, big_h + 40), (-40, big_h + 40)], fill=bottom)
    save_png(img.resize((W, H), Image.LANCZOS), ASSETS / name)


# ---------------------------------------------------------------- category photos: torn clipping
def placeholder_square(n, colour, label, sub):
    img = Image.new("RGB", (n, n), colour)
    d = ImageDraw.Draw(img)
    lw = max(3, n // 90)
    d.ellipse((n * 0.16, n * 0.30, n * 0.84, n * 0.98), fill=WHITE, outline=BLACK, width=lw)
    d.ellipse((n * 0.30, n * 0.44, n * 0.70, n * 0.84), fill=colour, outline=BLACK, width=lw)
    centered_text(d, (0, n * 0.04, n, n * 0.28), [(label, font(n // 9)), (sub, font(n // 18, False))])
    return img


def clipping(photo, n, seed):
    """Square photo n x n on white: rounded top corners, torn bottom edge."""
    inner = cover(photo, (n, n))
    N = n * SS
    m = Image.new("L", (N, N), 0)
    d = ImageDraw.Draw(m)
    r = int(n * 0.06) * SS
    edge = [(x * SS, y * SS) for x, y in torn_points(n, n * 0.955, n * 0.012, seed, step=max(8, n // 40))]
    d.polygon([(0, r), (0, 0), (N, 0), (N, r)] + [(N, edge[-1][1])] + edge[::-1], fill=255)
    # round the two top corners
    d.rectangle((0, 0, r, r), fill=0)
    d.rectangle((N - r, 0, N, r), fill=0)
    d.pieslice((0, 0, 2 * r, 2 * r), 180, 270, fill=255)
    d.pieslice((N - 2 * r, 0, N, 2 * r), 270, 360, fill=255)
    m = m.resize((n, n), Image.LANCZOS)
    out = Image.new("RGB", (n, n), WHITE)
    out.paste(inner, (0, 0), m)
    return out


def build_cat_photos():
    for i, c in enumerate(CATS):
        n = (BIG_PHOTO if i == 0 else SMALL_PHOTO) * 2
        p = find_input(c["stem"])
        photo = Image.open(p) if p else placeholder_square(1000, c["ph"], f"CAT{i + 1}", c["ph_sub"])
        save_jpg(clipping(photo, n, 7 + i * 13), ASSETS / f'{c["stem"]}.jpg', JPG_MAX_SMALL)
        report[-1] += f"  [{'real' if p else 'placeholder'}]"


# ---------------------------------------------------------------- small graphics
def star_poly(cx, cy, ro, ri):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = ro if i % 2 == 0 else ri
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return pts


def build_stars():
    """200 x 36 shown (400 x 72): five orange stars with black outline, on white."""
    W, H = 400, 72
    big = Image.new("RGB", (W * SS, H * SS), WHITE)
    d = ImageDraw.Draw(big)
    for k in range(5):
        cx = (40 + k * 80) * SS
        d.polygon(star_poly(cx, 38 * SS, 33 * SS, 14 * SS), fill=ORANGE, outline=BLACK, width=5 * SS)
    save_png(big.resize((W, H), Image.LANCZOS), ASSETS / "stars.png")


def build_quote_mark():
    """44 x 34 shown (88 x 68), transparent PNG: black opening quote (decorative)."""
    W, H = 88, 68
    big = Image.new("RGBA", (W * SS, H * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)
    for x0 in (4, 48):
        x0 *= SS
        d.ellipse((x0, 26 * SS, x0 + 36 * SS, 62 * SS), fill=BLACK)
        d.polygon([(x0 + 2 * SS, 44 * SS), (x0 + 30 * SS, 4 * SS), (x0 + 36 * SS, 10 * SS), (x0 + 22 * SS, 34 * SS)],
                  fill=BLACK)
    save_png(big.resize((W, H), Image.LANCZOS), ASSETS / "quote.png")


def build_usp_icons():
    """64 x 64 shown (128 exported): white circle, black 3px ring, black pictogram.
    New set: measuring jug (mix), shop with awning (stores), house with heart (delivery)."""
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

    # measuring jug with a heap of mix on top
    img, d = base()
    d.polygon([(40 * u, 46 * u), (82 * u, 46 * u), (78 * u, 98 * u), (44 * u, 98 * u)], outline=BLACK, width=lw)
    d.arc((72 * u, 54 * u, 100 * u, 84 * u), 270, 90, fill=BLACK, width=lw)
    for y in (62, 74, 86):
        d.line([(46 * u, y * u), (58 * u, y * u)], fill=BLACK, width=int(lw * 0.7))
    d.chord((42 * u, 30 * u, 80 * u, 62 * u), 180, 360, fill=BLACK)
    done(img, "usp-mix.png")
    # shop with striped awning
    img, d = base()
    d.rectangle((36 * u, 56 * u, 92 * u, 96 * u), outline=BLACK, width=lw)
    d.rectangle((56 * u, 70 * u, 72 * u, 96 * u), fill=BLACK)
    d.polygon([(32 * u, 56 * u), (40 * u, 34 * u), (88 * u, 34 * u), (96 * u, 56 * u)], fill=WHITE, outline=BLACK,
              width=lw)
    for x in (52, 64, 76):
        d.line([(x * u, 34 * u), ((x + (x - 64) * 0.35) * u, 56 * u)], fill=BLACK, width=lw)
    done(img, "usp-magazin.png")
    # house with a heart (delivered home)
    img, d = base()
    d.polygon([(64 * u, 28 * u), (98 * u, 58 * u), (90 * u, 58 * u), (90 * u, 98 * u), (38 * u, 98 * u),
               (38 * u, 58 * u), (30 * u, 58 * u)], outline=BLACK, width=lw)
    hx, hy, hr = 64 * u, 74 * u, 8 * u
    d.ellipse((hx - 2 * hr, hy - hr, hx, hy + hr), fill=BLACK)
    d.ellipse((hx, hy - hr, hx + 2 * hr, hy + hr), fill=BLACK)
    d.polygon([(hx - 2 * hr + 1 * u, hy + 2 * u), (hx + 2 * hr - 1 * u, hy + 2 * u), (hx, hy + 2.6 * hr)], fill=BLACK)
    done(img, "usp-acasa.png")


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


# ---------------------------------------------------------------- HTML helpers
AK = "Akrobat,'Arial Narrow',Arial,sans-serif"
AR = "Arial,Helvetica,sans-serif"


def e(s):
    return html.escape(s, quote=False)


def nb(s):
    """Escaped text with a non-breaking space before the last word (no one-word orphan line)."""
    words = [f'<span style="white-space:nowrap;">{e(w)}</span>' if "-" in w else e(w) for w in s.split(" ")]
    if len(words) < 2:
        return "".join(words)
    return " ".join(words[:-2] + [words[-2] + "&nbsp;" + words[-1]])


def link(href, utm_content):
    return f"{href}?{UTM}&amp;utm_content={utm_content}"


def button(href, label, utm_content, width=280, height=56, kind="fill-orange", fs=18, cls="btn-m"):
    """Bulletproof pill. kind: 'fill-orange' (orange pill, black text: only on black),
    'outline' (white pill, black 2px border, black text)."""
    url = link(href, utm_content)
    r = height // 2
    if kind == "outline":
        vml = (f'<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" '
               f'href="{url}" style="height:{height}px;v-text-anchor:middle;width:{width}px;" arcsize="50%" '
               f'strokecolor="#000000" strokeweight="2px" fillcolor="#FFFFFF">')
        a = (f'<a href="{url}" target="_blank" class="tb {cls}" style="background-color:#FFFFFF;border:2px solid #000000;'
             f'border-radius:{r}px;color:#000000;display:inline-block;font-family:{AR};'
             f'font-size:{fs}px;font-weight:bold;line-height:{height - 4}px;text-align:center;text-decoration:none;'
             f'width:{width - 4}px;max-width:100%;-webkit-text-size-adjust:none;">{e(label)}</a>')
    else:
        vml = (f'<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" '
               f'href="{url}" style="height:{height}px;v-text-anchor:middle;width:{width}px;" arcsize="50%" '
               f'stroke="f" fillcolor="#FAA61A">')
        a = (f'<a href="{url}" target="_blank" class="tb {cls}" style="background-color:#FAA61A;border-radius:{r}px;'
             f'color:#000000;display:inline-block;font-family:{AR};font-size:{fs}px;'
             f'font-weight:bold;line-height:{height}px;text-align:center;text-decoration:none;width:{width}px;'
             f'max-width:100%;-webkit-text-size-adjust:none;">{e(label)}</a>')
    return (f'<div>\n        <!--[if mso]>\n        {vml}\n          <w:anchorlock/><center style="color:#000000;'
            f'font-family:{AR};font-size:{fs}px;font-weight:bold;">{e(label)}</center>\n'
            f'        </v:roundrect>\n        <![endif]-->\n        <!--[if !mso]><!-- -->{a}<!--<![endif]-->\n      </div>')


def torn(name, bottom_colour):
    return f'''  <tr>
    <td bgcolor="{bottom_colour}" style="background-color:{bottom_colour};font-size:0;line-height:0;">
      <img src="assets/{name}" width="600" height="28" alt="" class="fluid" style="display:block;width:600px;max-width:100%;height:auto;border:0;">
    </td>
  </tr>'''


def chip(text):
    """Black pill with orange text (orange text only on black)."""
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="left" class="chip" '
            f'style="border-collapse:separate;margin:0 0 10px 0;"><tr><td class="to" bgcolor="#000000" '
            f'style="background-color:#000000;border-radius:12px;padding:4px 10px;font-family:{AK};font-size:14px;'
            f'line-height:16px;font-weight:bold;letter-spacing:0.5px;color:#FAA61A;white-space:nowrap;">{e(text)}</td></tr></table>'
            f'<div style="clear:both;font-size:0;line-height:0;">&nbsp;</div>')


def cat_name(name):
    # PANCAKES & CRÊPES may break only after „&” (copy.md S4 notes)
    if " & " not in name:
        return e(name)
    left, right = name.split(" & ", 1)
    return (f'<span style="white-space:nowrap;">{e(left)}&nbsp;&amp;</span> '
            f'<span style="white-space:nowrap;">{e(right)}</span>')


def big_card(c):
    url = link(c["url"], c["utm"])
    n = BIG_PHOTO
    return f'''  <!-- CARD 1 (mare): {e(c["name"])} -->
  <tr>
    <td class="px" align="center" bgcolor="#86D2DA" style="background-color:#86D2DA;padding:0 40px 12px 40px;">
      <table role="presentation" class="inner" width="520" cellpadding="0" cellspacing="0" border="0" style="width:520px;border-collapse:separate;border-spacing:0;">
        <tr><td bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:3px solid #000000;border-radius:20px;font-size:0;text-align:left;">
          <!--[if mso]><table role="presentation" width="514" cellpadding="0" cellspacing="0" border="0"><tr><td width="262" valign="middle"><![endif]-->
          <div class="bc-col bc-img" style="display:inline-block;width:100%;max-width:262px;vertical-align:middle;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="bc-ip" style="padding:12px 12px 12px 12px;">
              <a href="{url}" target="_blank" style="display:block;"><img src="assets/{c["stem"]}.jpg" width="{n}" height="{n}" alt="{e(c["alt"])}" class="bc-photo" style="display:block;width:{n}px;height:{n}px;border:0;margin:0 auto;font-family:{AR};font-size:14px;color:#000000;"></a>
            </td></tr></table>
          </div><!--[if mso]></td><td width="252" valign="middle"><![endif]--><div class="bc-col" style="display:inline-block;width:100%;max-width:252px;vertical-align:middle;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="bc-tx" style="padding:12px 12px 16px 8px;text-align:left;">
              {chip(c["moment"])}
              <h3 class="tb bc-name" style="margin:0 0 8px 0;font-family:{AK};font-size:28px;line-height:30px;font-weight:bold;letter-spacing:0.5px;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;"><a href="{url}" target="_blank" class="tb" style="color:#000000;text-decoration:none;">{cat_name(c["name"])}</a></h3>
              <p class="tb" style="margin:0 0 18px 0;font-family:{AR};font-size:16px;line-height:24px;color:#000000;"><a href="{url}" target="_blank" class="tb" style="color:#000000;text-decoration:none;">{nb(c["line"])}</a></p>
              <table role="presentation" cellpadding="0" cellspacing="0" border="0" align="left" class="bc-btn"><tr><td>
      {button(c["url"], c["cta"], c["utm"], width=180, height=44, kind="outline", fs=16, cls="btn-s")}
              </td></tr></table>
            </td></tr></table>
          </div>
          <!--[if mso]></td></tr></table><![endif]-->
        </td></tr>
      </table>
    </td>
  </tr>'''


def small_card(c):
    url = link(c["url"], c["utm"])
    n = SMALL_PHOTO
    return f'''<td class="sc" width="232" valign="top" bgcolor="#FFFFFF" style="width:232px;background-color:#FFFFFF;border:3px solid #000000;border-radius:18px;padding:8px 8px 16px 8px;text-align:left;">
            <!-- CARD: {e(c["name"])} -->
            <a href="{url}" target="_blank" style="display:block;"><img src="assets/{c["stem"]}.jpg" width="{n}" height="{n}" alt="{e(c["alt"])}" class="sc-photo" style="display:block;width:{n}px;height:{n}px;border:0;font-family:{AR};font-size:13px;color:#000000;"></a>
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="sc-tx" style="padding:10px 6px 0 6px;">
              {chip(c["moment"])}
              <h3 class="tb sc-name" style="margin:0 0 6px 0;font-family:{AK};font-size:26px;line-height:28px;font-weight:bold;letter-spacing:0.5px;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;"><a href="{url}" target="_blank" class="tb" style="color:#000000;text-decoration:none;">{cat_name(c["name"])}</a></h3>
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="tb sc-line" valign="top" height="44" style="height:44px;font-family:{AR};font-size:14px;line-height:20px;color:#000000;padding:0 0 12px 0;"><a href="{url}" target="_blank" class="tb" style="color:#000000;text-decoration:none;">{nb(c["line"])}</a></td></tr></table>
              {button(c["url"], c["cta"], c["utm"], width=160, height=40, kind="outline", fs=15, cls="btn-s")}
            </td></tr></table>
          </td>'''


def small_rows():
    rows = []
    for a, b in ((CATS[1], CATS[2]), (CATS[3], CATS[4])):
        rows.append(f'''  <tr>
    <td class="px" align="center" bgcolor="#86D2DA" style="background-color:#86D2DA;padding:0 40px 12px 40px;">
      <table role="presentation" class="inner" width="520" cellpadding="0" cellspacing="0" border="0" style="width:520px;border-collapse:separate;border-spacing:0;table-layout:fixed;">
        <tr>
          {small_card(a)}
          <td class="gut" width="12" style="width:12px;font-size:0;line-height:0;">&nbsp;</td>
          {small_card(b)}
        </tr>
      </table>
    </td>
  </tr>''')
    return "\n".join(rows)


def review_card(rv, bg, big=False, short=False):
    if big:
        q = f'font-family:{AR};font-size:19px;line-height:28px;'
    elif short:
        q = f'font-family:{AR};font-size:24px;line-height:32px;font-weight:bold;'
    else:
        q = f'font-family:{AR};font-size:16px;line-height:24px;'
    qcls = "q-short" if short else ""
    return f'''<img src="assets/quote.png" width="44" height="34" alt="" style="display:block;width:44px;height:34px;border:0;margin:0 0 12px 0;">
            <p class="tb {qcls}" style="margin:0 0 16px 0;{q}color:#000000;">{e(rv["quote"])}</p>
            <p class="tb" style="margin:0;font-family:{AK};font-size:22px;line-height:24px;font-weight:bold;color:#000000;">{e(rv["name"])}</p>
            <p class="tb" style="margin:0;font-family:{AR};font-size:14px;line-height:20px;color:#000000;">{e(rv["product"])}</p>'''


def usp_col(icon, title, line):
    return f'''<div class="usp" style="display:inline-block;width:100%;max-width:193px;vertical-align:top;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
          <tr><td align="center" style="padding:0 6px 24px 6px;">
            <img src="assets/{icon}" width="64" height="64" alt="" style="display:block;width:64px;height:64px;border:0;margin:0 auto 14px auto;">
            <p class="tb usp-t" style="margin:0 0 6px 0;font-family:{AK};font-size:18px;line-height:22px;font-weight:bold;letter-spacing:0.3px;text-transform:uppercase;white-space:nowrap;color:#000000;mso-line-height-rule:exactly;">{e(title)}</p>
            <p class="tb" style="margin:0;font-family:{AR};font-size:14px;line-height:20px;color:#000000;">{nb(line)}</p>
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
<!-- GENERATED by build.py: edit COPY / CATS / REVIEWS in build.py (texts from copy.md), not this file. -->
${esp_header}<!--[if mso]>
<noscript><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript>
<style>td,th,div,p,a,h1,h2,h3{font-family:Arial,Helvetica,sans-serif;}
.usp-t{font-size:14px!important;letter-spacing:0!important;}</style>
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
    .btn-s{display:block!important;width:auto!important;font-size:14px!important;}
    .h-hero{font-size:48px!important;line-height:46px!important;}
    .h-xl{font-size:32px!important;line-height:32px!important;}
    .bc-col{display:block!important;max-width:100%!important;width:100%!important;}
    .bc-ip{padding:10px 10px 0 10px!important;}
    .bc-photo{width:100%!important;max-width:309px!important;height:auto!important;}
    .bc-tx{padding:14px 16px 18px 16px!important;}
    .bc-name{font-size:28px!important;line-height:28px!important;}
    .bc-btn{float:none!important;width:100%!important;}
    .sc{width:auto!important;padding:6px 6px 12px 6px!important;}
    .gut{width:8px!important;}
    .sc-photo{width:100%!important;height:auto!important;}
    .sc-tx{padding:8px 2px 0 2px!important;}
    .sc-name{font-size:21px!important;line-height:22px!important;}
    .sc-line{font-size:13px!important;line-height:18px!important;height:38px!important;}
    .chip td{font-size:12px!important;padding:3px 8px!important;}
    .stack{display:block!important;width:100%!important;max-width:100%!important;box-sizing:border-box;}
    .stack-gap{display:block!important;width:100%!important;height:12px!important;}
    .rv-pad{padding:20px 20px 22px 20px!important;}
    .q-short{font-size:22px!important;line-height:30px!important;}
    .rating{font-size:84px!important;line-height:80px!important;}
    .usp{max-width:300px!important;display:block!important;margin:0 auto!important;}
  }
  [data-ogsc] .tb{color:#000000!important;}
  [data-ogsc] .to{color:#FAA61A!important;}
  [data-ogsc] .tw{color:#FFFFFF!important;}
</style>
</head>
<body id="body" style="margin:0;padding:0;background-color:#FFFFFF;">

<!-- Preheader (subiect A recomandat: „${title}”) -->
<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">${preheader}${pad}</div>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" style="background-color:#FFFFFF;">
<tr><td align="center" valign="top">

<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td><![endif]-->
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" align="center" style="width:600px;max-width:600px;">

  <!-- ============ S0 LOGO (black: full logo, white outline visible) ============ -->
  <tr>
    <td align="center" bgcolor="#000000" style="background-color:#000000;padding:32px 20px 18px 20px;">
      <a href="https://lucasbites.ro" target="_blank" style="display:inline-block;"><img src="assets/logo.png" width="180" height="${logo_h}" alt="${alt_logo}" style="display:block;width:180px;height:auto;border:0;font-family:Arial,Helvetica,sans-serif;font-size:20px;font-weight:bold;color:#FAA61A;"></a>
    </td>
  </tr>

  <!-- ============ S1 HERO (black, text only, no button) ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#000000" style="background-color:#000000;padding:6px 40px 30px 40px;text-align:center;">
      ${esp_greeting}<p class="to" style="margin:0 0 10px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:22px;line-height:26px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:#FAA61A;">${greeting}</p>
      <h1 class="to h-hero" style="margin:0 0 16px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:64px;line-height:60px;font-weight:900;text-transform:uppercase;color:#FAA61A;mso-line-height-rule:exactly;">${h1_l1}<br>${h1_l2}</h1>
      <p class="tw" style="margin:0 auto;max-width:430px;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#FFFFFF;">${intro}</p>
    </td>
  </tr>
${torn_black_turq}

  <!-- ============ S2 CATEGORIES (turquoise): 1 large card + 2 x 2 grid ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#86D2DA" style="background-color:#86D2DA;padding:14px 40px 24px 40px;text-align:center;">
      <p class="tb" style="margin:0 0 6px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:22px;line-height:26px;font-weight:bold;letter-spacing:1px;color:#000000;">${s2_eyebrow}</p>
      <h2 class="tb h-xl" style="margin:0 0 10px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:42px;line-height:42px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">${s2_h2}</h2>
      <p class="tb" style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#000000;">${s2_intro}</p>
    </td>
  </tr>
${big_card}
${small_rows}
  <tr>
    <td class="px" align="center" bgcolor="#86D2DA" style="background-color:#86D2DA;padding:20px 40px 30px 40px;">
      <a href="{{SHOP_URL}}?${utm}&amp;utm_content=cat_toate" target="_blank" class="tb ul" style="font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:22px;line-height:26px;font-weight:bold;letter-spacing:0.5px;color:#000000;text-decoration:underline;">${all_products}</a>
    </td>
  </tr>
${torn_turq_white}

  <!-- ============ S3 REVIEWS (white): rating + 1 wide orange card + pink and turquoise cards ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:18px 40px 22px 40px;text-align:center;">
      <h2 class="tb h-xl" style="margin:0 0 10px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:40px;line-height:40px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">${s3_title}</h2>
      <p class="tb" style="margin:0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;color:#000000;"><span class="rating" style="font-size:96px;line-height:88px;font-weight:900;">${rating}</span> <span style="font-size:32px;line-height:32px;font-weight:bold;">${rating_of}</span></p>
      <img src="assets/stars.png" width="200" height="36" alt="${alt_stars}" style="display:block;width:200px;height:36px;border:0;margin:8px auto 10px auto;font-family:Arial,Helvetica,sans-serif;font-size:14px;font-weight:bold;color:#000000;">
      <p class="tb" style="margin:0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:20px;line-height:24px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:#000000;">${rating_sub}</p>
    </td>
  </tr>
  <tr>
    <td class="px" align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:6px 40px 12px 40px;">
      <table role="presentation" class="inner" width="520" cellpadding="0" cellspacing="0" border="0" style="width:520px;border-collapse:separate;border-spacing:0;">
        <tr><td class="rv-pad" bgcolor="#FAA61A" style="background-color:#FAA61A;border:3px solid #000000;border-radius:20px;padding:24px 30px 26px 30px;text-align:left;">
            ${review_big}
        </td></tr>
      </table>
    </td>
  </tr>
  <tr>
    <td class="px" align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:0 40px 0 40px;">
      <table role="presentation" class="inner" width="520" cellpadding="0" cellspacing="0" border="0" style="width:520px;border-collapse:separate;border-spacing:0;">
        <tr>
          <td class="stack rv-pad" width="204" valign="top" bgcolor="#F7ACB4" style="width:204px;background-color:#F7ACB4;border:3px solid #000000;border-radius:20px;padding:22px 22px 24px 22px;text-align:left;">
            ${review_s1}
          </td>
          <td class="stack-gap" width="12" style="width:12px;font-size:0;line-height:0;">&nbsp;</td>
          <td class="stack rv-pad" width="204" valign="top" bgcolor="#86D2DA" style="width:204px;background-color:#86D2DA;border:3px solid #000000;border-radius:20px;padding:22px 22px 24px 22px;text-align:left;">
            ${review_s2}
          </td>
        </tr>
      </table>
    </td>
  </tr>
  <tr>
    <td class="px" align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:26px 40px 30px 40px;">
      <a href="{{REVIEWS_URL}}?${utm}&amp;utm_content=recenzii_toate" target="_blank" class="tb ul" style="font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:22px;line-height:26px;font-weight:bold;letter-spacing:0.5px;color:#000000;text-decoration:underline;">${all_reviews}</a>
    </td>
  </tr>
${torn_white_pink}

  <!-- ============ S4 USP (pink, 3 columns desktop, stacked mobile; titles on one line) ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#F7ACB4" style="background-color:#F7ACB4;padding:14px 40px 16px 40px;">
      <h2 class="tb h-xl" style="margin:0 0 26px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:36px;line-height:36px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">${usp_title}</h2>
    </td>
  </tr>
  <tr>
    <td align="center" bgcolor="#F7ACB4" style="background-color:#F7ACB4;padding:0 10px 20px 10px;font-size:0;text-align:center;">
<!--[if mso]><table role="presentation" width="579" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td width="193" valign="top"><![endif]-->
      ${usp1}<!--[if mso]></td><td width="193" valign="top"><![endif]-->${usp2}<!--[if mso]></td><td width="193" valign="top"><![endif]-->${usp3}
<!--[if mso]></td></tr></table><![endif]-->
    </td>
  </tr>
${torn_pink_black}

  <!-- ============ S5 CLOSING (black): title, line, button, signature + Professional row ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#000000" style="background-color:#000000;padding:20px 40px 28px 40px;text-align:center;">
      <h2 class="to h-xl" style="margin:0 0 12px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:42px;line-height:42px;font-weight:900;text-transform:uppercase;color:#FAA61A;mso-line-height-rule:exactly;">${s5_title}</h2>
      <p class="tw" style="margin:0 auto 24px auto;max-width:420px;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#FFFFFF;">${s5_line}</p>
      ${cta_shop}
      <p class="to" style="margin:22px 0 0 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:30px;line-height:32px;font-weight:bold;color:#FAA61A;">${signature}</p>
    </td>
  </tr>
  <tr>
    <td class="px" align="center" bgcolor="#000000" style="background-color:#000000;padding:0 60px 34px 60px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-top:1px solid #FFFFFF;font-size:0;line-height:0;height:1px;">&nbsp;</td></tr></table>
      <p class="tw" style="margin:22px 0 8px 0;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:21px;color:#FFFFFF;">${pro_line}</p>
      <a href="{{PROFESSIONAL_URL}}?${utm}&amp;utm_content=professional" target="_blank" class="tw ul" style="font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:21px;font-weight:bold;color:#FFFFFF;text-decoration:underline;">${pro_link}</a>
    </td>
  </tr>
${torn_black_white}

  <!-- ============ S6 FOOTER (same structure as browse / checkout) ============ -->
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

ESP_HEADER = '''<!-- ESP-MARKER (theMarketer), de facut manual de Andreea:
  1. {{FIRST_NAME}}: inlocuieste cu tag-ul theMarketer + conditie: „Hei!” daca lipseste sau are peste 19 caractere.
  2. {{CATEGORY_URL_1..5}}, {{SHOP_URL}}, {{REVIEWS_URL}}, {{PROFESSIONAL_URL}}: linkurile reale; UTM-urile sunt deja puse (utm_campaign=website_01).
     {{CATEGORY_URL_5}} = pagina produsului Vegan Classic Pankees (cardul 5 e produs, nu categorie).
  3. {{UNSUBSCRIBE_URL}}: tag-ul de dezabonare theMarketer; List-Unsubscribe one-click activ.
  4. Footer: fraza „de ce primesti” [DE CONFIRMAT CU ANDREEA]; SRL + CUI [DE PRIMIT DE LA CLIENT].
  5. assets/ -> URL-uri absolute HTTPS (imagini + fonturi) la upload.
  Fara feed dinamic de produse in acest email. -->
'''


def build_html(logo_h, stripes_h):
    pad = "&#847;&zwnj;&nbsp;" * 40
    common = {k: e(v) for k, v in COPY.items() if isinstance(v, str)}
    for k in ("intro", "s2_intro", "s5_line", "footer_why", "pro_line"):
        common[k] = nb(COPY[k])
    common.update(
        pad=pad, utm=UTM, logo_h=logo_h, stripes_h=stripes_h,
        s5_title=f'{e(COPY["s5_title_l1"])}<br>{e(COPY["s5_title_l2"])}',
        cta_shop=button("{{SHOP_URL}}", COPY["cta_shop"], "cta_shop"),
        big_card=big_card(CATS[0]),
        small_rows=small_rows(),
        review_big=review_card(REVIEWS[0], ORANGE, big=True),
        review_s1=review_card(REVIEWS[1], PINK),
        review_s2=review_card(REVIEWS[2], TURQ, short=True),
        usp1=usp_col("usp-mix.png", *COPY["usp"][0]),
        usp2=usp_col("usp-magazin.png", *COPY["usp"][1]),
        usp3=usp_col("usp-acasa.png", *COPY["usp"][2]),
        torn_black_turq=torn("torn-black-turq.png", "#86D2DA"),
        torn_turq_white=torn("torn-turq-white.png", "#FFFFFF"),
        torn_white_pink=torn("torn-white-pink.png", "#F7ACB4"),
        torn_pink_black=torn("torn-pink-black.png", "#000000"),
        torn_black_white=torn("torn-black-white.png", "#FFFFFF"),
    )
    greet_note = ('<!-- ESP-MARKER: salut conditionat in theMarketer, fallback „Hei!” '
                  '(FIRST_NAME gol sau peste 19 caractere) -->\n      ')
    for name, esp in (("index.html", False), ("index-esp.html", True)):
        out = HTML.substitute(common, esp_header=ESP_HEADER if esp else "",
                              esp_greeting=greet_note if esp else
                              "<!-- Greeting: fallback „Hei!” when FIRST_NAME is empty or longer than 19 characters (copy.md S1) -->\n      ")
        (HERE / name).write_text(out, encoding="utf-8")
        kb = len(out.encode("utf-8")) / 1024
        report.append(f"{name}  {kb:.1f}KB" + ("  !! over 102 KB (Gmail clipping)" if kb > 102 else ""))


# ---------------------------------------------------------------- previews (optional, headless Chrome)
def trim_bottom(img):
    rgb = img.convert("RGB")
    bbox = ImageChops.difference(rgb, Image.new("RGB", rgb.size, WHITE)).getbbox()
    return rgb.crop((0, 0, rgb.width, min(rgb.height, bbox[3] + 40))) if bbox else rgb


def build_previews():
    if not Path(CHROME).exists():
        print(f"Preview skipped: Chrome not found at {CHROME}")
        return
    # Headless Chrome enforces a minimum window width (~500px), so the email is rendered
    # inside an iframe of the exact width (its own viewport, media queries apply).
    with tempfile.TemporaryDirectory() as tmp:
        for w, out in ((600, "preview.png"), (375, "preview-mobile.png")):
            shot = Path(tmp) / out
            frame = Path(tmp) / f"frame-{w}.html"
            frame.write_text(f'<!DOCTYPE html><html><body style="margin:0;background:#FFFFFF;">'
                             f'<iframe src="{(HERE / "index.html").as_uri()}" width="{w}" height="8000" '
                             f'style="border:0;display:block;"></iframe></body></html>', encoding="utf-8")
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                            "--allow-file-access-from-files",
                            f"--window-size={max(w, 800)},8000", f"--screenshot={shot}", frame.as_uri()],
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
    torn_divider("torn-black-turq.png", BLACK, PINK, TURQ, 11)
    torn_divider("torn-turq-white.png", TURQ, ORANGE, WHITE, 23)
    torn_divider("torn-white-pink.png", WHITE, TURQ, PINK, 37)
    torn_divider("torn-pink-black.png", PINK, ORANGE, BLACK, 41)
    torn_divider("torn-black-white.png", BLACK, TURQ, WHITE, 53)
    build_cat_photos()
    build_stars()
    build_quote_mark()
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
