import os, sys

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

start_tag = '<div class="framer-1eht9vy" data-framer-name="CTA">'
end_tag = '</a><!--/$--></div>'

targets = ['ongoing-projects.html', 'completed-projects.html', 'upcoming-projects.html', 'projects.html']

for fname in targets:
    p = os.path.join('pages', fname)
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    
    start_pos = html.find(start_tag)
    if start_pos == -1:
        print(f'{fname}: start_tag NOT FOUND')
        continue
    
    end_pos = html.find(end_tag, start_pos)
    if end_pos == -1:
        print(f'{fname}: end_tag NOT FOUND')
        continue
    
    end_pos += len(end_tag)
    cta_block = html[start_pos:end_pos]
    
    # Confirm it contains the image
    assert 'cdil/bg/2.jpg' in cta_block
    assert 'data-framer-name="CTA"' in cta_block
    
    # Remove it
    new_html = html[:start_pos] + html[end_pos:]
    
    with open(p, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print(f'Successfully removed CTA container with hero house image from {fname} ({len(cta_block)} bytes removed)')
