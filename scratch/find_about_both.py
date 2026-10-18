import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

def find_tag_boundaries(html, attr_search):
    idx = html.find(attr_search)
    if idx == -1:
        return None, None
    tag_start = html.rfind('<div', 0, idx)
    
    depth = 0
    i = tag_start
    while i < len(html):
        if html.startswith('<div', i) and (i + 4 == len(html) or html[i+4] in ' \t\r\n>/'):
            depth += 1
            i += 4
        elif html.startswith('</div>', i):
            depth -= 1
            if depth == 0:
                tag_end = i + len('</div>')
                return tag_start, tag_end
            i += len('</div>')
        else:
            i += 1
    return tag_start, None

for fname in ['index.html', 'pages/page.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    s, e = find_tag_boundaries(c, 'data-framer-name="About"')
    print(f"{fname}: s={s}, e={e}, size={e-s if s and e else 0}")
    if s and e:
        print("Starts with:", repr(c[s:s+120]))
        print("Ends with:", repr(c[e-80:e]))
        print("Before:", repr(c[max(0, s-100):s]))
        print("After:", repr(c[e:e+100]))
