import urllib.request
from bs4 import BeautifulSoup

for page in ['outgoing-project.html', 'completed-project.html', 'upcoming-project.html', 'index.html']:
    url = f'https://cdilrealestate.com/{page}' if page != 'index.html' else 'https://cdilrealestate.com/'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            soup = BeautifulSoup(resp.read().decode('utf-8', errors='ignore'), 'html.parser')
            print(f"=== {page} ===")
            for h in soup.find_all(['h2', 'h3', 'h4', 'h5']):
                t = h.get_text(strip=True)
                if t and len(t) < 60:
                    # check if parent or sibling has location
                    parent_text = " | ".join([s for s in h.parent.stripped_strings if s != t])
                    print(f"  {t} -> {parent_text[:100]}")
    except Exception as e:
        print(f"Error {page}: {e}")
