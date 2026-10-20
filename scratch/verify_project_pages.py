import os, sys
from bs4 import BeautifulSoup

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

targets = ['ongoing-projects.html', 'completed-projects.html', 'upcoming-projects.html', 'projects.html']

for fname in targets:
    p = os.path.join('pages', fname)
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    
    print(f'=== Verifying {fname} ===')
    # Check 2.jpg
    if '2.jpg' in html:
        print(f'  [FAIL] 2.jpg still present in {fname}!')
    else:
        print(f'  [OK] 2.jpg completely gone from {fname}.')
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Check cards
    cards = soup.find_all('a', class_=lambda c: c and 'framer-zzaslx' in c)
    print(f'  [OK] Total project cards: {len(cards)}')
    
    # Check card images
    card_imgs = [c.find('img') for c in cards]
    valid_card_imgs = [img for img in card_imgs if img and img.get('src')]
    print(f'  [OK] Total project card images: {len(valid_card_imgs)}')
    for img in valid_card_imgs:
        print(f'     - Card img: {img.get("src")}')
    
    # Check navbar
    nav = soup.find('div', class_=lambda c: c and 'framer-wd06y0-container' in c)
    print(f'  [OK] Navbar present: {nav is not None}')
    
    # Check page head
    head = soup.find('div', attrs={'data-framer-name': 'Page Head'})
    print(f'  [OK] Page Head present: {head is not None}')
    
    # Check filter buttons
    filters = soup.find_all('button', class_='rf-c-R6malp')
    print(f'  [OK] Filter buttons present: {len(filters)}')
