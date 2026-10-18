import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/about.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

story = soup.find('div', attrs={'data-framer-name': 'Story'})
if story:
    print("--- Story Text ---")
    for p in story.find_all(['h2', 'h3', 'h4', 'p']):
        print(f"[{p.name}]: {p.get_text(strip=True)}")

values = soup.find('div', attrs={'data-framer-name': 'Values'})
if values:
    print("\n--- Values Text ---")
    for p in values.find_all(['h2', 'h3', 'h4', 'p']):
        print(f"[{p.name}]: {p.get_text(strip=True)}")
