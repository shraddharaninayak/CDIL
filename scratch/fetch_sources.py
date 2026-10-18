import urllib.request, os, sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

os.makedirs("scratch/official_sources", exist_ok=True)

sources = {
    "about": "https://cdilrealestate.com/about.html",
    "ongoing": "https://cdilrealestate.com/outgoing-project.html",
    "completed": "https://cdilrealestate.com/completed-project.html",
    "upcoming": "https://cdilrealestate.com/upcoming-project.html",
    "gallery": "https://cdilrealestate.com/gallery.html",
    "news": "https://cdilrealestate.com/news-updates.html",
    "blog": "https://cdilrealestate.com/blog.html"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for key, url in sources.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw_html = resp.read().decode('utf-8', errors='ignore')
        
        with open(f"scratch/official_sources/{key}.html", "w", encoding="utf-8") as f:
            f.write(raw_html)
        
        soup = BeautifulSoup(raw_html, 'html.parser')
        # Extract main text content
        text = soup.get_text(separator='\n', strip=True)
        with open(f"scratch/official_sources/{key}_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
            
        print(f"Fetched {key}: {len(raw_html)} bytes HTML, {len(text)} chars text")
    except Exception as e:
        print(f"Error fetching {key} ({url}): {e}")

print("Fetch completed.")
