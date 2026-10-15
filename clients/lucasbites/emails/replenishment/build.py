#!/usr/bin/env python3
"""Lucas Bites, Replenishment email: asset builder.

Usage:  python3 build.py        (needs Pillow only, no network)

Same approach as new-customer-01/build.py:
- Photos from images/ (hero.png, s4-icon-clean.png, s5-cta.png; .png/.jpg/.jpeg)
  are pre-composited onto their section colour as opaque files in assets/, so
  index.html never changes. Transparent PNGs are composited on the brand colour;
  opaque photos are cover-cropped to the slot.
- Missing photos get placeholders at the final size; rerun after adding them.
- Builds the wave dividers, logos, social icons (identical to the family) and
  copies the Akrobat webfont from welcome-03.
- Product images in S3 are NOT built here: they come from the theMarketer feed.
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
HERO = (1200, 880)      # shown 600 x 440, on orange
ICON = (192, 192)       # shown 96 x 96, on black
# S5: full content width, export 1200 wide, height proportional (shown 600 wide)

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
def build_hero():
    p = find_input("hero")
    if p:
        src = Image.open(p)
        if has_alpha(src):
            img = fit_slot(src, HERO, ORANGE)
        else:  # opaque photo on solid orange: contain (no crop), centred on orange
            src = snap_bg(src.convert("RGB"), ORANGE)
            src.thumbnail(HERO, Image.LANCZOS)
            img = Image.new("RGB", HERO, ORANGE)
            img.paste(src, ((HERO[0] - src.width) // 2, (HERO[1] - src.height) // 2))
    else:
        img = placeholder(HERO, ORANGE, "HERO 1200 x 880", "teanc de pancakes, ingrediente în zbor")
        report.append("  ! images/hero.png missing: placeholder")
    save_jpg(img, ASSETS / "hero.jpg", 230_000)


def build_icon():
    p = find_input("s4-icon-clean")
    if p:
        img = fit_slot(Image.open(p), ICON, BLACK)
    else:
        # placeholder: orange ring with a check, reads as "clean label"
        n = ICON[0] * SS
        m = Image.new("L", (n, n), 0)
        d = ImageDraw.Draw(m)
        d.ellipse((8 * SS, 8 * SS, n - 8 * SS, n - 8 * SS), outline=255, width=12 * SS)
        d.line([(58 * SS, 98 * SS), (84 * SS, 124 * SS), (136 * SS, 70 * SS)], fill=255, width=14 * SS, joint="curve")
        m = m.resize(ICON, Image.LANCZOS)
        img = Image.new("RGB", ICON, BLACK)
        img.paste(Image.new("RGB", ICON, ORANGE), (0, 0), m)
        report.append("  ! images/s4-icon-clean.png missing: placeholder icon")
    save_png(img.convert("RGB"), ASSETS / "s4-icon.png")


def build_cta():
    """Whole image, no crop, no rounded card: full content width (600), height
    proportional, background snapped to exact turquoise so it blends in."""
    p = find_input("s5-cta")
    if p:
        src = snap_bg(Image.open(p).convert("RGB"), TURQ)
        w = 1200
        img = src.resize((w, round(src.height * w / src.width)), Image.LANCZOS)
    else:
        img = placeholder((1200, 738), TURQ, "S5 1200 x 738", "imagine de produs / lifestyle")
        report.append("  ! images/s5-cta.png missing: placeholder")
    save_jpg(img, ASSETS / "s5-cta.jpg", 220_000)
    return img.height // 2


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


def sync_cta_height(h):
    html = HERE / "index.html"
    t = html.read_text(encoding="utf-8")
    t2 = re.sub(r'(src="assets/s5-cta.jpg" width="600" height=")\d+(")', lambda m: f"{m.group(1)}{h}{m.group(2)}", t)
    if t2 != t:
        html.write_text(t2, encoding="utf-8")


def main():
    ASSETS.mkdir(exist_ok=True)
    build_logos()
    copy_fonts()
    wave("wave-white-orange.png", WHITE, ORANGE, phase=0.0)
    wave("wave-orange-white.png", ORANGE, WHITE, phase=math.pi)
    wave("wave-white-pink.png", WHITE, PINK, phase=math.pi / 2)
    wave("wave-pink-black.png", PINK, BLACK, phase=0.0)
    wave("wave-black-turq.png", BLACK, TURQ, phase=math.pi)
    wave("wave-turq-white.png", TURQ, WHITE, phase=-math.pi / 2)
    build_hero()
    build_icon()
    sync_cta_height(build_cta())
    build_icons()
    print("Built assets:")
    for line in report:
        print("  " + line)
    sys.path.insert(0, str(HERE.parent / "tools"))
    from figma_export import export
    export(HERE)


if __name__ == "__main__":
    main()
