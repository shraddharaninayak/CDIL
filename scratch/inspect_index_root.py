import os, sys
from bs4 import BeautifulSoup

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
root = soup.find('div', attrs={'data-framer-root': True})
if root:
    print('=== index.html root children ===')
    for i, child in enumerate(root.children):
        if child.name:
            fn = child.get('data-framer-name', '')
            cls = ' '.join(child.get('class', []))
            print(f'#{i}: <{child.name} class="{cls}" data-framer-name="{fn}"> (len={len(str(child))})')
