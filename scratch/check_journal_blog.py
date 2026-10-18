import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

for fpath in ['pages/journal.html', 'pages/blog.html']:
    exists = os.path.exists(fpath)
    print(f"\n--- Checking {fpath} (exists={exists}) ---")
    if exists:
        with open(fpath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        h1s = [h.get_text(strip=True) for h in soup.find_all('h1')]
        h2s = [h.get_text(strip=True) for h in soup.find_all('h2')]
        h3s = [h.get_text(strip=True) for h in soup.find_all('h3')]
        print("H1:", h1s)
        print("H2:", h2s[:5])
        print("H3:", h3s[:6])
