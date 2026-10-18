import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/about.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Count occurrences of "Banner"
banner_count = c.count('data-framer-name="Banner"')
print(f"Banner count (Expected 1): {banner_count}")

# 2. Check <div> tag balance
open_divs = len(re.findall(r'<div\b', c))
close_divs = len(re.findall(r'</div>', c))
print(f"<div> balance: open={open_divs}, close={close_divs}, diff={open_divs - close_divs}")

# 3. List top-level section names in order
section_matches = [m.start() for m in re.finditer(r'data-framer-name="([^"]+)"', c)]
sections_ordered = []
for m in re.finditer(r'<div[^>]*data-framer-name="([^"]+)"', c):
    name = m.group(1)
    if name in ['Page Head', 'Story', 'Values', 'Banner', 'CTA']:
        sections_ordered.append(name)

print("Section sequence:")
for idx, s in enumerate(sections_ordered):
    print(f"  {idx+1}. {s}")

# 4. Check context around Banner and CTA
banner_idx = c.find('data-framer-name="Banner"')
cta_idx = c.find('data-framer-name="CTA"')
print(f"\nBanner index: {banner_idx}")
print(f"CTA index: {cta_idx}")
print(f"Characters between Banner and CTA: {cta_idx - banner_idx}")
assert banner_idx < cta_idx, "Banner must be before CTA"

# Context between Values and Banner
print("\nContext before Banner (end of Values):")
print(repr(c[banner_idx-150:banner_idx]))

# Context between Banner and CTA
banner_end = c.find('</div></div></div></div>', banner_idx) + len('</div></div></div></div>')
print("\nContext between Banner and CTA:")
print(repr(c[banner_end:banner_end+150]))
