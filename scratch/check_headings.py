import os, sys
from bs4 import BeautifulSoup

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['ongoing-projects.html', 'completed-projects.html', 'upcoming-projects.html', 'projects.html']:
    p = os.path.join('pages', fname)
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    page_head = soup.find('div', attrs={'data-framer-name': 'Page Head'})
    print(f'=== {fname} Page Head ===')
    if page_head:
        h1 = page_head.find('h1')
        p_tag = page_head.find('p', class_=lambda c: c and 'framer-styles-preset-1ii2ixo' in c)
        desc = page_head.find('div', class_=lambda c: c and 'framer-trmeqr' in c)
        print('  Eyebrow:', p_tag.get_text() if p_tag else 'None')
        print('  H1:', h1.get_text() if h1 else 'None')
        print('  Desc:', desc.get_text() if desc else 'None')
    else:
        print('  NO Page Head found!')
