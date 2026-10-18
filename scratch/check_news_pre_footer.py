import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/news-updates.html', 'r', encoding='utf-8') as f:
    n = f.read()

body_pos = n.find('<body')
footer_pos = n.find('<div class="ssr-variant hidden-1lljya2 hidden-1sjjjhl">', body_pos)
print("footer_pos in news:", footer_pos)
print("1500 chars before footer in news:")
print(n[footer_pos-1500:footer_pos])

