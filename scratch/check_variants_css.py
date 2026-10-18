import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

for m in re.finditer(r'\.framer-[a-zA-Z0-9_-]*\s*\.framer-60zqrq\b[^{]*\{[^}]+\}', c):
    print("60zqrq variant:", m.group(0))

for m in re.finditer(r'[^{}]*framer-gtXe7[^{}]*\{[^}]+\}', c):
    print("gtXe7:", m.group(0))

