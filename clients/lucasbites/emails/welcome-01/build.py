#!/usr/bin/env python3
"""Lucas Bites, Welcome Email 1: asset builder.

Usage:  python3 build.py        (needs Pillow)

- Real photos dropped into images/ (exact names below) are processed into assets/.
- Missing photos get a brand-colour placeholder at the final size, so index.html
  never changes: rerun this script after adding photos and the email updates.
- Also builds wave dividers, logos, social icons and review stars.

Brand colours only: #FAA61A, #F7ACB4, #86D2DA, #000000, plus white.
"""
import math
import sys
from io import BytesIO
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
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
JPG_MAX = 200_000                          # bytes
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

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


def save_jpg(img, path):
    img = img.convert("RGB")
    for q in range(82, 55, -4):
        buf = BytesIO()
        img.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
        if buf.tell() <= JPG_MAX or q <= 58:
            path.write_bytes(buf.getvalue())
            report.append(f"{path.relative_to(HERE)}  {img.width}x{img.height}  q{q}  {buf.tell() // 1024}KB")
            return


def save_png(img, path, quantize_over=None):
    img.save(path, "PNG", optimize=True)
    size = path.stat().st_size
    if quantize_over and size > quantize_over and img.mode == "RGBA":
        img.quantize(colors=256, method=Image.Quantize.FASTOCTREE).save(path, "PNG", optimize=True)
        size = path.stat().st_size
    report.append(f"{path.relative_to(HERE)}  {img.width}x{img.height}  {size // 1024}KB")


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


def circle_mask(size):
    m = Image.new("L", (size * SS, size * SS), 0)
    ImageDraw.Draw(m).ellipse((0, 0, size * SS - 1, size * SS - 1), fill=255)
    return m.resize((size, size), Image.LANCZOS)


def centered_text(draw, box, lines, fill=BLACK):
    """lines: list of (text, font). Centred block inside box (x0,y0,x1,y1)."""
    x0, y0, x1, y1 = box
    heights = [draw.textbbox((0, 0), t, font=f)[3] for t, f in lines]
    gap = 14
    total = sum(heights) + gap * (len(lines) - 1)
    y = y0 + (y1 - y0 - total) / 2
    for (t, f), hgt in zip(lines, heights):
        tw = draw.textlength(t, font=f)
        draw.text((x0 + (x1 - x0 - tw) / 2, y), t, font=f, fill=fill)
        y += hgt + gap


def placeholder(w, h, color, label, sub):
    img = Image.new("RGB", (w, h), color)
    d = ImageDraw.Draw(img)
    centered_text(d, (0, 0, w, h), [(label, font(max(28, w // 14))),
                                    (sub, font(max(18, w // 30), bold=False))])
    return img


def real(name):
    p = IMAGES / name
    if p.exists():
        return Image.open(p)
    return None


# ---------------------------------------------------------------- logos
def build_logos():
    src = Image.open(LOGO_DIR / "Logo_LucasBites.png").convert("RGBA")
    w = 360                                                # displayed at 180px
    src.resize((w, round(src.height * w / src.width)), Image.LANCZOS).save(ASSETS / "logo.png", optimize=True)
    report.append(f"assets/logo.png  {w}px wide (shown 180px)")

    # Stripes logo: the band is 6875px wide with the wordmark ~17% of it.
    # Shown full-width the wordmark would be < 120px (logo min size rule), so we
    # crop the band symmetrically around the wordmark. No scaling distortion, no recolour.
    st = Image.open(LOGO_DIR / "Logo_LucasBites_stripes-nobg.png").convert("RGBA")
    # top 470px holds only near-invisible stray pixels (alpha <= 6): trim on a threshold
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
def hero_placeholder_cutout(w=960, h=1200):
    """Stylised pancake stack on transparency, so the overlap effect is visible."""
    S = 2
    img = Image.new("RGBA", (w * S, h * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = w * S // 2
    pw, ph, step, n = 1480, 320, 290, 6
    bottom = h * S - 40
    for i in range(n):
        y1 = bottom - i * step
        x0 = cx - pw // 2 + (14 if i % 2 else -14)
        d.rounded_rectangle((x0, y1 - ph, x0 + pw, y1), radius=160, fill=PINK + (255,),
                            outline=BLACK + (255,), width=14)
    # butter pat on top
    ty = bottom - (n - 1) * step - ph
    d.rounded_rectangle((cx - 150, ty - 110, cx + 150, ty + 40), radius=30, fill=ORANGE + (255,),
                        outline=BLACK + (255,), width=14)
    img = img.resize((w, h), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    mid = bottom // S - 3 * step // S - ph // (2 * S)
    centered_text(d, (0, mid - 60, w, mid + 60),
                  [("IMG1  HERO CUTOUT  4:5", font(44)), ("placeholder, transparent PNG", font(26, False))])
    return img


def build_hero():
    """Cutout composited over an orange block whose wave line crosses the lower
    part of the food, so the stack 'breaks out' into the white section.
    Baked into one opaque image: identical in Outlook, Gmail, Apple Mail."""
    W = 1200
    box_w, box_h = 960, 1200
    src = real("img1-hero.png")
    if src is not None:
        src = src.convert("RGBA")
        if src.getchannel("A").getextrema()[0] == 255:
            print("WARNING: img1-hero.png has no transparency; the overlap effect needs a cutout.")
        else:
            src = src.crop(src.getchannel("A").getbbox())
        tag = "real"
    else:
        src = hero_placeholder_cutout(box_w, box_h)
        src = src.crop(src.getchannel("A").getbbox())
        tag = "placeholder"
    src = ImageOps.contain(src, (box_w, box_h), Image.LANCZOS)
    top, bottom = 24, 40
    H = top + src.height + bottom
    wave_base = top + round(src.height * 0.72)
    canvas = Image.new("RGB", (W, H), ORANGE)
    canvas.paste(Image.new("RGB", (W, H), WHITE), (0, 0), wave_mask(W, H, wave_base, 26, 1.1, 0.6))
    canvas = canvas.convert("RGBA")
    canvas.alpha_composite(src, ((W - src.width) // 2, top))
    save_jpg(canvas, ASSETS / "hero.jpg")
    report[-1] += f"  [{tag}]"
    sync_html_height("assets/hero.jpg", H // 2)


def sync_html_height(src_path, display_h):
    """Keep the height attribute in index.html in step with the generated image."""
    html = HERE / "index.html"
    if not html.exists():
        return
    import re
    text = html.read_text(encoding="utf-8")
    pat = re.compile(r'(src="' + re.escape(src_path) + r'"[^>]*?height=")\d+(")')
    new = pat.sub(lambda m: f"{m.group(1)}{display_h}{m.group(2)}", text)
    if new != text:
        html.write_text(new, encoding="utf-8")


# ---------------------------------------------------------------- cards
def build_circle(src_name, out_name, color, label, sub):
    size = 400
    src = real(src_name)
    if src is not None:
        sq = ImageOps.fit(src.convert("RGB"), (size, size), Image.LANCZOS)
        tag = "real"
    else:
        sq = Image.new("RGB", (size, size), color)
        d = ImageDraw.Draw(sq)
        centered_text(d, (0, 0, size, size), [(label, font(40)), (sub, font(22, False))])
        tag = "placeholder"
    out = sq.convert("RGBA")
    out.putalpha(circle_mask(size))
    save_png(out, ASSETS / out_name, quantize_over=JPG_MAX)
    report[-1] += f"  [{tag}]"


# ---------------------------------------------------------------- full-width photos
def build_img5():
    W, H = 1200, 800
    src = real("img5-tigaie.png")
    if src is not None:
        img, tag = ImageOps.fit(src.convert("RGB"), (W, H), Image.LANCZOS), "real"
    else:
        img, tag = placeholder(W, H, ORANGE, "IMG5  TIGAIE  3:2", "placeholder, pancakes in pan"), "placeholder"
    # bottom edge cut by the pink wave of the reviews section
    img.paste(Image.new("RGB", (W, H), PINK), (0, 0), wave_mask(W, H, H - 46, 20, 1.3, 2.2))
    save_jpg(img, ASSETS / "img5-tigaie.jpg")
    report[-1] += f"  [{tag}]"


def build_img6():
    W, H = 1200, 1200
    src = real("img6-brunch.png")
    if src is not None:
        img, tag = ImageOps.fit(src.convert("RGB"), (W, H), Image.LANCZOS), "real"
    else:
        img, tag = placeholder(W, H, TURQ, "IMG6  BRUNCH  1:1", "placeholder, overhead brunch table"), "placeholder"
    # top edge: pink section flows into the photo with a wave
    img.paste(Image.new("RGB", (W, H), PINK), (0, 0), wave_mask(W, H, 46, 20, 1.2, 4.0, fill_below=False))
    save_jpg(img, ASSETS / "img6-brunch.jpg")
    report[-1] += f"  [{tag}]"


# ---------------------------------------------------------------- UI icons
def icon_canvas(n=256):
    return Image.new("L", (n, n), 0), n


def finish_icon(mask, name, size=64):
    mask = mask.resize((size, size), Image.LANCZOS)
    img = Image.new("RGBA", (size, size), BLACK + (0,))
    img.putalpha(mask)
    save_png(img, ASSETS / name)


def build_icons():
    # Instagram: black circle, glyph knocked out
    m, n = icon_canvas()
    d = ImageDraw.Draw(m)
    d.ellipse((0, 0, n - 1, n - 1), fill=255)
    d.rounded_rectangle((68, 68, 188, 188), radius=34, outline=0, width=16)
    d.ellipse((99, 99, 157, 157), outline=0, width=16)
    d.ellipse((156, 84, 174, 102), fill=0)
    finish_icon(m, "icon-instagram.png")

    # TikTok: music note knocked out
    m, n = icon_canvas()
    d = ImageDraw.Draw(m)
    d.ellipse((0, 0, n - 1, n - 1), fill=255)
    d.rectangle((128, 58, 150, 168), fill=0)                 # stem
    d.ellipse((76, 134, 150, 200), outline=0, width=22)      # head ring
    d.arc((128, 10, 214, 108), start=95, end=180, fill=0, width=22)  # flag
    finish_icon(m, "icon-tiktok.png")

    # Facebook: "f" knocked out
    m, n = icon_canvas()
    d = ImageDraw.Draw(m)
    d.ellipse((0, 0, n - 1, n - 1), fill=255)
    f = font(190)
    tw = d.textlength("f", font=f)
    bb = d.textbbox((0, 0), "f", font=f)
    d.text(((n - tw) / 2 + 6, (n - (bb[3] - bb[1])) / 2 - bb[1] + 18), "f", font=f, fill=0)
    finish_icon(m, "icon-facebook.png")

    # YouTube: rounded rectangle knocked out, play triangle restored
    m, n = icon_canvas()
    d = ImageDraw.Draw(m)
    d.ellipse((0, 0, n - 1, n - 1), fill=255)
    d.rounded_rectangle((56, 80, 200, 176), radius=28, fill=0)
    d.polygon([(110, 104), (110, 152), (152, 128)], fill=255)
    finish_icon(m, "icon-youtube.png")

    # Five review stars, shown 160x28
    sw, gap, h = 28 * SS * 2, 5 * SS * 2, 28 * SS * 2
    W = sw * 5 + gap * 4
    m = Image.new("L", (W, h), 0)
    d = ImageDraw.Draw(m)
    for k in range(5):
        cx, cy, R, r = k * (sw + gap) + sw / 2, h / 2 + h * 0.04, sw / 2, sw / 2 * 0.45
        pts = []
        for i in range(10):
            a = -math.pi / 2 + i * math.pi / 5
            rad = R if i % 2 == 0 else r
            pts.append((cx + rad * math.cos(a), cy + rad * math.sin(a)))
        d.polygon(pts, fill=255)
    m = m.resize((W // SS, h // SS), Image.LANCZOS)
    img = Image.new("RGBA", m.size, BLACK + (0,))
    img.putalpha(m)
    save_png(img, ASSETS / "stars.png")


# ---------------------------------------------------------------- main
def main():
    ASSETS.mkdir(exist_ok=True)
    IMAGES.mkdir(exist_ok=True)
    build_logos()
    wave_divider("wave-white-orange.png", WHITE, ORANGE, phase=0.0)
    wave_divider("wave-white-turq.png", WHITE, TURQ, phase=3.4, periods=1.4)
    wave_divider("wave-black-white.png", BLACK, WHITE, phase=1.6, periods=1.2)
    build_hero()
    build_circle("img2-pancakes.png", "img2-pancakes.png", ORANGE, "IMG2", "pancakes 1:1")
    build_circle("img3-clatite.png", "img3-clatite.png", PINK, "IMG3", "clătite 1:1")
    build_circle("img4-brownie.png", "img4-brownie.png", TURQ, "IMG4", "brownie 1:1")
    build_img5()
    build_img6()
    build_icons()
    print("Built assets:")
    for line in report:
        print("  " + line)


if __name__ == "__main__":
    main()
