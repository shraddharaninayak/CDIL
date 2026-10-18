import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    g = f.read()

pos_footer = g.find('<div class="ssr-variant hidden-1lljya2 hidden-1sjjjhl">')
print("500 chars before footer in gallery.html:")
print(g[pos_footer-500:pos_footer])

