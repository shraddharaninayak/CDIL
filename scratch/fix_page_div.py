import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/page.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Pattern for <a> in page.html
old_a_open_m = re.search(r'<a (class="framer-gtXe7 [^"]*"[^>]*href="\.\./pages/projects\.html"[^>]*)>', c)
if old_a_open_m:
    attrs = old_a_open_m.group(1)
    attrs_no_href = re.sub(r'\s*href="\.\./pages/projects\.html"', '', attrs)
    if 'style="' in attrs_no_href:
        attrs_no_href = attrs_no_href.replace('style="', 'style="cursor: default; ')
    new_div_open = f'<div {attrs_no_href}>'
    c_new = c[:old_a_open_m.start()] + new_div_open + c[old_a_open_m.end():]
    
    ind_pos = c_new.find('class="framer-1wgasjr"', old_a_open_m.start())
    closing_a_pos = c_new.find('</a><!--/$-->', ind_pos)
    if closing_a_pos != -1:
        c_new = c_new[:closing_a_pos] + '</div><!--/$-->' + c_new[closing_a_pos + len('</a><!--/$-->'):]
        with open('pages/page.html', 'w', encoding='utf-8') as f:
            f.write(c_new)
        print("Updated pages/page.html to div successfully!")
    else:
        print("Could not find closing </a> in page.html!")
else:
    print("Could not match <a> in page.html!")

