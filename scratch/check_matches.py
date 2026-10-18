import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

p1 = r'<div class="framer-1pvpn3z"[^>]*>.*?</div></div>'
p2 = r'<div class="framer-p7ud9d"[^>]*>.*?</div></div>'
p3 = r'<div class="framer-1swy35y"[^>]*>.*?</div></div>'

print("Match 1:")
print(re.search(p1, c).group(0))

print("\nMatch 2:")
print(re.search(p2, c).group(0))

print("\nMatch 3:")
print(re.search(p3, c).group(0))

