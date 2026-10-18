import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = 194330
snippet = c[pos-200:pos+6000]

print("=== ALL 'View →' IN SNIPPET ===")
for m in re.finditer(r'<p[^>]*>View\s*→</p>', snippet):
    # print context of each
    sub = snippet[max(0, m.start()-250):min(len(snippet), m.end()+100)]
    print("\n--- VIEW OCCURRENCE ---")
    print(sub)

