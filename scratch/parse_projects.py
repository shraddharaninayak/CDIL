import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

def parse_projects(name):
    print(f"\n==========================================")
    print(f"=== PROJECTS: {name.upper()} ===")
    with open(f"scratch/official_sources/{name}.html", "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # find cards or project items
    for h4 in soup.find_all('h4'):
        title = h4.get_text(strip=True)
        if any(x in title.lower() for x in ['cdil', 'our project', 'location']):
            continue
        # find closest parent or container
        parent = h4.parent
        for _ in range(3):
            if parent and parent.parent:
                parent = parent.parent
        # find img
        img = parent.find('img') if parent else None
        img_src = img.get('src') if img else None
        # find link
        link = parent.find('a') if parent else None
        link_href = link.get('href') if link else None
        # text
        text = parent.get_text(separator=' | ', strip=True) if parent else ""
        print(f"Project: {title}")
        print(f"  Img: {img_src}")
        print(f"  Link: {link_href}")
        print(f"  Snippet: {text[:200]}")

for p in ['ongoing', 'completed', 'upcoming']:
    parse_projects(p)
