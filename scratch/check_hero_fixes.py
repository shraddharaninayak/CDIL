import os, sys

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['ongoing-projects.html', 'completed-projects.html', 'upcoming-projects.html', 'projects.html']:
    p = os.path.join('pages', fname)
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    print(f'=== {fname} ===')
    idx = html.find('id="cdil-hero-fix"')
    if idx != -1:
        end = html.find('</style>', idx)
        print(html[idx:end+8])
    else:
        print('cdil-hero-fix not found')
