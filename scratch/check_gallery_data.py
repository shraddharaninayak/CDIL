import os, sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

print("=== OFFICIAL GALLERY HTML IMAGES ===")
with open('scratch/official_sources/gallery.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

items = []
for box in soup.find_all(['div', 'a', 'li'], class_=lambda c: c and any(k in str(c).lower() for k in ['gallery', 'portfolio', 'item', 'grid'])):
    img = box.find('img')
    if img and img.get('src'):
        src = img.get('src')
        alt = img.get('alt', '')
        # find category or title
        cat = box.get('class', [])
        parent_txt = box.get_text(separator=' ', strip=True)
        items.append((src, alt, cat, parent_txt[:50]))

print(f"Total potential gallery elements: {len(items)}")
# Deduplicate by src
unique = {}
for src, alt, cat, txt in items:
    if src not in unique:
        unique[src] = (alt, cat, txt)

print(f"Unique images in official gallery: {len(unique)}")
for src, (alt, cat, txt) in unique.items():
    print(f"  Src: {src} | Alt: {alt} | Classes: {cat}")

print("\n=== CURRENT PAGES/GALLERY.HTML IMAGES ===")
with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    soup_curr = BeautifulSoup(f.read(), 'html.parser')

curr_imgs = soup_curr.find_all('img')
print(f"Total images in pages/gallery.html: {len(curr_imgs)}")
for im in curr_imgs[:10]:
    print("  Src:", im.get('src'), "Alt:", im.get('alt'))

