#!/usr/bin/env python3
"""Lucas Bites, Sunset email: asset builder.

Usage:  python3 build.py        (needs Pillow only, no network)

- images/s1-visual.png (~1200 x 600, solid #FAA61A bg): whole image, NO crop,
  NO card, background snapped to exact orange, empty margins trimmed, exported
  640 wide (shown 320), height synced into index.html. Missing: placeholder.
- Waves: white>orange, orange>white, white>turquoise, turquoise>white.
- Family assets (logos, social icons, Akrobat webfont) copied from request-review/.
- Product images in S2 come from the theMarketer feed, not built here.
- Ends by writing index-figma.html / index-figma-mobile.html (tools/figma_export.py).
Brand colours only: #FAA61A, #F7ACB4, #86D2DA, #000000, plus white.
"""
import math, re, shutil, sys
from io import BytesIO
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
IMAGES, ASSETS = HERE / "images", HERE / "assets"
FAMILY = HERE.parent / "request-review" / "assets"
ORANGE, TURQ, BLACK, WHITE = (250, 166, 26), (134, 210, 218), (0, 0, 0), (255, 255, 255)
SS = 4
VIS_W = 640  # shown 320
report = []


def save_jpg(img, path, max_bytes):
    img = img.convert("RGB")
    for q in range(90, 55, -4):
        buf = BytesIO()
        img.save(buf, "JPEG", quality=q, optimize=True, progressive=True, subsampling=0)
        if buf.tell() <= max_bytes or q <= 62:
            break
    path.write_bytes(buf.getvalue())
    report.append(f"{path.name}  {img.width}x{img.height}  q{q}  {buf.tell() // 1024}KB")


def wave(name, top, bottom, phase=0.0, periods=1.5, h=96, amp=18):
    W, H = 1200 * SS, h * SS
    pts = [(W * i / 240, (h / 2 + amp * math.sin(2 * math.pi * periods * i / 240 + phase)) * SS) for i in range(241)]
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).polygon(pts + [(W, H), (0, H)], fill=255)
    img = Image.new("RGB", (1200, h), top)
    img.paste(Image.new("RGB", (1200, h), bottom), (0, 0), m.resize((1200, h), Image.LANCZOS))
    img.save(ASSETS / name, optimize=True)
    report.append(name)


def snap_bg(img, target, near=34, far=70):
    w, h = img.size
    px = [img.getpixel(p) for p in ((2, 2), (w - 3, 2), (2, h - 3), (w - 3, h - 3))]
    bg = tuple(sorted(c[i] for c in px)[1] for i in range(3))
    chans = [ch.point(lambda v, k=bg[i]: abs(v - k)) for i, ch in enumerate(img.split())]
    d = ImageChops.lighter(ImageChops.lighter(chans[0], chans[1]), chans[2])
    mask = d.point(lambda v: 255 if v <= near else 0 if v >= far else int(255 * (far - v) / (far - near)))
    out = img.copy()
    out.paste(Image.new("RGB", img.size, target), (0, 0), mask)
    return out


def trim(img, bg, tol=40, pad=0.08):
    diff = ImageChops.difference(img, Image.new("RGB", img.size, bg)).convert("L")
    b = diff.point(lambda v: 255 if v > tol else 0).getbbox()
    if not b:
        return img
    px, py = int((b[2] - b[0]) * pad), int((b[3] - b[1]) * pad)
    return img.crop((max(0, b[0] - px), max(0, b[1] - py), min(img.width, b[2] + px), min(img.height, b[3] + py)))


def build_visual():
    src = next((p for p in sorted(IMAGES.glob("s1-visual.*")) if p.suffix.lower() in (".png", ".jpg", ".jpeg")), None)
    if src:
        im = Image.open(src)
        if im.mode in ("RGBA", "LA"):
            bg = Image.new("RGBA", im.size, ORANGE + (255,)); bg.alpha_composite(im.convert("RGBA")); im = bg
        im = trim(snap_bg(im.convert("RGB"), ORANGE), ORANGE)
        im = im.resize((VIS_W, round(im.height * VIS_W / im.width)), Image.LANCZOS)
        im = snap_bg(im, ORANGE)
    else:
        im = Image.new("RGB", (VIS_W, 320), ORANGE)
        d = ImageDraw.Draw(im)
        d.rectangle((8, 8, VIS_W - 9, 311), outline=BLACK, width=4)
        try:
            f = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 34)
        except OSError:
            f = ImageFont.load_default()
        for t, y in (("S1 VISUAL 640 x 320", 120), ("images/s1-visual.png", 170)):
            d.text(((VIS_W - d.textlength(t, font=f)) / 2, y), t, font=f, fill=BLACK)
        report.append("! images/s1-visual.png missing: placeholder")
    save_jpg(im, ASSETS / "s1-visual.jpg", 120_000)
    h = im.height // 2
    html = HERE / "index.html"
    t = html.read_text(encoding="utf-8")
    html.write_text(re.sub(r'(src="assets/s1-visual\.jpg" width="320" height=")\d+', lambda m: m.group(1) + str(h), t), encoding="utf-8")


def main():
    ASSETS.mkdir(exist_ok=True)
    for n in ("logo.png", "logo-stripes.png", "icon-instagram.png", "icon-tiktok.png", "icon-facebook.png", "icon-youtube.png"):
        shutil.copy2(FAMILY / n, ASSETS / n)
    shutil.copytree(FAMILY / "fonts", ASSETS / "fonts", dirs_exist_ok=True)
    wave("wave-white-orange.png", WHITE, ORANGE, 0.0)
    wave("wave-orange-white.png", ORANGE, WHITE, math.pi / 2)
    wave("wave-white-turq.png", WHITE, TURQ, -math.pi / 2)
    wave("wave-turq-white.png", TURQ, WHITE, math.pi)
    build_visual()
    print("Built:", *report, sep="\n  ")
    sys.path.insert(0, str(HERE.parent / "tools"))
    from figma_export import export
    export(HERE)


if __name__ == "__main__":
    main()
