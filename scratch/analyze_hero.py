import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

line697 = content.splitlines()[696]

soup = BeautifulSoup(line697, 'html.parser')

rh = soup.find(string=re.compile(r'Rare homes'))
if rh:
    print("Found text:", rh)
    p = rh.parent
    for i in range(8):
        if p:
            print(f"Parent {i}: tag={p.name}, class={p.get('class')}, id={p.get('id')}")
            p = p.parent

card = soup.find(class_=re.compile(r'framer-gtXe7'))
if card:
    print("\n--- Card HTML ---")
    print(card.prettify()[:1500])
