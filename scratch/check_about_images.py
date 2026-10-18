import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/about.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("All images in pages/about.html:")
for img in soup.find_all('img'):
    print("  src:", img.get('src'), "| alt:", img.get('alt'))

