import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = soup.find_all('a', attrs={'data-cdil-project': True})
print("Total data-cdil-project cards:", len(cards))
for c in cards:
    title = c.find('h3')
    badge = c.find('p', class_=lambda cl: cl and 'framer-styles-preset-11shj4z' in str(cl))
    print(f"  [{c.get('data-cdil-status')}] {c.get('data-cdil-project')} -> {title.get_text() if title else 'N/A'} (Badge: {badge.get_text() if badge else 'N/A'}, Link: {c.get('href')})")

cta = soup.find('div', attrs={'data-framer-name': 'CTA'})
footer = soup.find('footer')
print("CTA present:", cta is not None)
print("Footer present:", footer is not None)

