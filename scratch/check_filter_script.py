import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'/\* CDIL Interactive Project Status Filter \*/.*?</script>', html, re.DOTALL)
if m:
    print("Filter script:")
    print(m.group(0))

# Also check data-cdil-project attributes
print("\nCards with data-cdil-project:")
for card in re.finditer(r'<div[^>]*data-cdil-project="([^"]+)"[^>]*>', html):
    snippet = html[card.start():card.start()+400]
    title_m = re.search(r'<h3[^>]*>([^<]+)</h3>', snippet)
    print("Project:", card.group(1), "Title:", title_m.group(1) if title_m else "N/A")

