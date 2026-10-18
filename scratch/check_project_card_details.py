import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    c = f.read()

# find each h3 title and its surrounding text
for proj in ['Laxmi Pushp', '3 Leaf Farmhouse', 'Watertouch', 'Amboli Van Veli', 'Teakwood Farm', 'River Ranch']:
    pos = c.find(proj)
    print(f"\n==========================================")
    print(f"Project: {proj} at {pos}")
    snippet = c[max(0, pos-400):min(len(c), pos+400)]
    # extract status badge
    badge = re.findall(r'data-framer-name="Status Badge"[^>]*>.*?<p[^>]*>([^<]+)</p>', snippet, re.DOTALL)
    # extract location
    loc = re.findall(r'dir="auto">([^<]+)</p>', snippet)
    print("Badge:", badge)
    print("Text parts:", loc[:6])
