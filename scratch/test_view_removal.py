import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Pattern for slide 1: framer-1pvpn3z
    p1 = r'<div class="framer-1pvpn3z"[^>]*>.*?</div></div>'
    # Pattern for slide 2: framer-p7ud9d
    p2 = r'<div class="framer-p7ud9d"[^>]*>.*?</div></div>'
    # Pattern for slide 3: framer-1swy35y
    p3 = r'<div class="framer-1swy35y"[^>]*>.*?</div></div>'

    m1 = re.search(p1, c)
    m2 = re.search(p2, c)
    m3 = re.search(p3, c)

    print(f"File {filepath}:")
    print(f"  Slide 1 View element found: {m1 is not None}")
    print(f"  Slide 2 View element found: {m2 is not None}")
    print(f"  Slide 3 View element found: {m3 is not None}")

update_file('index.html')
update_file('pages/page.html')

