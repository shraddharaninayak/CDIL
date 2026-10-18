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
    content = f.read()

# 1. Locate Banner
b_start, b_end = find_tag_boundaries(content, 'data-framer-name="Banner"')
assert b_start is not None and b_end is not None

banner_chunk = content[b_start:b_end]
print("Found Banner chunk:")
print(banner_chunk[:200])
print("...")
print(banner_chunk[-150:])

# Remove Banner from top
without_banner = content[:b_start] + content[b_end:]

# 2. Locate CTA in the modified content
cta_start, cta_end = find_tag_boundaries(without_banner, 'data-framer-name="CTA"')
assert cta_start is not None

# Prepare map section with appropriate spacing before CTA
# Ensure inline style adds padding-bottom for comfortable spacing before CTA
banner_moved = banner_chunk
if 'style=' in banner_chunk[:60]:
    pass
else:
    # add style="padding-bottom: 80px;" to the outer container
    banner_moved = banner_moved.replace(
        '<div class="framer-uaetb5" data-framer-name="Banner">',
        '<div class="framer-uaetb5" data-framer-name="Banner" style="padding-top: 0; padding-bottom: 80px;">'
    )

final_content = without_banner[:cta_start] + banner_moved + without_banner[cta_start:]

with open('pages/about.html', 'w', encoding='utf-8') as f:
    f.write(final_content)

print(f"Successfully moved map banner in pages/about.html! (Length: {len(content)} -> {len(final_content)})")
