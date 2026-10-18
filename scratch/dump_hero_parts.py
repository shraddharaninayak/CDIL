import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

line697 = content.splitlines()[696]
soup = BeautifulSoup(line697, 'html.parser')

card = soup.find(class_=re.compile(r'framer-gtXe7'))
with open('scratch/card_full.html', 'w', encoding='utf-8') as cf:
    if card:
        cf.write(card.prettify())

# Let's see the hero container and background images
# Look for where images/ZiuHJRK3VDqMlK0bXLemGXGx8o.jpg is placed
hero_bg = soup.find('img', {'src': re.compile(r'ZiuHJRK3VDqMlK0bXLemGXGx8o')})
if hero_bg:
    # let's write parent 3 levels up
    p = hero_bg
    for _ in range(4):
        if p.parent:
            p = p.parent
    with open('scratch/hero_bg_context.html', 'w', encoding='utf-8') as hf:
        hf.write(p.prettify())

print("Dumped card and hero_bg_context")
