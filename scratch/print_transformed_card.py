import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

def transform_card(content):
    p1 = r'<div class="framer-1pvpn3z"[^>]*>.*?</div></div>'
    p2 = r'<div class="framer-p7ud9d"[^>]*>.*?</div></div>'
    p3 = r'<div class="framer-1swy35y"[^>]*>.*?</div></div>'

    c_new = re.sub(p1, '', content)
    c_new = re.sub(p2, '', c_new)
    c_new = re.sub(p3, '', c_new)

    c_new = c_new.replace(
        '<div class="framer-60zqrq" style="background-color: rgba(0, 0, 0, 0); opacity: 1;">',
        '<div class="framer-60zqrq" style="background-color: rgba(0, 0, 0, 0); opacity: 1; height: 72px;">'
    )

    old_a_open_m = re.search(r'<a (class="framer-gtXe7 [^"]*"[^>]*href="\./pages/projects\.html"[^>]*)>', c_new)
    if old_a_open_m:
        attrs = old_a_open_m.group(1)
        attrs_no_href = re.sub(r'\s*href="\./pages/projects\.html"', '', attrs)
        if 'style="' in attrs_no_href:
            attrs_no_href = attrs_no_href.replace('style="', 'style="cursor: default; ')
        new_div_open = f'<div {attrs_no_href}>'
        c_new = c_new[:old_a_open_m.start()] + new_div_open + c_new[old_a_open_m.end():]
        
        ind_pos = c_new.find('class="framer-1wgasjr"', old_a_open_m.start())
        closing_a_pos = c_new.find('</a><!--/$-->', ind_pos)
        if closing_a_pos != -1:
            c_new = c_new[:closing_a_pos] + '</div><!--/$-->' + c_new[closing_a_pos + len('</a><!--/$-->'):]

    return c_new

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

res = transform_card(orig)
pos1 = res.find('class="framer-gtXe7') - 5
pos2 = res.find('</div><!--/$-->', pos1 + 500) + len('</div><!--/$-->')

print("FULL NEW CARD HTML:")
print(res[pos1:pos2])

