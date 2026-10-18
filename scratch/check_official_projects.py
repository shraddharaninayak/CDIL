import os, sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

def check_source(fname):
    path = os.path.join('scratch', 'official_sources', fname)
    if not os.path.exists(path):
        print(f"Missing {path}")
        return
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    print(f"\n=================== {fname} ===================")
    for h in soup.find_all(['h2', 'h3', 'h4', 'h5']):
        txt = h.get_text(strip=True)
        if txt and len(txt) < 80:
            print("HEADING:", txt)
    # also print all img tags with their src and alt
    for img in soup.find_all('img'):
        print("IMG:", img.get('src'), "| alt:", img.get('alt'))
    # also print paragraphs or cards
    for p in soup.find_all('p'):
        pt = p.get_text(strip=True)
        if len(pt) > 30 and len(pt) < 300:
            print("P:", pt[:100], "...")

check_source('outgoing-project.html')
check_source('completed-project.html')
check_source('upcoming-project.html')
