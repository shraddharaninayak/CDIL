from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

sec = soup.find('div', class_='framer-1vsy57f')
if sec:
    print(f"Found framer-1vsy57f:")
    print(f"  id: {sec.get('id')}")
    print(f"  data-framer-name: {sec.get('data-framer-name')}")
    # find all headings inside
    for h in sec.find_all(['h2', 'h3', 'p']):
        txt = h.get_text(strip=True).encode('ascii', 'ignore').decode('ascii')
        if len(txt) < 50 and txt:
            print(f"    {h.name}: {txt}")

# Check the View Projects button in the Hero
btn = soup.find('a', attrs={'data-framer-name': 'View Projects Button'})
if btn:
    print("\nView Projects Button:")
    print(f"  tag: {btn.name}, href: {btn.get('href')}, class: {btn.get('class')}")
