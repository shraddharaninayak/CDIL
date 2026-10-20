import os, sys
from bs4 import BeautifulSoup

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

with open('pages/ongoing-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
main = soup.find('div', id='main')
children = [c for c in main.children if c.name]

print('=== CHILD #3 (CTA) ===')
print(str(children[2])[:500])

print('\n=== CHILD #4 ===')
print(str(children[3])[:1000])

print('\n=== CHILD #5 (Navbar) ===')
print(str(children[4])[:500])
