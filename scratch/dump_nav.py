from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

btn = soup.find('button', attrs={'aria-label': 'Switch to light mode'})
if btn:
    p = btn
    while p and p.name != 'nav':
        p = p.parent

    with open('scratch/nav_full.html', 'w', encoding='utf-8') as nf:
        nf.write(p.prettify())
    print("Dumped nav to scratch/nav_full.html")
