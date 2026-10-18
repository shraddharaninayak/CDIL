import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/news-updates.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("--- Current News in pages/news-updates.html ---")
for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'p']):
    t = h.get_text(strip=True)
    if t and len(t) > 20 and not any(x in t.lower() for x in ['schedule', 'menu', 'contact']):
        print(f"[{h.name}]: {t[:120]}...")

imgs = soup.find_all('img')
print(f"\nImages in news-updates.html: {len(imgs)}")
for img in imgs:
    print(" ", img.get('src'))
