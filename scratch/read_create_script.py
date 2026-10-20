import os, sys

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

if os.path.exists('scripts/create_project_pages.ps1'):
    with open('scripts/create_project_pages.ps1', 'r', encoding='utf-8', errors='ignore') as f:
        print(f.read())
