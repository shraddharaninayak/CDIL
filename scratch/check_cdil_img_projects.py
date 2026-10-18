# Let's search CDIL website and any online references for the palm trees or the sunset lawn
# Could it be "3 Leaf Farmhouse" or "Amboli Van-Veli" or "Mountain Bliss" or "Laxmi Pushp"?
import urllib.request
import re

# Let's fetch all project pages from cdilrealestate.com
for p in ['outgoing-project.html', 'completed-project.html', 'upcoming-project.html']:
    url = f'https://cdilrealestate.com/{p}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print(f"=== {p} ===")
        # find all images and text around them
        matches = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"][^>]*>.*?(?:<h3>|<h4>)(.*?)(?:</h3>|</h4>)', html, re.DOTALL)
        for m in matches:
            print(" ", m[0], "->", m[1].strip())
