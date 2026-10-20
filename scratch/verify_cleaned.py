import os, sys

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['ongoing-projects.html', 'completed-projects.html', 'upcoming-projects.html', 'projects.html']:
    p = os.path.join('pages', fname)
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Check for any other 2.jpg
    start_tag = '<div class="framer-1eht9vy" data-framer-name="CTA">'
    end_tag = '</a><!--/$--></div>'
    start_pos = html.find(start_tag)
    end_pos = html.find(end_tag, start_pos) + len(end_tag)
    
    cleaned_html = html[:start_pos] + html[end_pos:]
    if '2.jpg' in cleaned_html:
        print(f'{fname}: 2.jpg STILL IN CLEANED HTML!')
    else:
        print(f'{fname}: 2.jpg completely absent from cleaned HTML.')
