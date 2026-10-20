import os, sys
from bs4 import BeautifulSoup

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

with open('pages/ongoing-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
main = soup.find('div', id='main')

for i, child in enumerate(main.children):
    if child.name:
        fn = child.get('data-framer-name', '')
        cls = child.get('class', '')
        print(f'Child #{i}: <{child.name} class="{cls}" data-framer-name="{fn}"> (len={len(str(child))})')
