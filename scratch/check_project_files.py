import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

for f in ['pages/ongoing-projects.html', 'pages/completed-projects.html', 'pages/upcoming-projects.html']:
    exists = os.path.exists(f)
    print(f"{f}: exists={exists}, size={os.path.getsize(f) if exists else 0}")
