import os, sys

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['ongoing-projects.html', 'completed-projects.html', 'upcoming-projects.html', 'projects.html']:
    p = os.path.join('pages', fname)
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    
    start_tag = '<div class="framer-1eht9vy" data-framer-name="CTA">'
    start_pos = html.find(start_tag)
    end_tag = '</a><!--/$--></div>'
    end_pos = html.find(end_tag, start_pos) + len(end_tag)
    
    print(f'=== {fname} ===')
    print('BEFORE CTA:', html[start_pos-100:start_pos])
    print('AFTER CTA:', html[end_pos:end_pos+100])
