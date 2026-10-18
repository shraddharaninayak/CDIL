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
        content = f.read()
    s, e = find_tag_boundaries(content, 'data-framer-name="Services"')
    if s is not None and e is not None:
        removed_content = content[s:e]
        print(f"Removing {len(removed_content)} chars from {fname}...")
        # Verify content has 'Complete Real Estate Solutions' or 'Farmhouse Plots'
        assert 'Complete Real Estate Solutions' in removed_content or 'Services' in removed_content
        new_content = content[:s] + content[e:]
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully removed Services section from {fname}.")
    else:
        print(f"Warning: Services section not found in {fname}")

