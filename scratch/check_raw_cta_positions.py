import os, sys

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['ongoing-projects.html', 'completed-projects.html', 'upcoming-projects.html', 'projects.html']:
    p = os.path.join('pages', fname)
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    
    start_tag = '<div class="framer-1eht9vy" data-framer-name="CTA">'
    start_pos = html.find(start_tag)
    if start_pos == -1:
        print(f'{fname}: NOT found')
        continue
    
    # find where it ends
    end_tag = '</a><!--/$--></div>'
    end_pos = html.find(end_tag, start_pos)
    if end_pos != -1:
        end_pos += len(end_tag)
        snippet = html[start_pos:end_pos]
        print(f'{fname}: start={start_pos}, end={end_pos}, len={len(snippet)}')
        # verify snippet starts with start_tag and ends with end_tag
        assert snippet.startswith(start_tag)
        assert snippet.endswith('</div>')
    else:
        print(f'{fname}: end_tag not found')
