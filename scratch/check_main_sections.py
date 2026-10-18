from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8-sig') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

main = soup.find('div', id='main')
if main:
    print("Main classes:", main.get('class'))
    # inspect sections inside main
    for child in main.find_all('div', recursive=False):
        print(f"Child: class={child.get('class')}, framer-name={child.get('data-framer-name')}, style={child.get('style')}")

# Also check pages/about.html
with open('pages/about.html', 'r', encoding='utf-8-sig') as f:
    soup_about = BeautifulSoup(f.read(), 'html.parser')
main_about = soup_about.find('div', id='main')
if main_about:
    print("\nAbout Main classes:", main_about.get('class'))
