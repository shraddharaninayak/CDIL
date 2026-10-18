import os, sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

cards = soup.find_all('a', class_=lambda c: c and 'framer-zzaslx' in c)
print(f"Total framer-zzaslx cards: {len(cards)}")
for i, c in enumerate(cards):
    title = c.find(['h2', 'h3', 'h4'])
    badge = c.find('div', attrs={'data-framer-name': 'Status Badge'})
    loc = c.find_all('p')
    img = c.find('img')
    print(f"\n--- Card {i+1} ---")
    print("Href:", c.get('href'))
    print("Title:", title.get_text(strip=True) if title else "N/A")
    print("Badge:", badge.get_text(strip=True) if badge else "N/A")
    print("Img src:", img.get('src') if img else "N/A")
    print("Texts:", [p.get_text(strip=True) for p in loc[:4]])
