import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/about.html', 'r', encoding='utf-8') as f:
    c = f.read()

# find all sections or main container children with data-framer-name
sections = re.findall(r'<div[^>]*data-framer-name=["\']([^"\']+)["\'][^>]*>', c)
print("Data framer names in about.html:")
for s in sections:
    print(" -", s)
