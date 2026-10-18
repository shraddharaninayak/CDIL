import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()

# find body
body_pos = c.find('<body')
print("Body pos:", body_pos)
# Find all occurrences of framer-111okhc AFTER body_pos
occurrences = [m.start() for m in re.finditer(r'framer-111okhc', c[body_pos:])]
print("Occurrences of framer-111okhc after body:", occurrences)

# find the footer / closing tags
footer_pos = c.find('<footer')
print("Footer pos in gallery:", footer_pos)
print("From footer_pos to end:", len(c) - footer_pos)
print("Tail 500 chars of gallery.html:")
print(c[-500:])

