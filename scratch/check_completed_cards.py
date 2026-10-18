import urllib.request
from bs4 import BeautifulSoup

for page in ['completed-project.html', 'upcoming-project.html']:
    url = f'https://cdilrealestate.com/{page}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        soup = BeautifulSoup(resp.read().decode('utf-8', errors='ignore'), 'html.parser')
        print(f"=== {page} ===")
        for card in soup.find_all('div', class_=lambda c: c and ('project' in c or 'item' in c or 'col' in c)):
            h = card.find(['h3', 'h4', 'h5'])
            if h and len(h.get_text(strip=True)) < 50:
                p_text = " ".join([p.get_text(strip=True) for p in card.find_all(['p', 'span', 'li', 'a'])])
                # encode ascii ignore
                print(f"  {h.get_text(strip=True)} -> {p_text.encode('ascii', 'ignore').decode('ascii')}")
