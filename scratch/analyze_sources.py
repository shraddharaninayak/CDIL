import os, sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

def analyze_page(name):
    print(f"\n==========================================")
    print(f"=== PAGE: {name.upper()} ===")
    with open(f"scratch/official_sources/{name}.html", "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Titles & Headings
    h1s = [h.get_text(strip=True) for h in soup.find_all('h1')]
    h2s = [h.get_text(strip=True) for h in soup.find_all('h2')]
    h3s = [h.get_text(strip=True) for h in soup.find_all('h3')]
    h4s = [h.get_text(strip=True) for h in soup.find_all('h4')]
    h5s = [h.get_text(strip=True) for h in soup.find_all('h5')]
    print(f"H1: {h1s}")
    print(f"H2: {h2s}")
    print(f"H3: {h3s}")
    print(f"H4: {h4s}")
    
    # Images
    imgs = []
    for img in soup.find_all('img'):
        src = img.get('src')
        alt = img.get('alt', '')
        if src and not any(x in src.lower() for x in ['logo', 'icon', 'envelope', 'phone']):
            imgs.append((src, alt))
    print(f"Key Images ({len(imgs)}):")
    for s, a in imgs[:8]:
        print(f"  {s} (alt: '{a}')")

for p in ['about', 'ongoing', 'completed', 'upcoming', 'gallery', 'news', 'blog']:
    analyze_page(p)
