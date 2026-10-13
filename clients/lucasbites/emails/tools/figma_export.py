#!/usr/bin/env python3
"""Lucas Bites emails: self-contained HTML for Figma import.

Usage:  python3 tools/figma_export.py welcome-01 [welcome-02 ...]
        (or call export(folder) from an email's build.py)

Figma (html.to.design / the Figma MCP importer) does not fetch external files,
so relative paths like assets/hero.jpg or assets/fonts/*.woff2 come in empty.
For each email folder this reads index.html (left untouched, it is the ESP
version) and writes:

- index-figma.html         desktop, 600px frame
- index-figma-mobile.html  mobile, 375px frame (the max-width:599px rules applied)

Both embed every local image and font as a base64 data URI, drop the hidden
preheader and the Outlook-only conditional blocks, and fix the page width so
the captured frame is exactly the email width. Stdlib only.
"""
import base64
import mimetypes
import re
import sys
from pathlib import Path

MIME = {".woff2": "font/woff2", ".woff": "font/woff", ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg", ".png": "image/png", ".gif": "image/gif"}

MEDIA_RE = re.compile(r"@media only screen and \(max-width:599px\)\{(.*?)\n\s*\}\n", re.S)


def data_uri(path):
    mime = MIME.get(path.suffix.lower()) or mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def inline_assets(html, folder):
    missing = []

    def sub(m):
        ref = m.group(2)
        p = folder / ref
        if "..." in ref:  # example path inside an HTML comment
            return m.group(0)
        if not p.is_file():
            missing.append(ref)
            return m.group(0)
        return f"{m.group(1)}{data_uri(p)}{m.group(3)}"

    html = re.sub(r'(src=")((?:assets|images|ugc)/[^"]+)(")', sub, html)
    html = re.sub(r"(url\(')((?:assets|images)/[^']+)('\))", sub, html)
    return html, missing


def feed_placeholders(html):
    """<img src="{{ESP_TAG}}"> would import as a broken image: swap in a grey
    placeholder of the same size, labelled like the previews."""
    def sub(m):
        tag = m.group(0)
        w = re.search(r'\bwidth="(\d+)"', tag)
        h = re.search(r'\bheight="(\d+)"', tag)
        w = int(w.group(1)) if w else 120
        h = int(h.group(1)) if h else w
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w*2}" height="{h*2}">'
               f'<rect width="100%" height="100%" fill="#E6E6E6"/>'
               f'<text x="50%" y="50%" text-anchor="middle" dominant-baseline="middle" '
               f'font-family="Arial" font-weight="bold" font-size="{max(12, min(w, h) // 5)}" '
               f'fill="#000000">IMAGINE DIN FEED</text></svg>')
        uri = "data:image/svg+xml;base64," + base64.b64encode(svg.encode("utf-8")).decode("ascii")
        return re.sub(r'src="\{\{[^"]*\}\}"', f'src="{uri}"', tag)

    return re.sub(r'<img\b[^>]*src="\{\{[^"]*\}\}"[^>]*>', sub, html)


def strip_email_only(html):
    # Outlook-only blocks (VML buttons, ghost tables, mso styles); browsers skip them anyway
    html = re.sub(r"<!--\[if mso\]>.*?<!\[endif\]-->", "", html, flags=re.S)
    # Hidden preheader: would import as an invisible layer
    html = re.sub(r"<!-- Preheader -->\s*<div style=\"display:none;.*?</div>\s*", "", html, count=1, flags=re.S)
    return html


def lock_width(html, width, mobile_rules=""):
    css = (f"\n<style>html,body{{width:{width}px!important;min-width:{width}px!important;"
           f"max-width:{width}px!important;margin:0!important;padding:0!important;}}"
           f"{mobile_rules}</style>\n</head>")
    return html.replace("</head>", css, 1)


def export(folder):
    folder = Path(folder).resolve()
    src = (folder / "index.html").read_text(encoding="utf-8")
    html, missing = inline_assets(feed_placeholders(strip_email_only(src)), folder)

    desktop = lock_width(html, 600)
    (folder / "index-figma.html").write_text(desktop, encoding="utf-8")

    m = MEDIA_RE.search(html)
    mobile_rules = m.group(1) if m else ""
    # .wrap is 100% on mobile; force the 375 frame so it does not depend on the viewport
    mobile = lock_width(html, 375, mobile_rules + ".wrap{width:375px!important;max-width:375px!important;}")
    (folder / "index-figma-mobile.html").write_text(mobile, encoding="utf-8")

    kb = len(desktop.encode("utf-8")) // 1024
    print(f"{folder.name}: index-figma.html + index-figma-mobile.html ({kb} KB)")
    if not m:
        print(f"  ! {folder.name}: no max-width:599px block found, mobile file = desktop rules at 375px")
    for ref in missing:
        print(f"  ! missing file, not embedded: {ref}")


if __name__ == "__main__":
    base = Path(__file__).resolve().parent.parent
    for name in sys.argv[1:] or ["welcome-01", "welcome-02", "welcome-03"]:
        export(base / name if not Path(name).is_absolute() else name)
