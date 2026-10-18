import os, sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/journal.html', 'r', encoding='utf-8') as f:
    c = f.read()

soup = BeautifulSoup(c, 'html.parser')
body = soup.find('body')

print("All headings in journal.html body:")
for h in body.find_all(['h1', 'h2', 'h3', 'h4']):
    print(f"  {h.name}: {h.get_text(strip=True)[:80]}")

print("\nAll links to articles or posts:")
for a in body.find_all('a'):
    href = a.get('href', '')
    if any(k in href for k in ['.html', 'post', 'blog', 'journal']):
        print(f"  Href: {href} | Text: {a.get_text(strip=True)[:50]}")

