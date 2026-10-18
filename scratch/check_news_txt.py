import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('scratch/official_sources/news_text.txt', 'r', encoding='utf-8', errors='ignore') as f:
    t = f.read()

print("Length of news_text.txt:", len(t))
print("First 1000 chars:")
print(t[:1000])

