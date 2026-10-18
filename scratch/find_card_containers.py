import os, sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

# find each project name and print the ancestor structure
names = ['Laxmi Pushp', '3 Leaf Farmhouse', 'Watertouch', 'Amboli Van Veli', 'Teakwood Farm', 'River Ranch']

for name in names:
    pos = html.find(name)
    print(f"\n================ {name} ================")
    # Look back 800 chars
    prefix = html[max(0, pos-800):pos]
    # find all '<div class="framer-' in prefix
    matches = list(re.finditer(r'<div\s+class="([^"]+)"([^>]*)>', prefix))
    if matches:
        for m in matches[-3:]:
            print("ANCESTOR DIV class:", m.group(1), "attrs:", m.group(2))

