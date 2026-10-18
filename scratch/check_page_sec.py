from bs4 import BeautifulSoup

with open('pages/page.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

sec = soup.find('div', class_='framer-1vsy57f')
print("page.html framer-1vsy57f exists:", bool(sec))
btn = soup.find('a', attrs={'data-framer-name': 'View Projects Button'})
print("page.html View Projects Button exists:", bool(btn))
if btn:
    print("  href:", btn.get('href'))
