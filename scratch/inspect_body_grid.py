import os, sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('<div class="framer-111okhc">')
print("Position of <div class=\"framer-111okhc\">:", pos)

# Let's inspect the entire contents of this container
# or find the matching closing tag
end_pos = html.find('<!--/$--></div><div class="framer-1j1p29n', pos)
if end_pos == -1:
    end_pos = pos + 25000

print("Length of grid chunk:", end_pos - pos)
snippet = html[pos:pos+1500]
print(snippet)

