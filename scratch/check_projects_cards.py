import os, sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    c = f.read()

soup = BeautifulSoup(c, 'html.parser')

# find filter links
filters = []
for a in soup.find_all('a'):
    if 'projects.html' in str(a.get('href')):
        filters.append((a.get_text(strip=True), a.get('href')))

print("Filter links in projects.html:", filters[:10])

# find project cards
print("\n--- Project Cards in projects.html ---")
cards = soup.find_all('div', attrs={'data-framer-name': 'Card'})
print(f"Cards found: {len(cards)}")
for i, card in enumerate(cards):
    title = card.find(['h3', 'h4', 'h2'])
    loc = card.find('p')
    a = card.find('a')
    img = card.find('img')
    print(f"Card {i+1}:")
    print(f"  Title: {title.get_text(strip=True) if title else 'N/A'}")
    print(f"  Loc/Text: {loc.get_text(strip=True) if loc else 'N/A'}")
    print(f"  Img: {img.get('src') if img else 'N/A'}")
    print(f"  Link: {a.get('href') if a else 'N/A'}")
