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

with open('pages/about.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Boundaries of Banner
b_start, b_end = find_tag_boundaries(c, 'data-framer-name="Banner"')
print(f"Banner: start={b_start}, end={b_end}, len={b_end - b_start}")
print("Banner snippet:")
print(repr(c[b_start:b_start+200]))
print("...")
print(repr(c[b_end-100:b_end]))

# 2. Before and After Banner
print("\nBefore Banner:")
print(repr(c[max(0, b_start-150):b_start]))
print("\nAfter Banner:")
print(repr(c[b_end:b_end+150]))

# 3. Boundaries of CTA
cta_start, cta_end = find_tag_boundaries(c, 'data-framer-name="CTA"')
print(f"\nCTA: start={cta_start}, end={cta_end}")
print("\nBefore CTA:")
print(repr(c[max(0, cta_start-150):cta_start]))
