#!/usr/bin/env python3
"""Lucas Bites, Website Abandoned Email 2: asset + HTML builder.

Usage:
  .venv/bin/python build.py              build assets/, index.html, index-esp.html, Figma copies
  .venv/bin/python build.py --preview    same, then preview.png (600px) and preview-mobile.png (375px)
                                         with headless Google Chrome (macOS path, see CHROME below)

Needs Pillow only (no network). If Pillow is missing:
  python3 -m venv .venv && .venv/bin/pip install Pillow && .venv/bin/python build.py

- Photos dropped into images/ (names from image-prompts.md, .png/.jpg/.jpeg) are cropped
  square and framed as "torn recipe clippings" (same treatment as Email 1).
- Missing photos get a placeholder at the final size and final file name.
- Texts come from copy.md (Copywriter), verbatim, in COPY / RECIPES below.
- Seasonal swap (1 Nov - 31 Dec): set SEASON = True (card 1 becomes Gingerbread Pancakes,
  texts from copy.md section 3) and rebuild; or edit card 1 by hand in theMarketer
  (see design-direction.md, section 6).
- index.html     = preview, 3 EXEMPLU product cards in the recommendations block.
  index-esp.html = theMarketer version: [RECOMANDĂRI PRODUSE THEMARKETER] between
                   THEMARKETER_FEED START/END; whole S3 section between
                   THEMARKETER_SECTION_S3 START/END so Andreea can hide it.

Helpers (save_jpg/png, find_input, cover, torn edge, clipping, button, chip, logos, fonts,
previews) are copied from ../email-01/build.py (not importable: its paths point to its folder).

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
ROOT = HERE.parents[4]
EMAILS = HERE.parents[1]
IMAGES = HERE / "images"
ASSETS = HERE / "assets"
LOGO_DIR = ROOT / "Logo"
FONTS_SRC = EMAILS / "welcome-02" / "assets" / "fonts"
ICONS_SRC = EMAILS / "welcome-03" / "assets"
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

UTM = "utm_source=email&amp;utm_medium=flow&amp;utm_campaign=website_02"

SEASON = "--sezon" in sys.argv     # build the Gingerbread variant of card 1 (manual seasonal swap)

# ---------------------------------------------------------------- COPY (verbatim from copy.md)
COPY = {
    "title": "Din mix, direct în farfurie",
    "preheader": "Două rețete de făcut acasă și câteva mixuri care merită încercate.",
    "greeting": "Hei, {{FIRST_NAME}}!",
    "h1_l1": "HAI ÎN",
    "h1_l2": "BUCĂTĂRIE!",
    "intro": "Două rețete cu mixurile noastre și câteva sugestii de la noi, pentru când ai poftă.",
    "s2_eyebrow": "din mix, în farfurie",
    "s2_h2": "PUNE MIXUL LA TREABĂ",
    "s2_intro": "Fiecare rețetă are mixul ei. Tu alegi cu care începi.",
    "all_recipes": "Mai multe rețete",
    "s3_chip": "MERITĂ ÎNCERCATE",
    "s3_h2": "S-AR PUTEA SĂ-ȚI PLACĂ",
    "s3_intro": "Câteva mixuri din gamă, fiecare cu pofta lui.",
    "cta_rec": "Vezi și alte mixuri",
    "s3_fb_line": "Toată gama e aici, fiecare mix cu pagina lui.",
    "s3_fb_cta": "Vezi gama completă",
    "usp_title": "PE SCURT",
    "usp": [("SIMPLU DE FĂCUT", "Oricine le poate face, fără bătaie de cap."),
            ("LE RECUNOȘTI", "Ingredientele din mix, fără conservanți."),
            ("TRANSPORT GRATUIT", "Alegi două mixuri? Livrarea nu costă nimic.")],
    "s5_title_l1": "CÂND AI CHEF,",
    "s5_title_l2": "NOI SUNTEM AICI.",
    "s5_line": "De la pancakes la pizza, alege ce-ți face poftă azi.",
    "cta_shop": "Hai în magazin",
    "signature": "eat what you love",
    "alt_logo": "Lucas Bites",
    "alt_footer_logo": "Lucas Bites, eat what you love",
    "footer_why": "Primești acest email pentru că ai acceptat să primești emailuri de la Lucas Bites.",
    "footer_unsub_pre": "Nu mai vrei emailuri de la noi?",
    "footer_unsub_link": "Dezabonează-te aici",
    "footer_unsub_post": "Durează un click.",
}
# Recipe cards (copy.md S2). Same structure on both, so the seasonal swap is text + image only.
RECIPES = [
    {"stem": "reteta1-clatite", "moment": "duminica fără grabă", "t1": "CLĂTITE PENTRU", "t2": "TOATĂ FAMILIA",
     "product": "Cu Crêpes Traditional", "info": "Familie · 10 min", "cta": "Vezi rețeta",
     "url": "{{URL_RETETA_CLATITE}}", "utm": "reteta_1", "ph": PINK, "ph_sub": "clătite plic",
     "alt": "Clătite de casă pentru toată familia"},
    {"stem": "reteta2-cookies", "moment": "gustarea de după școală", "t1": "COOKIES CU", "t2": "CIOCOLATĂ NEAGRĂ",
     "product": "Cu Cookie Mix", "info": "Desert · 14 min", "cta": "Vezi rețeta",
     "url": "{{URL_RETETA_COOKIES}}", "utm": "reteta_2", "ph": TURQ, "ph_sub": "cookies întregi",
     "alt": "Cookies întregi cu bucăți mari de ciocolată neagră"},
]
GINGERBREAD = {"stem": "sezon-gingerbread", "moment": "Sărbătorile de iarnă", "t1": "GINGERBREAD", "t2": "PANCAKES",
               "product": "Cu Classic Pankees", "info": "Desert · 15 min", "cta": "Vezi rețeta",
               "url": "{{URL_RETETA_GINGERBREAD}}", "utm": "reteta_1", "ph": ORANGE, "ph_sub": "gingerbread pancakes",
               "alt": "Teanc de gingerbread pancakes"}
if SEASON:
    RECIPES[0] = GINGERBREAD

PHOTO = 238          # recipe photo, displayed px (export 2x)
PROD_IMG = 140       # EXEMPLU product image in the preview grid

report = []


# ---------------------------------------------------------------- helpers (from ../email-01/build.py)
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



# ---------------------------------------------------------------- new for Email 2
def build_recipe_photos():
    items = RECIPES + ([] if SEASON else [GINGERBREAD])
    for i, c in enumerate(items):
        n = PHOTO * 2
        p = find_input(c["stem"])
        photo = Image.open(p) if p else placeholder_square(1000, c["ph"], f"REȚETA {i + 1}" if i < 2 else "SEZON",
                                                           c["ph_sub"])
        save_jpg(clipping(photo, n, 5 + i * 17), ASSETS / f'{c["stem"]}.jpg', JPG_MAX_SMALL)
        report[-1] += f"  [{'real' if p else 'placeholder'}]"


def build_example_product():
    """EXEMPLU product image (preview only): turquoise square, white plate, label."""
    n = PROD_IMG * 2
    img = Image.new("RGB", (n, n), TURQ)
    d = ImageDraw.Draw(img)
    d.ellipse((n * 0.2, n * 0.28, n * 0.8, n * 0.88), fill=WHITE, outline=BLACK, width=4)
    centered_text(d, (0, n * 0.04, n, n * 0.26), [("EXEMPLU", font(n // 9)), ("imagine din feed", font(n // 16, False))])
    save_jpg(img, ASSETS / "exemplu-produs.jpg", 40_000)


def build_mini_stars():
    """90 x 16 shown (180 x 32): placeholder for the feed rating, black outline, no fill."""
    W, H = 180, 32
    big = Image.new("RGB", (W * SS, H * SS), WHITE)
    d = ImageDraw.Draw(big)
    for k in range(5):
        cx = (18 + k * 36) * SS
        d.polygon(star_poly(cx, 17 * SS, 15 * SS, 6.5 * SS), fill=ORANGE if k < 4 else WHITE, outline=BLACK, width=3 * SS)
    save_png(big.resize((W, H), Image.LANCZOS), ASSETS / "stele-exemplu.png")


def build_usp_icons():
    """64 x 64 shown (128): white circle, black ring. New set: spatula (simplu),
    magnifier (le recunoști), two paper bags (două mixuri, transport)."""
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

    img, d = base()   # spatula, diagonal
    d.rounded_rectangle((52 * u, 26 * u, 80 * u, 62 * u), radius=6 * u, outline=BLACK, width=lw)
    for x in (61, 71):
        d.line([(x * u, 34 * u), (x * u, 54 * u)], fill=BLACK, width=int(lw * 0.7))
    d.line([(66 * u, 62 * u), (66 * u, 102 * u)], fill=BLACK, width=int(lw * 1.4))
    done(img.rotate(-30, resample=Image.BICUBIC, center=(N / 2, N / 2)), "usp-spatula.png")

    img, d = base()   # magnifier
    d.ellipse((34 * u, 32 * u, 76 * u, 74 * u), outline=BLACK, width=lw)
    d.line([(72 * u, 70 * u), (94 * u, 92 * u)], fill=BLACK, width=int(lw * 1.6))
    d.arc((42 * u, 40 * u, 68 * u, 66 * u), 200, 260, fill=BLACK, width=int(lw * 0.6))
    done(img, "usp-lupa.png")

    img, d = base()   # two paper bags
    for x0, y0 in ((32, 50), (62, 42)):
        d.rectangle((x0 * u, y0 * u, (x0 + 32) * u, 96 * u), fill=WHITE, outline=BLACK, width=lw)
        d.arc(((x0 + 8) * u, (y0 - 12) * u, (x0 + 24) * u, (y0 + 8) * u), 180, 360, fill=BLACK, width=int(lw * 0.8))
    done(img, "usp-pungi.png")


def recipe_title(c):
    return (f'<span style="white-space:nowrap;">{e(c["t1"])}</span><br>'
            f'<span style="white-space:nowrap;">{e(c["t2"])}</span>')


def recipe_card(c, idx, photo_right=False):
    """Horizontal 'fișă de rețetă': photo 238 + text 252, alternating sides on desktop
    (dir=rtl trick), photo always on top on mobile."""
    url = link(c["url"], c["utm"])
    n = PHOTO
    dir_outer = ' dir="rtl"' if photo_right else ""
    dir_in = ' dir="ltr"'
    return f'''  <!-- CARD_RETETA_{idx} START: {e(c["t1"])} {e(c["t2"])} (schimb de sezon: vezi design-direction.md, sectiunea 6) -->
  <tr>
    <td class="px" align="center" bgcolor="#FAA61A" style="background-color:#FAA61A;padding:0 40px 16px 40px;">
      <table role="presentation" class="inner" width="520" cellpadding="0" cellspacing="0" border="0" style="width:520px;border-collapse:separate;border-spacing:0;">
        <tr><td{dir_outer} bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:3px solid #000000;border-radius:20px;font-size:0;text-align:left;">
          <!--[if mso]><table role="presentation" width="514" cellpadding="0" cellspacing="0" border="0"{dir_outer}><tr><td width="262" valign="middle"><![endif]-->
          <div{dir_in} class="bc-col bc-img" style="display:inline-block;width:100%;max-width:262px;vertical-align:middle;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="bc-ip" style="padding:12px;">
              <a href="{url}" target="_blank" style="display:block;"><img src="assets/{c["stem"]}.jpg" width="{n}" height="{n}" alt="{e(c["alt"])}" class="bc-photo" style="display:block;width:{n}px;height:{n}px;border:0;margin:0 auto;font-family:{AR};font-size:14px;color:#000000;"></a>
            </td></tr></table>
          </div><!--[if mso]></td><td width="252" valign="middle"><![endif]--><div{dir_in} class="bc-col" style="display:inline-block;width:100%;max-width:252px;vertical-align:middle;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="bc-tx" style="padding:14px {"8px 16px 14px" if photo_right else "14px 16px 8px"};text-align:left;">
              {chip(c["moment"])}
              <h3 class="tb bc-name" style="margin:0 0 10px 0;font-family:{AK};font-size:28px;line-height:30px;font-weight:bold;letter-spacing:0.5px;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;"><a href="{url}" target="_blank" class="tb" style="color:#000000;text-decoration:none;">{recipe_title(c)}</a></h3>
              <p class="tb" style="margin:0 0 2px 0;font-family:{AR};font-size:16px;line-height:22px;font-weight:bold;color:#000000;"><a href="{url}" target="_blank" class="tb" style="color:#000000;text-decoration:none;">{e(c["product"])}</a></p>
              <p class="tb" style="margin:0 0 16px 0;font-family:{AR};font-size:15px;line-height:22px;color:#000000;"><a href="{url}" target="_blank" class="tb" style="color:#000000;text-decoration:none;">{e(c["info"])}</a></p>
              <table role="presentation" cellpadding="0" cellspacing="0" border="0" align="left" class="bc-btn"><tr><td>
      {button(c["url"], c["cta"], c["utm"], width=170, height=44, kind="outline", fs=16, cls="btn-s")}
              </td></tr></table>
            </td></tr></table>
          </div>
          <!--[if mso]></td></tr></table><![endif]-->
        </td></tr>
      </table>
    </td>
  </tr>
  <!-- CARD_RETETA_{idx} END -->'''


def example_product(k):
    return f'''<div class="pc" style="display:inline-block;width:100%;max-width:175px;vertical-align:top;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding:0 3px 12px 3px;">
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;"><tr>
            <td bgcolor="#FFFFFF" style="background-color:#FFFFFF;border:3px solid #000000;border-radius:16px;padding:8px 8px 14px 8px;text-align:center;">
              <a href="#exemplu-{k}" style="display:block;"><img src="assets/exemplu-produs.jpg" width="{PROD_IMG}" height="{PROD_IMG}" alt="Nume produs" class="pc-img" style="display:block;width:{PROD_IMG}px;max-width:100%;height:auto;border:0;margin:0 auto;"></a>
              <p class="tb" style="margin:10px 0 4px 0;font-family:{AK};font-size:20px;line-height:22px;font-weight:bold;text-transform:uppercase;color:#000000;">Nume produs</p>
              <img src="assets/stele-exemplu.png" width="90" height="16" alt="Rating (din feed)" style="display:block;width:90px;height:16px;border:0;margin:0 auto 6px auto;">
              <p class="tb" style="margin:0;font-family:{AR};font-size:16px;line-height:22px;font-weight:bold;color:#000000;">XX,XX lei</p>
            </td></tr></table>
        </td></tr></table>
      </div>'''


def feed_block(esp):
    if esp:
        inner = ('<!-- THEMARKETER_FEED START: latime utila 520px desktop (335px pe mobil 375); 3 produse pe un rand. '
                 'Imaginea, numele, pretul, ratingul si linkul le genereaza blocul; UTM mostenit din „UTM campanie” (utm_content=rec_feed). -->\n'
                 f'      <p class="tb" style="margin:0;font-family:{AR};font-size:16px;line-height:24px;font-weight:bold;color:#000000;">[RECOMANDĂRI PRODUSE THEMARKETER]</p>\n'
                 '      <!-- THEMARKETER_FEED END -->')
        return f'''  <tr>
    <td class="px" align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:0 40px 8px 40px;">
      {inner}
    </td>
  </tr>'''
    cards = "".join(example_product(k) for k in (1, 2, 3))
    return f'''  <!-- EXEMPLU (doar preview): in index-esp.html aici e blocul theMarketer -->
  <tr>
    <td align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:0 37px 8px 37px;font-size:0;text-align:center;">
<!--[if mso]><table role="presentation" width="526" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td width="175" valign="top"><![endif]-->
      {cards}
<!--[if mso]></td></tr></table><![endif]-->
    </td>
  </tr>'''


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


def measure_usp():
    """Check the one-line rule: title width vs 181px usable (193 column - 12 padding)."""
    cands = [("Akrobat Bold", ROOT / "Fonturi" / "Akrobat-Bold.ttf"),
             ("Arial Narrow Bold", Path("/System/Library/Fonts/Supplemental/Arial Narrow Bold.ttf")),
             ("Arial Bold", Path(FONT_BOLD))]
    for t, _ in COPY["usp"]:
        parts = []
        for name, p in cands:
            if p.exists():
                f = ImageFont.truetype(str(p), 18)
                w = ImageDraw.Draw(Image.new("L", (1, 1))).textlength(t, font=f) + 0.3 * (len(t) - 1)
                parts.append(f"{name} {w:.0f}px")
        report.append(f"USP „{t}”: " + ", ".join(parts) + " (util 181px)")


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
<!-- GENERATED by build.py: edit COPY / RECIPES in build.py (texts from copy.md), not this file. -->
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
    .pc{max-width:50%!important;}
    .bc-tx{padding:14px 16px 18px 16px!important;}
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

  <!-- ============ S0 LOGO (pink) ============ -->
  <tr>
    <td align="center" bgcolor="#F7ACB4" style="background-color:#F7ACB4;padding:32px 20px 18px 20px;">
      <a href="https://lucasbites.ro" target="_blank" style="display:inline-block;"><img src="assets/logo.png" width="180" height="${logo_h}" alt="${alt_logo}" style="display:block;width:180px;height:auto;border:0;font-family:Arial,Helvetica,sans-serif;font-size:20px;font-weight:bold;color:#000000;"></a>
    </td>
  </tr>

  <!-- ============ S1 HERO (pink, black text, no image, no button) ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#F7ACB4" style="background-color:#F7ACB4;padding:6px 40px 30px 40px;text-align:center;">
      ${esp_greeting}<p class="tb" style="margin:0 0 10px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:22px;line-height:26px;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:#000000;">${greeting}</p>
      <h1 class="tb h-hero" style="margin:0 0 16px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:64px;line-height:60px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">${h1_l1}<br>${h1_l2}</h1>
      <p class="tb" style="margin:0 auto;max-width:430px;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#000000;">${intro}</p>
    </td>
  </tr>
${torn_pink_orange}

  <!-- ============ S2 RECIPES (orange): 2 horizontal recipe cards, alternating ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#FAA61A" style="background-color:#FAA61A;padding:14px 40px 24px 40px;text-align:center;">
      <p class="tb" style="margin:0 0 6px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:22px;line-height:26px;font-weight:bold;letter-spacing:1px;color:#000000;">${s2_eyebrow}</p>
      <h2 class="tb h-xl" style="margin:0 0 10px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:42px;line-height:42px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">${s2_h2}</h2>
      <p class="tb" style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#000000;">${s2_intro}</p>
    </td>
  </tr>
${card1}
${card2}
  <tr>
    <td class="px" align="center" bgcolor="#FAA61A" style="background-color:#FAA61A;padding:14px 40px 30px 40px;">
      <a href="{{RECIPES_URL}}?${utm}&amp;utm_content=retete_toate" target="_blank" class="tb ul" style="font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:22px;line-height:26px;font-weight:bold;letter-spacing:0.5px;color:#000000;text-decoration:underline;">${all_recipes}</a>
    </td>
  </tr>
${torn_orange_white}

  <!-- THEMARKETER_SECTION_S3 START: toata sectiunea de recomandari (chip, titlu, intro, bloc, buton). Se ascunde intreaga daca blocul nu are rezultate. -->
  <!-- ============ S3 RECOMMENDATIONS (white) ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:20px 40px 22px 40px;text-align:center;">
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center" style="border-collapse:separate;margin:0 auto 12px auto;"><tr><td class="to" bgcolor="#000000" style="background-color:#000000;border-radius:14px;padding:5px 14px;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:16px;line-height:18px;font-weight:bold;letter-spacing:1px;color:#FAA61A;white-space:nowrap;">${s3_chip}</td></tr></table>
      <h2 class="tb h-xl" style="margin:0 0 10px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:42px;line-height:42px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;"><span style="white-space:nowrap;">S-AR PUTEA</span> <span style="white-space:nowrap;">SĂ-ȚI PLACĂ</span></h2>
      <p class="tb" style="margin:0;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#000000;">${s3_intro}</p>
    </td>
  </tr>
${feed}
  <tr>
    <td class="px" align="center" bgcolor="#FFFFFF" style="background-color:#FFFFFF;padding:14px 40px 34px 40px;">
      <!-- Buton „Vezi și alte mixuri”: doar daca blocul theMarketer nu are butoane proprii (altfel se sterge). -->
      ${cta_rec}
    </td>
  </tr>
  <!-- Fallback (doar daca sectiunea NU se poate ascunde): in locul intro-ului si al blocului: „${s3_fb_line}” + buton „${s3_fb_cta}” ({{SHOP_URL}}, utm_content=cta_rec). -->
  <!-- THEMARKETER_SECTION_S3 END -->
${torn_white_turq}

  <!-- ============ S4 USP (turquoise, 3 columns of 193px, titles on one line) ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#86D2DA" style="background-color:#86D2DA;padding:14px 40px 16px 40px;">
      <h2 class="tb h-xl" style="margin:0 0 26px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:36px;line-height:36px;font-weight:900;text-transform:uppercase;color:#000000;mso-line-height-rule:exactly;">${usp_title}</h2>
    </td>
  </tr>
  <tr>
    <td align="center" bgcolor="#86D2DA" style="background-color:#86D2DA;padding:0 10px 20px 10px;font-size:0;text-align:center;">
<!--[if mso]><table role="presentation" width="579" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td width="193" valign="top"><![endif]-->
      ${usp1}<!--[if mso]></td><td width="193" valign="top"><![endif]-->${usp2}<!--[if mso]></td><td width="193" valign="top"><![endif]-->${usp3}
<!--[if mso]></td></tr></table><![endif]-->
    </td>
  </tr>
${torn_turq_black}

  <!-- ============ S5 CLOSING (black) ============ -->
  <tr>
    <td class="px" align="center" bgcolor="#000000" style="background-color:#000000;padding:20px 40px 36px 40px;text-align:center;">
      <h2 class="to h-xl" style="margin:0 0 12px 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:42px;line-height:42px;font-weight:900;text-transform:uppercase;color:#FAA61A;mso-line-height-rule:exactly;">${s5_title}</h2>
      <p class="tw" style="margin:0 auto 24px auto;max-width:420px;font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:24px;color:#FFFFFF;">${s5_line}</p>
      ${cta_shop}
      <p class="to" style="margin:22px 0 0 0;font-family:Akrobat,'Arial Narrow',Arial,sans-serif;font-size:30px;line-height:32px;font-weight:bold;color:#FAA61A;">${signature}</p>
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
  1. {{FIRST_NAME}}: tag-ul theMarketer + conditie: „Hei!” daca lipseste sau are peste 19 caractere.
  2. {{URL_RETETA_CLATITE}}, {{URL_RETETA_COOKIES}}, {{RECIPES_URL}}, {{SHOP_URL}}: linkurile reale; UTM-urile sunt puse (utm_campaign=website_02).
     Fara pagina proprie de reteta -> {{RECIPES_URL}}.
  3. Recomandari: inlocuieste [RECOMANDĂRI PRODUSE THEMARKETER] (intre THEMARKETER_FEED START/END) cu blocul de recomandari
     (3 produse, latime utila 520px). Fara rezultate: ascunde tot ce e intre THEMARKETER_SECTION_S3 START/END.
  4. Schimb de sezon 1 nov - 31 dec: cardul intre CARD_RETETA_1 START/END devine Gingerbread Pancakes (design-direction.md, sectiunea 6).
  5. {{UNSUBSCRIBE_URL}}: tag-ul de dezabonare theMarketer; footer: fraza „de ce primesti”, SRL + CUI.
  6. assets/ -> URL-uri absolute HTTPS (imagini + fonturi) la upload. -->
'''


def build_html(logo_h, stripes_h):
    pad = "&#847;&zwnj;&nbsp;" * 40
    common = {k: e(v) for k, v in COPY.items() if isinstance(v, str)}
    for k in ("intro", "s2_intro", "s3_intro", "s5_line", "footer_why"):
        common[k] = nb(COPY[k])
    common.update(
        pad=pad, utm=UTM, logo_h=logo_h, stripes_h=stripes_h,
        s5_title=f'{e(COPY["s5_title_l1"])}<br>{e(COPY["s5_title_l2"])}',
        cta_shop=button("{{SHOP_URL}}", COPY["cta_shop"], "cta_shop"),
        cta_rec=button("{{SHOP_URL}}", COPY["cta_rec"], "cta_rec", width=260, height=52, kind="outline", fs=17),
        card1=recipe_card(RECIPES[0], 1),
        card2=recipe_card(RECIPES[1], 2, photo_right=True),
        usp1=usp_col("usp-spatula.png", *COPY["usp"][0]),
        usp2=usp_col("usp-lupa.png", *COPY["usp"][1]),
        usp3=usp_col("usp-pungi.png", *COPY["usp"][2]),
        torn_pink_orange=torn("torn-pink-orange.png", "#FAA61A"),
        torn_orange_white=torn("torn-orange-white.png", "#FFFFFF"),
        torn_white_turq=torn("torn-white-turq.png", "#86D2DA"),
        torn_turq_black=torn("torn-turq-black.png", "#000000"),
        torn_black_white=torn("torn-black-white.png", "#FFFFFF"),
    )
    greet_note = ('<!-- ESP-MARKER: salut conditionat in theMarketer, fallback „Hei!” '
                  '(FIRST_NAME gol sau peste 19 caractere) -->\n      ')
    for name, esp in (("index.html", False), ("index-esp.html", True)):
        out = HTML.substitute(common, esp_header=ESP_HEADER if esp else "", feed=feed_block(esp),
                              esp_greeting=greet_note if esp else
                              "<!-- Greeting: fallback „Hei!” when FIRST_NAME is empty or longer than 19 characters (copy.md S1) -->\n      ")
        if SEASON:
            name = name.replace(".html", "-sezon.html")
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
    torn_divider("torn-pink-orange.png", PINK, TURQ, ORANGE, 13)
    torn_divider("torn-orange-white.png", ORANGE, PINK, WHITE, 29)
    torn_divider("torn-white-turq.png", WHITE, ORANGE, TURQ, 43)
    torn_divider("torn-turq-black.png", TURQ, PINK, BLACK, 59)
    torn_divider("torn-black-white.png", BLACK, ORANGE, WHITE, 71)
    build_recipe_photos()
    build_example_product()
    build_mini_stars()
    build_usp_icons()
    measure_usp()
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
