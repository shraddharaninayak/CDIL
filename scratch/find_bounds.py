import os
import sys

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
        content = f.read()
    s, e = find_tag_boundaries(content, 'data-framer-name="Services"')
    print(f"{fname}: s={s}, e={e}, size={e-s if s and e else 0}")
    if s and e:
        print("Start snippet:", repr(content[s:s+120]))
        print("End snippet:", repr(content[e-80:e]))
        # also print what's immediately before and after
        print("Before snippet:", repr(content[max(0, s-100):s]))
        print("After snippet:", repr(content[e:e+100]))
