import os, sys
from bs4 import BeautifulSoup

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['ongoing-projects.html', 'completed-projects.html', 'upcoming-projects.html', 'projects.html']:
    p = os.path.join('pages', fname)
    if not os.path.exists(p):
        continue
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    print(f'================ {fname} ================')
    imgs = soup.find_all('img')
    print(f'Total <img> tags: {len(imgs)}')
    for i, img in enumerate(imgs):
        src = img.get('src', '')
        alt = img.get('alt', '')
        parent_fn = img.parent.get('data-framer-name', '') if img.parent else ''
        grandparent_fn = img.parent.parent.get('data-framer-name', '') if img.parent and img.parent.parent else ''
        print(f'  [{i}] src="{src}" | alt="{alt}" | parent_framer_name="{parent_fn}" / "{grandparent_fn}"')
