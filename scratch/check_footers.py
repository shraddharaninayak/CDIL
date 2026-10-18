import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    g = f.read()

with open('pages/news-updates.html', 'r', encoding='utf-8') as f:
    n = f.read()

# Let's see where the footer starts
footer_g = g[g.find('<div class="ssr-variant hidden-1lljya2 hidden-1sjjjhl">'):]
footer_n = n[n.find('<div class="ssr-variant hidden-1lljya2 hidden-1sjjjhl">'):]

print("footer_g len:", len(footer_g), "footer_n len:", len(footer_n))
print("Are footers identical?:", footer_g == footer_n)

