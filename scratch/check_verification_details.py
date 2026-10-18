import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    g = f.read()
print("cdil-gal-card in gallery.html:", g.count('cdil-gal-card'))

with open('pages/news-updates.html', 'r', encoding='utf-8') as f:
    n = f.read()
print("cdil-news-card in news-updates.html:", n.count('cdil-news-card'))

with open('pages/about.html', 'r', encoding='utf-8') as f:
    a = f.read()
print("map in about.html:", [m for m in ['map', 'Map', 'location_map', 'Location Map'] if m in a])
print("Founder or Kute in about.html:", [m for m in ['Kute', 'founder', 'Founder', '16'] if m in a])

