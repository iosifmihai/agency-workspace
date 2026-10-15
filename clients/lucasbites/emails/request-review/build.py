#!/usr/bin/env python3
"""Lucas Bites, Request review email: asset builder.

Usage:  python3 build.py        (needs Pillow only, no network)

Same approach as new-customer-01/build.py:
- Photos from images/ (hero.png, social-1/2/3.png; .png/.jpg/.jpeg) are
  pre-composited onto their section colour as opaque files in assets/.
  hero: whole image, NO crop, NO card, background snapped to exact orange,
  full content width with proportional height (index.html height synced).
  social: square UGC photos, rounded square tiles on pink.
- Missing photos get placeholders at the final size; rerun after adding them.
- Builds the wave dividers, logos, social icons (identical to the family) and
  copies the Akrobat webfont from welcome-03.
- Also builds: V chevron (orange > black), speech-bubble tails, outline stars
  replaced by: S1 outline star strip (one image, one link) and S1 bubble tail.
- Product images in S2 / S4 are NOT built here: they come from the theMarketer feed.
- Ends by writing index-figma.html / index-figma-mobile.html (tools/figma_export.py).

Brand colours only: #FAA61A, #F7ACB4, #86D2DA, #000000, plus white.
"""
import math
import re
import shutil
import sys
from io import BytesIO
from pathlib import Path

try:
    from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps
except ImportError:
    sys.exit("Pillow missing. Install it in a venv: python3 -m venv .venv && .venv/bin/pip install Pillow")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
IMAGES = HERE / "images"
ASSETS = HERE / "assets"
LOGO_DIR = ROOT / "Logo"
FONTS_SRC = HERE.parent / "welcome-03" / "assets" / "fonts"

ORANGE = (250, 166, 26)
PINK = (247, 172, 180)
TURQ = (134, 210, 218)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SS = 4
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

# Image slots (export size = 2x display size)
HERO_W = 1200           # shown 600 wide, height proportional, on orange
TILE = (320, 320)       # social tiles, shown 160 x 160, on pink

report = []


def font(size):
    try:
        return ImageFont.truetype(FONT_BOLD, size)
    except OSError:
        return ImageFont.load_default(size=size)


def save_jpg(img, path, max_bytes):
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


def find_input(stem):
    if not IMAGES.exists():
        return None
    for p in sorted(IMAGES.glob("*")):
        if p.stem.lower() == stem.lower() and p.suffix.lower() in (".png", ".jpg", ".jpeg"):
            return p
    return None


def wave_mask(w, h, base, amp, periods, phase):
    W, H = w * SS, h * SS
    pts = [(W * i / 240, (base + amp * math.sin(2 * math.pi * periods * i / 240 + phase)) * SS) for i in range(241)]
    pts += [(W, H), (0, H)]
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).polygon(pts, fill=255)
    return m.resize((w, h), Image.LANCZOS)


def wave(name, top, bottom, phase=0.0, periods=1.5, h=96, amp=18):
    """Wave divider (ref Misfits): 1200 x 96, shown 600 x 48."""
    img = Image.new("RGB", (1200, h), top)
    img.paste(Image.new("RGB", (1200, h), bottom), (0, 0), wave_mask(1200, h, h / 2, amp, periods, phase))
    save_png(img, ASSETS / name)


def has_alpha(img):
    return img.mode in ("RGBA", "LA") and img.getchannel("A").getextrema()[0] < 250


def fit_slot(src, size, bg, contain_if_alpha=True):
    """Transparent: contain on bg colour. Opaque: cover-crop."""
    if has_alpha(src) and contain_if_alpha:
        src = src.convert("RGBA")
        bbox = src.getchannel("A").point(lambda v: 255 if v > 20 else 0).getbbox()
        if bbox:
            src = src.crop(bbox)
        src.thumbnail((int(size[0] * 0.96), int(size[1] * 0.96)), Image.LANCZOS)
        canvas = Image.new("RGBA", size, bg + (255,))
        canvas.alpha_composite(src, ((size[0] - src.width) // 2, size[1] - src.height - int(size[1] * 0.02)))
        return canvas.convert("RGB")
    return ImageOps.fit(src.convert("RGB"), size, Image.LANCZOS)


def placeholder(size, bg, label, sub, ink=BLACK):
    img = Image.new("RGB", size, bg)
    d = ImageDraw.Draw(img)
    w, h = size
    d.rectangle((10, 10, w - 11, h - 11), outline=ink, width=4)
    f1, f2 = font(max(20, h // 9)), font(max(14, h // 18))
    for txt, f, y in ((label, f1, h / 2 - h // 10), (sub, f2, h / 2 + h // 20)):
        tw = d.textlength(txt, font=f)
        d.text(((w - tw) / 2, y), txt, font=f, fill=ink)
    return img


def rounded(img, bg, radius):
    W, H = img.size
    m = Image.new("L", (W * SS, H * SS), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, W * SS - 1, H * SS - 1), radius=radius * SS, fill=255)
    m = m.resize((W, H), Image.LANCZOS)
    out = Image.new("RGB", (W, H), bg)
    out.paste(img, (0, 0), m)
    return out


def snap_bg(img, target, near=34, far=70):
    """Generated photos sit on a slightly-off brand colour: pull pixels close to the
    corner colour onto the exact brand colour (soft ramp), so there is no seam."""
    w, h = img.size
    px = [img.getpixel(p) for p in ((2, 2), (w - 3, 2), (2, h - 3), (w - 3, h - 3))]
    bg = tuple(sorted(c[i] for c in px)[1] for i in range(3))
    r, g, b = img.split()
    dist = Image.merge("RGB", [ch.point(lambda v, k=bg[i]: abs(v - k)) for i, ch in enumerate((r, g, b))])
    d = ImageChops.lighter(ImageChops.lighter(*dist.split()[:2]), dist.split()[2])
    mask = d.point(lambda v: 255 if v <= near else 0 if v >= far else int(255 * (far - v) / (far - near)))
    out = img.copy()
    out.paste(Image.new("RGB", img.size, target), (0, 0), mask)
    return out


# ---------------------------------------------------------------- photos
def trim_bg(img, bg, tol=40, pad=0.06):
    """Crop away empty background around the subject (bbox of non-bg pixels + pad),
    clamped to the image, so the food is never cut."""
    diff = ImageChops.difference(img, Image.new("RGB", img.size, bg)).convert("L")
    bbox = diff.point(lambda v: 255 if v > tol else 0).getbbox()
    if not bbox:
        return img
    px, py = int((bbox[2] - bbox[0]) * pad), int((bbox[3] - bbox[1]) * pad)
    box = (0, max(0, bbox[1] - py), img.width, min(img.height, bbox[3] + py))  # vertical only: keeps the plate at its natural size
    report.append(f"  hero trimmed {img.size} -> {box}")
    return img.crop(box)


def build_hero():
    """Whole image, no crop, no card: 1200 wide, height proportional,
    background snapped to exact orange so it blends into S1."""
    p = find_input("hero")
    if p:
        src = Image.open(p)
        if has_alpha(src):
            bg = Image.new("RGBA", src.size, ORANGE + (255,))
            bg.alpha_composite(src.convert("RGBA"))
            src = bg.convert("RGB")
        else:
            src = snap_bg(src.convert("RGB"), ORANGE)
        src = trim_bg(src, ORANGE)
        img = src.resize((HERO_W, round(src.height * HERO_W / src.width)), Image.LANCZOS)
    else:
        img = placeholder((HERO_W, 900), ORANGE, "HERO 1200 x 900", "pancakes, prima felie tăiată")
        report.append("  ! images/hero.png missing: placeholder")
    save_jpg(img, ASSETS / "hero.jpg", 230_000)
    return img.height // 2


def build_social():
    for i in (1, 2, 3):
        p = find_input(f"social-{i}")
        if p:
            img = ImageOps.fit(Image.open(p).convert("RGB"), TILE, Image.LANCZOS)  # square in, square out: no visible crop
        else:
            img = placeholder(TILE, WHITE, f"SOCIAL {i}", "800 x 800")
            report.append(f"  ! images/social-{i}.png missing: placeholder")
        save_jpg(rounded(img, PINK, 28), ASSETS / f"social-{i}.jpg", 60_000)


# ---------------------------------------------------------------- shapes
def chevron(name, top, bottom, w=1200, h=120):
    """Angled V divider (ref IQBAR): top colour points down into the next section."""
    m = Image.new("L", (w * SS, h * SS), 0)
    ImageDraw.Draw(m).polygon([(0, 0), (w * SS, 0), (w * SS / 2, h * SS)], fill=255)
    img = Image.new("RGB", (w, h), bottom)
    img.paste(Image.new("RGB", (w, h), top), (0, 0), m.resize((w, h), Image.LANCZOS))
    save_png(img, ASSETS / name)


def tail(name, colour, bg, side, w=36, h=56):
    """Speech-bubble tail: triangle pointing left or right toward the product image."""
    W, H = w * SS, h * SS
    pts = [(W, 0), (W, H), (0, H * 0.5)] if side == "l" else [(0, 0), (0, H), (W, H * 0.5)]
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).polygon(pts, fill=255)
    img = Image.new("RGB", (w, h), bg)
    img.paste(Image.new("RGB", (w, h), colour), (0, 0), m.resize((w, h), Image.LANCZOS))
    save_png(img, ASSETS / name)


def outline_tail(name, bg, w=80, h=96, stroke=6):
    """Tail for the empty S3 bubble: black outline, pink fill, pointing down-left."""
    W, H, s = w * SS, h * SS, stroke * SS
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    d.polygon([(s, 0), (W - s, 0), (s, H - s)], fill=BLACK)
    d.polygon([(s * 2.2, 0), (W - s * 3.6, 0), (s * 2.2, H - s * 3.6)], fill=bg)
    save_png(img.resize((w, h), Image.LANCZOS), ASSETS / name)


def down_tail(name, colour, bg, w=72, h=60):
    """IQBAR bubble tail under the S1 bubble: vertical left edge, slants down-left. Shown 36 x 30."""
    W, H = w * SS, h * SS
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).polygon([(0, 0), (W, 0), (0, H)], fill=255)
    img = Image.new("RGB", (w, h), bg)
    img.paste(Image.new("RGB", (w, h), colour), (0, 0), m.resize((w, h), Image.LANCZOS))
    save_png(img, ASSETS / name)


def star_pts(cx, cy, r, ri):
    return [(cx + (r if i % 2 == 0 else ri) * math.sin(math.pi * i / 5),
             cy - (r if i % 2 == 0 else ri) * math.cos(math.pi * i / 5)) for i in range(10)]


def build_stars():
    # S1: 5 empty (outline) orange stars on black, one image = one link. 520 x 96, shown 260 x 48.
    w, h = 520, 96
    m = Image.new("L", (w * SS, h * SS), 0)
    d = ImageDraw.Draw(m)
    for i in range(5):
        cx, cy = (52 + i * 104) * SS, h * SS * 0.53
        d.polygon(star_pts(cx, cy, 46 * SS, 19 * SS), fill=255)
        d.polygon(star_pts(cx, cy, 37 * SS, 15 * SS), fill=0)
    img = Image.new("RGB", (w, h), BLACK)
    img.paste(Image.new("RGB", (w, h), ORANGE), (0, 0), m.resize((w, h), Image.LANCZOS))
    save_png(img, ASSETS / "stars-outline-orange.png")


# ---------------------------------------------------------------- family assets (same as new-customer-01)
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
    w = 520
    st = st.resize((w, round(st.height * w / st.width)), Image.LANCZOS)
    st.save(ASSETS / "logo-stripes.png", optimize=True)
    report.append(f"assets/logo-stripes.png  {w}x{st.height} (shown 260px)")


def copy_fonts():
    dst = ASSETS / "fonts"
    dst.mkdir(exist_ok=True)
    found = list(FONTS_SRC.glob("Akrobat-*.woff*"))
    if not found:
        print(f"WARNING: no Akrobat webfont found in {FONTS_SRC}")
    for f in found:
        shutil.copy2(f, dst / f.name)


def finish_icon(mask, name, size=64):
    mask = mask.resize((size, size), Image.LANCZOS)
    img = Image.new("RGBA", (size, size), BLACK + (0,))
    img.putalpha(mask)
    save_png(img, ASSETS / name)


def build_icons():
    n = 256
    m = Image.new("L", (n, n), 0); d = ImageDraw.Draw(m)
    d.ellipse((0, 0, n - 1, n - 1), fill=255)
    d.rounded_rectangle((68, 68, 188, 188), radius=34, outline=0, width=16)
    d.ellipse((99, 99, 157, 157), outline=0, width=16)
    d.ellipse((156, 84, 174, 102), fill=0)
    finish_icon(m, "icon-instagram.png")

    m = Image.new("L", (n, n), 0); d = ImageDraw.Draw(m)
    d.ellipse((0, 0, n - 1, n - 1), fill=255)
    d.rectangle((128, 58, 150, 168), fill=0)
    d.ellipse((76, 134, 150, 200), outline=0, width=22)
    d.arc((128, 10, 214, 108), start=95, end=180, fill=0, width=22)
    finish_icon(m, "icon-tiktok.png")

    m = Image.new("L", (n, n), 0); d = ImageDraw.Draw(m)
    d.ellipse((0, 0, n - 1, n - 1), fill=255)
    f = font(190)
    tw = d.textlength("f", font=f)
    bb = d.textbbox((0, 0), "f", font=f)
    d.text(((n - tw) / 2 + 6, (n - (bb[3] - bb[1])) / 2 - bb[1] + 18), "f", font=f, fill=0)
    finish_icon(m, "icon-facebook.png")

    m = Image.new("L", (n, n), 0); d = ImageDraw.Draw(m)
    d.ellipse((0, 0, n - 1, n - 1), fill=255)
    d.rounded_rectangle((56, 80, 200, 176), radius=28, fill=0)
    d.polygon([(110, 104), (110, 152), (152, 128)], fill=255)
    finish_icon(m, "icon-youtube.png")


def sync_height(name, h):
    html = HERE / "index.html"
    t = html.read_text(encoding="utf-8")
    t2 = re.sub(r'(src="assets/%s" width="600" height=")\d+(")' % re.escape(name), lambda m: f"{m.group(1)}{h}{m.group(2)}", t)
    if t2 != t:
        html.write_text(t2, encoding="utf-8")


def main():
    ASSETS.mkdir(exist_ok=True)
    build_logos()
    copy_fonts()
    wave("wave-white-orange.png", WHITE, ORANGE, phase=0.0)
    wave("wave-orange-pink.png", ORANGE, PINK, phase=math.pi / 2)
    wave("wave-pink-white.png", PINK, WHITE, phase=-math.pi / 2)
    down_tail("tail-black-down.png", BLACK, ORANGE)
    outline_tail("tail-outline-pink.png", PINK)
    build_stars()
    build_social()
    build_icons()
    print("Built assets:")
    for line in report:
        print("  " + line)
    sys.path.insert(0, str(HERE.parent / "tools"))
    from figma_export import export
    export(HERE)


if __name__ == "__main__":
    main()
