from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

# Find headings or sections with "Our Projects" or "Projects"
for el in soup.find_all(['section', 'div', 'h2', 'h1']):
    txt = el.get_text(strip=True)
    if 'Our Projects' in txt or 'projects' in txt.lower():
        if el.name in ['h2', 'h1'] or (el.get('id') or el.get('data-framer-name')):
            print(f"Tag: {el.name}, id: {el.get('id')}, class: {el.get('class')}, framer-name: {el.get('data-framer-name')}, text: {txt[:50]}")

# Let's search where project cards are located
for h in soup.find_all('h3'):
    t = h.get_text(strip=True)
    if any(p in t for p in ['Amboli', '3 Leaf', 'Mountain Bliss', 'Watertouch', 'Teakwood', 'Laxmi Pushp']):
        # climb parents to find container with id or section
        p_el = h
        chain = []
        for _ in range(8):
            if p_el:
                chain.append(f"{p_el.name}(id={p_el.get('id')}, name={p_el.get('data-framer-name')}, class={p_el.get('class')})")
                p_el = p_el.parent
        print(f"Project card '{t}': {' -> '.join(chain)}")
        break
