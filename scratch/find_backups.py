import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

# check files in scratch or pages
for root, dirs, files in os.walk('.'):
    for f in files:
        if 'project' in f.lower() and f.endswith(('.bak', '.html', '.orig', '.txt')):
            print(os.path.join(root, f))

