import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = 194330
snippet = c[pos-200:pos+3500]

print("=== ALL OCCURRENCES OF 'View →' ===")
for m in re.finditer(r'<p[^>]*>View\s*→</p>', snippet):
    print("Found 'View →' at offset:", m.start())

# Also let's inspect all slides inside framer-60zqrq
m_wrap = re.search(r'<div class="framer-60zqrq"[^>]*>(.*?)</div></div></div>', snippet, re.DOTALL)
if m_wrap:
    print("\nInside framer-60zqrq length:", len(m_wrap.group(1)))
    # find all h3 titles in here
    titles = re.findall(r'<h3[^>]*>(.*?)</h3>', m_wrap.group(1))
    print("Titles:", titles)
    # find all locations
    locs = re.findall(r'<p class="framer-text framer-styles-preset-159ll4e"[^>]*>(.*?)</p>', m_wrap.group(1))
    print("Locations:", locs)
    # find all view links
    views = re.findall(r'View\s*→', m_wrap.group(1))
    print("View links count:", len(views))

