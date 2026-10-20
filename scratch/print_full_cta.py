import os, sys
from bs4 import BeautifulSoup

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

with open('pages/ongoing-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
cta = soup.find('div', attrs={'data-framer-name': 'CTA'})
print(str(cta))
