from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

# Find language switcher elements like 'EN', 'ع', or similar
nav = soup.find('nav') or soup.find(class_=re.compile(r'nav', re.I))
# search text EN
en_nodes = soup.find_all(string=re.compile(r'\bEN\b'))
print(f"Found {len(en_nodes)} occurrences of EN:")
for n in en_nodes:
    p = n.parent
    print(f"  Parent: {p.name}, class={p.get('class')}, id={p.get('id')}")
    # print up to 4 parents
    ancestors = []
    curr = p
    for _ in range(5):
        if curr:
            ancestors.append(f"{curr.name}.{'.'.join(curr.get('class', []))}")
            curr = curr.parent
    print("   Chain:", " -> ".join(ancestors))

# Also search for the theme toggle icon (sun icon or svg)
svgs = soup.find_all('svg')
print(f"\nTotal svgs in index.html: {len(svgs)}")
for s in svgs:
    p = s.parent
    # check if parent is button or has aria label or class
    print(f"SVG parent: {p.name}, class={p.get('class')}, aria-label={p.get('aria-label')}, title={p.get('title')}")
