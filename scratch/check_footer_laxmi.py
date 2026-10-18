import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/laxmi-pushp.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('<footer')
print("Footer pos in laxmi-pushp:", pos)
print("Length from footer to end:", len(c) - pos)

# Also let's check what was before footer in laxmi-pushp
print("\nBefore footer:")
print(c[pos-500:pos])

