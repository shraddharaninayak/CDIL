from bs4 import BeautifulSoup

for f in ['pages/amara-whitfield.html', 'pages/about.html', 'pages/projects.html', 'index.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        soup = BeautifulSoup(fp.read(), 'html.parser')
        nav = soup.find('nav')
        print(f"\n{f}:")
        if nav:
            print("  nav class:", nav.get('class'))
            lang = nav.find('div', attrs={'aria-label': 'Language'})
            theme = nav.find('button', attrs={'aria-label': lambda a: a and 'mode' in a.lower()})
            print(f"  has lang: {bool(lang)}, has theme btn: {bool(theme)}")
        else:
            print("  No <nav> found!")
