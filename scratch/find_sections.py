from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

# Find all framer-name attributes on top-level sections
for div in soup.find_all('div', attrs={'data-framer-name': True}):
    fname = div.get('data-framer-name')
    if any(k in fname.lower() for k in ['project', 'residence', 'residences', 'properties', 'cards', 'listing']):
        print(f"Section: {fname}, id={div.get('id')}, class={div.get('class')}")

# Also check for headings with "Our Projects"
for h2 in soup.find_all(['h2', 'h1', 'p']):
    t = h2.get_text(strip=True)
    if 'Our Projects' in t and h2.parent.get('data-framer-name') != 'Hero Text':
        print(f"Heading element: {h2.name}, text='{t.encode('ascii', 'ignore').decode('ascii')}', parent: {h2.parent.get('data-framer-name')}, grand: {h2.parent.parent.get('data-framer-name') if h2.parent.parent else ''}")
