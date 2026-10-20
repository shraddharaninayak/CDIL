import os, sys
from bs4 import BeautifulSoup

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['ongoing-projects.html', 'completed-projects.html', 'upcoming-projects.html', 'projects.html']:
    p = os.path.join('pages', fname)
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    cta = soup.find('div', attrs={'data-framer-name': 'CTA'})
    if cta:
        print(f'=== {fname} ===')
        print(f'CTA found, length: {len(str(cta))}')
        print(str(cta)[:300] + ' ... ' + str(cta)[-150:])
    else:
        print(f'=== {fname}: NO CTA found! ===')
