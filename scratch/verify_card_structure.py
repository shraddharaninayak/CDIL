import os, sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

for filepath in ['index.html', 'pages/page.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    soup = BeautifulSoup(c, 'html.parser')
    
    # check card existence
    card = soup.find('div', class_=lambda cl: cl and 'framer-gtXe7' in cl)
    print(f"\n=== {filepath} ===")
    print(f"Card found: {card is not None}")
    if card:
        titles = [h.get_text() for h in card.find_all(['h2', 'h3', 'h4'])]
        texts = [p.get_text() for p in card.find_all('p')]
        print(f"Titles in card: {titles}")
        print(f"Paragraphs in card: {texts}")
        print(f"'View' in card: {'View' in card.get_text()}")
        indicators = card.find('div', class_=lambda cl: cl and 'framer-1wgasjr' in cl)
        print(f"Slide indicators present: {indicators is not None}")

    # check div balance
    open_divs = len(re.findall(r'<div\b', c))
    close_divs = len(re.findall(r'</div>', c))
    print(f"Div balance: open={open_divs}, close={close_divs}, diff={open_divs - close_divs}")

