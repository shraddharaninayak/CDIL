import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

for name in ['ongoing', 'completed', 'upcoming']:
    print(f"\n=================== {name.upper()} ===================")
    with open(f"scratch/official_sources/{name}.html", 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Let's inspect elements inside the project section
    # Find all divs or elements with project cards
    for box in soup.find_all(['div', 'article'], class_=lambda c: c and any(k in str(c).lower() for k in ['project', 'item', 'col', 'portfolio'])):
        h = box.find(['h3', 'h4', 'h5'])
        if h and h.get_text(strip=True):
            img = box.find('img')
            a = box.find('a', href=True)
            p = box.find(['p', 'span'])
            # avoid duplicating parents
            if len(box.find_all(['h3', 'h4', 'h5'])) == 1:
                print(f"TITLE: {h.get_text(strip=True)}")
                print(f"  LOCATION/DESC: {p.get_text(strip=True) if p else 'N/A'}")
                print(f"  IMG: {img.get('src') if img else 'N/A'}")
                print(f"  HREF: {a.get('href') if a else 'N/A'}")
