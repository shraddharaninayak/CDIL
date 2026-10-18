import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('scratch/official_sources/news.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# find all divs containing n1.jpeg, n2.jpeg, etc.
for img in soup.find_all('img'):
    src = img.get('src')
    if 'n' in src and ('.jpeg' in src or '.jpg' in src):
        # find parent container
        parent = img.parent
        for _ in range(3):
            if parent and parent.parent:
                parent = parent.parent
        print(f"\n--- News item for {src} ---")
        print(parent.get_text(separator=' | ', strip=True) if parent else "N/A")
        a = parent.find('a') if parent else None
        print("Link:", a.get('href') if a else "N/A")
