import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/about.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("--- Headings in pages/about.html ---")
for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'p']):
    t = h.get_text(strip=True)
    if t and len(t) > 15:
        print(f"[{h.name}]: {t[:100]}...")
