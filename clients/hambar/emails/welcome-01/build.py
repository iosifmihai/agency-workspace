#!/usr/bin/env python3
"""Hambar, Welcome Email 1: asset builder (needs Pillow).

- Photos in images/ are cropped, resized and saved as optimised JPG in assets/.
- Missing photos get a placeholder at the final size, so index.html never changes.
- Logos come from clients/hambar/logos/, social icons are recoloured from the
  Lucas Bites icon set (generic glyphs) to the footer ink #efedea.
"""
import sys
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps

HERE = Path(__file__).resolve().parent
CLIENT = HERE.parents[1]
IMAGES, ASSETS = HERE / "images", HERE / "assets"
LOGOS = CLIENT / "logos"
ICONS = CLIENT.parent / "lucasbites" / "emails" / "welcome-01" / "assets"
ASSETS.mkdir(exist_ok=True)

BG = (247, 246, 245)
FOOTER_INK = (239, 237, 234)
PLACEHOLDER = (65, 53, 53)
JPG_MAX = 200_000
report = []

# name in images/ -> (asset name, output size, vertical crop anchor)
PHOTOS = {
    "img1-hero.png": ("hero.jpg", (1200, 1500), 0.5),
    "img2-zacusca-muraturi.png": ("cat-zacusca.jpg", (560, 560), 0.5),
    "img3-branzeturi-lactate.png": ("cat-branzeturi.jpg", (560, 560), 0.5),
    "img4-carne-mezeluri.png": ("cat-carne.jpg", (560, 560), 0.5),
    "img5-miere-dulceturi.png": ("cat-miere.jpg", (560, 560), 0.5),
    "img6-paine-patiserie.png": ("cat-paine.jpg", (560, 560), 0.5),
    "img7-cosuri-cadouri.png": ("cat-cosuri.jpg", (560, 560), 0.5),
    "img8-producator.png": ("producator.jpg", (1200, 800), 0.5),
}


def save_jpg(img, path):
    img = img.convert("RGB")
    for q in range(84, 55, -4):
        buf = BytesIO()
        img.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
        if buf.tell() <= JPG_MAX or q <= 58:
            path.write_bytes(buf.getvalue())
            report.append(f"{path.name}  {img.width}x{img.height}  q{q}  {buf.tell() // 1024}KB")
            return


def find_source(name):
    for ext in (".png", ".jpg", ".jpeg", ".webp"):
        p = IMAGES / (Path(name).stem + ext)
        if p.exists():
            return p
    return None


def build_photos():
    for src_name, (out, size, anchor) in PHOTOS.items():
        src = find_source(src_name)
        if src:
            img = ImageOps.fit(Image.open(src).convert("RGB"), size, Image.LANCZOS, centering=(0.5, anchor))
        else:
            img = Image.new("RGB", size, PLACEHOLDER)
            report.append(f"MISSING {src_name} -> placeholder")
        if out == "hero.jpg" and src:
            img = darken_top(img)
        save_jpg(img, ASSETS / out)


def darken_top(img, strength=0.55, until=0.55):
    """Ink gradient over the top of the hero so live white text keeps AA contrast."""
    w, h = img.size
    grad = Image.new("L", (1, h))
    stop = int(h * until)
    for y in range(h):
        grad.putpixel((0, y), int(255 * strength * max(0.0, 1 - y / stop)) if y < stop else 0)
    ink = Image.new("RGB", (w, h), (36, 30, 30))
    return Image.composite(ink, img, grad.resize((w, h)))


def build_logos():
    # header logo on solid background so forced dark mode cannot hide it
    logo = Image.open(LOGOS / "hambar-logotype.png").convert("RGBA")
    flat = Image.new("RGBA", logo.size, BG + (255,))
    flat.alpha_composite(logo)
    flat.convert("RGB").save(ASSETS / "logo.png", optimize=True)
    Image.open(LOGOS / "hambar-logotype-white.png").save(ASSETS / "logo-white.png", optimize=True)
    report.append("logo.png, logo-white.png")


def build_icons():
    for n in ("facebook", "instagram", "tiktok", "youtube"):
        src = Image.open(ICONS / f"icon-{n}.png").convert("RGBA")
        out = Image.new("RGBA", src.size, FOOTER_INK + (0,))
        out.putalpha(src.getchannel("A"))
        out.save(ASSETS / f"icon-{n}.png", optimize=True)
    report.append("icons x4 (#efedea)")


if __name__ == "__main__":
    build_photos()
    build_logos()
    build_icons()
    print("\n".join(report))
