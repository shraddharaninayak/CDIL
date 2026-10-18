import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('scratch/official_sources/news.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("All text in news.html:")
for p in soup.find_all(['h2', 'h3', 'h4', 'h5', 'p', 'a']):
    t = p.get_text(strip=True)
    if t and len(t) > 5 and not any(x in t.lower() for x in ['cdil', 'location', 'phone', 'email', 'home', 'about', 'project']):
        print(f"[{p.name}]: {t}")

imgs = soup.find_all('img')
print("\nImages in news.html:")
for img in imgs:
    print(img.get('src'))
