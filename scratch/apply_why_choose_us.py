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

with open("scratch/why_choose_us_component.html", "r", encoding="utf-8") as f:
    component_html = f.read().strip()

for fname in ['index.html', 'pages/page.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    s, e = find_tag_boundaries(content, 'data-framer-name="About"')
    assert s is not None and e is not None, f"Could not find About section in {fname}"
    
    # Replace About section with Why Choose Us component
    new_content = content[:s] + component_html + content[e:]
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully replaced About section with Why Choose Us in {fname} ({len(content)} -> {len(new_content)} bytes)")
