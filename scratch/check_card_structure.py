import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

def get_cards(filename):
    print(f"\n*** CARDS IN {filename} ***")
    with open(f"scratch/official_sources/{filename}.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # find all project blocks
    # usually .project-item or .col-...
    for div in soup.find_all('div', class_=lambda c: c and any(k in str(c).lower() for k in ['project', 'portfolio', 'item', 'product'])):
        h4 = div.find(['h4', 'h3', 'h5'])
        img = div.find('img')
        a = div.find('a')
        p = div.find('p')
        if h4 and img:
            print(f"Title: {h4.get_text(strip=True)}")
            print(f"Location/Sub: {p.get_text(strip=True) if p else 'N/A'}")
            print(f"Img: {img.get('src')}")
            print(f"Link: {a.get('href') if a else 'N/A'}")
            print("---")

for f in ['ongoing', 'completed', 'upcoming']:
    get_cards(f)
