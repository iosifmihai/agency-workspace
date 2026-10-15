import re,sys,base64,mimetypes,pathlib
d=pathlib.Path(sys.argv[1]); h=(d/'index.html').read_text(encoding='utf-8')
sample={'FIRST_NAME':'Andreea','ORDER_PRODUCT_NAME':'Classic Pankees','ORDER_PRODUCT_IMAGE':'../new-customer-02/packshots/pr-classic-front.jpg','UNSUBSCRIBE_URL':'#'}
h=re.sub(r'\{\{([A-Z_]+)\}\}',lambda m:sample.get(m.group(1),'#'),h)
h=re.sub(r'<!--\[if !mso\]><!--( --)?>|<!--<!\[endif\]-->','',h)  # unwrap non-Outlook parts first
h=re.sub(r'(?s)<!--\[if [^\]]*\]>.*?<!\[endif\]-->','',h)      # then drop Outlook-only VML
h=re.sub(r'(?s)<!--(?!\[).*?-->','',h)                          # notes/markers
# Figma importer ignores the align="" attribute: copy it into CSS (cells -> text-align, tables -> auto margins)
def _addstyle(tag,css):
    return re.sub(r'style="',('style="'+css),tag,1) if 'style="' in tag else tag[:-1]+' style="%s">'%css
h=re.sub(r'<(td|th|div|p)\b[^>]*\balign="(center|right|left)"[^>]*>',lambda m:_addstyle(m.group(0),'text-align:%s;'%m.group(2)),h)
h=re.sub(r'<table\b[^>]*\balign="center"[^>]*>',lambda m:_addstyle(m.group(0),'margin-left:auto;margin-right:auto;'),h)
# pill buttons centre text via line-height, which Figma drops: use flex centring with an explicit height
def _btn(m):
    t=m.group(0); lh=re.search(r'line-height:(\d+)px',t)
    if not lh: return t
    return t.replace('display:inline-block;','display:inline-flex;align-items:center;justify-content:center;height:%spx;'%lh.group(1))
h=re.sub(r'<a\b[^>]*display:inline-block;[^>]*>',_btn,h)
def inline(m):
    p=(d/m.group(2)).resolve()
    if not p.exists(): return m.group(0)
    mt=mimetypes.guess_type(str(p))[0] or ('font/woff2' if p.suffix=='.woff2' else 'font/woff')
    return m.group(1)+'data:%s;base64,%s'%(mt,base64.b64encode(p.read_bytes()).decode())+m.group(3)
h=re.sub(r'''(src=")([^"#][^"]*\.(?:png|jpe?g|gif))(")''',inline,h)
h=re.sub(r'''(url\(')([^']+\.woff2?)('\))''',inline,h)
(d/'figma.html').write_text(h,encoding='utf-8'); print(d, len(h)//1024,'KB')
