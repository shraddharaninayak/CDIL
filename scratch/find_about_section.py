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

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

s, e = find_tag_boundaries(c, 'data-framer-name="About"')
print(f"About section in index.html: start={s}, end={e}, len={e-s}")
print("Opening:")
print(repr(c[s:s+250]))
print("...")
print("Closing:")
print(repr(c[e-250:e]))

# Check what comes before and after
print("\nBefore About:")
print(repr(c[max(0, s-150):s]))
print("\nAfter About:")
print(repr(c[e:e+150]))
