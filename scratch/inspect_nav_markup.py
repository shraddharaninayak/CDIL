from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

btn = soup.find('button', attrs={'aria-label': 'Switch to light mode'})
if btn:
    # let's climb up to navbar container
    p = btn
    while p and not (p.get('class') and any('nav' in c.lower() for c in p.get('class'))):
        p = p.parent
    if not p:
        p = btn.parent.parent.parent.parent

    print(f"Container: {p.name}, class={p.get('class')}, id={p.get('id')}")
    # print prettified container
    print(p.prettify()[:3000])
