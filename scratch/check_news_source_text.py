import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('scratch/official_sources/news.html', 'r', encoding='utf-8', errors='ignore') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

for i in range(1, 10):
    img = soup.find('img', src=lambda s: s and f"n{i}.jpeg" in s)
    if img:
        parent = img.parent
        for _ in range(4):
            if parent and parent.parent:
                parent = parent.parent
        print(f"\n--- NEWS ITEM {i} (n{i}.jpeg) ---")
        print("Text:", parent.get_text(separator=' | ', strip=True)[:200])

