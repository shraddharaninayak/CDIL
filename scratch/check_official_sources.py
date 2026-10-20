import os, sys
from bs4 import BeautifulSoup

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['ongoing_text.txt', 'completed_text.txt', 'upcoming_text.txt', 'ongoing.html', 'completed.html', 'upcoming.html']:
    p = os.path.join('scratch', 'official_sources', fname)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            print(f'=== {fname} ===')
            print(f.read()[:600])
