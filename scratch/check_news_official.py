import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('scratch/official_sources/news.html', 'r', encoding='utf-8', errors='ignore') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("=== NEWS HEADINGS & IMGS ===")
for box in soup.find_all(['div', 'article'], class_=lambda c: c and any(k in str(c).lower() for k in ['news', 'blog', 'item', 'post', 'card'])):
    h = box.find(['h2', 'h3', 'h4', 'h5'])
    img = box.find('img')
    p = box.find('p')
    if h and img:
        print(f"TITLE: {h.get_text(strip=True)}")
        print(f"  IMG: {img.get('src')}")
        print(f"  DESC: {p.get_text(strip=True)[:120] if p else 'N/A'}...")

# Also print all images in news.html
print("\n=== ALL IMGS IN NEWS.HTML ===")
for img in soup.find_all('img'):
    print(img.get('src'), "| alt:", img.get('alt'))

