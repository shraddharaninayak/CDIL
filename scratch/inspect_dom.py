import os, sys
from bs4 import BeautifulSoup

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

with open('pages/ongoing-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

body = soup.find('body')
print('=== Direct children of body ===')
for child in body.children:
    if child.name:
        cls = child.get('class', '')
        id_ = child.get('id', '')
        print(f'<{child.name} id="{id_}" class="{cls}">')

main = soup.find('div', id='main')
if main:
    print('\n=== Direct children of #main ===')
    for child in main.children:
        if child.name:
            cls = child.get('class', '')
            id_ = child.get('id', '')
            fn = child.get('data-framer-name', '')
            print(f'<{child.name} id="{id_}" class="{cls}" data-framer-name="{fn}">')

root = main.find('div', attrs={'data-framer-root': True}) if main else None
if root:
    print('\n=== Direct children of data-framer-root ===')
    for child in root.children:
        if child.name:
            cls = child.get('class', '')
            id_ = child.get('id', '')
            fn = child.get('data-framer-name', '')
            print(f'<{child.name} id="{id_}" class="{cls}" data-framer-name="{fn}">')
