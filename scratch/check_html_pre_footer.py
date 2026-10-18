import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    g = f.read()

body_pos = g.find('<body')
footer_pos = g.find('<div class="ssr-variant hidden-1lljya2 hidden-1sjjjhl">', body_pos)
print("footer_pos:", footer_pos)
print("1500 chars before footer in HTML body:")
print(g[footer_pos-1500:footer_pos])

