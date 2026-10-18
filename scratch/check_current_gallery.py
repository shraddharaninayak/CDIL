import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("--- Current Gallery in pages/gallery.html ---")
imgs = soup.find_all('img')
print(f"Total img tags in gallery.html: {len(imgs)}")
for i, img in enumerate(imgs):
    print(f"Img {i+1}: {img.get('src')} | alt: '{img.get('alt')}'")
