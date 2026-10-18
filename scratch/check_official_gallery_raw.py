import os, sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('scratch/official_sources/gallery.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
imgs = soup.find_all('img')
print("Total imgs in scratch/official_sources/gallery.html:", len(imgs))
for i, img in enumerate(imgs):
    print(f"{i+1}: {img.get('src')} | alt: {img.get('alt')}")

# Also check if images are in <a> tags or background-image
links = soup.find_all('a', href=lambda h: h and any(ext in str(h).lower() for ext in ['.jpg', '.jpeg', '.png', '.webp']))
print("Image links in <a>:", len(links))
for a in links:
    print("  Link:", a.get('href'))

