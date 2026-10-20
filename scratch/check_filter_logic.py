import os, sys
from bs4 import BeautifulSoup

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['ongoing-projects.html', 'completed-projects.html', 'upcoming-projects.html']:
    p = os.path.join('pages', fname)
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    btn_container = soup.find('div', class_='framer-dmy9z2-container')
    print(f'=== {fname} Filter buttons ===')
    if btn_container:
        btns = btn_container.find_all('button')
        for b in btns:
            print(f'  button: data-filter="{b.get("data-filter")}" aria-pressed="{b.get("aria-pressed")}" text="{b.get_text()}"')
    
    # Check if there is an inline filter script
    scripts = soup.find_all('script')
    for s in scripts:
        if s.string and 'filter' in s.string:
            print('  Filter script found:', s.string[:200])
