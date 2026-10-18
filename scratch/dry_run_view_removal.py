import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

def transform_card(content):
    # 1. Slide 1 view link
    p1 = r'<div class="framer-1pvpn3z"[^>]*>.*?</div></div>'
    # 2. Slide 2 view link
    p2 = r'<div class="framer-p7ud9d"[^>]*>.*?</div></div>'
    # 3. Slide 3 view link
    p3 = r'<div class="framer-1swy35y"[^>]*>.*?</div></div>'

    # Remove all 3 view links
    c_new = re.sub(p1, '', content)
    c_new = re.sub(p2, '', c_new)
    c_new = re.sub(p3, '', c_new)

    # 4. Set height: 72px on framer-60zqrq
    c_new = c_new.replace(
        '<div class="framer-60zqrq" style="background-color: rgba(0, 0, 0, 0); opacity: 1;">',
        '<div class="framer-60zqrq" style="background-color: rgba(0, 0, 0, 0); opacity: 1; height: 72px;">'
    )

    # 5. Change outer <a class="framer-gtXe7 ... href="./pages/projects.html" ...> to <div ...>
    # Find the opening <a class="framer-gtXe7
    old_a_open_m = re.search(r'<a (class="framer-gtXe7 [^"]*"[^>]*href="\./pages/projects\.html"[^>]*)>', c_new)
    if old_a_open_m:
        attrs = old_a_open_m.group(1)
        # remove href="./pages/projects.html"
        attrs_no_href = re.sub(r'\s*href="\./pages/projects\.html"', '', attrs)
        # add cursor: default to style if style exists
        if 'style="' in attrs_no_href:
            attrs_no_href = attrs_no_href.replace('style="', 'style="cursor: default; ')
        new_div_open = f'<div {attrs_no_href}>'
        c_new = c_new[:old_a_open_m.start()] + new_div_open + c_new[old_a_open_m.end():]
        
        # Replace the matching closing </a>
        # It's right after framer-1wgasjr indicators
        # find framer-1wgasjr after old_a_open_m.start()
        ind_pos = c_new.find('class="framer-1wgasjr"', old_a_open_m.start())
        closing_a_pos = c_new.find('</a><!--/$-->', ind_pos)
        if closing_a_pos != -1:
            c_new = c_new[:closing_a_pos] + '</div><!--/$-->' + c_new[closing_a_pos + len('</a><!--/$-->'):]
            print("Successfully converted outer <a> to <div>!")
        else:
            print("Could not find closing </a> after indicators!")

    return c_new

with open('index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

res = transform_card(orig)

# Verify
print("Occurrences of 'View →' in new index.html:", res.count('View →'))
pos = res.find('class="framer-gtXe7')
print("\nNew card snippet:")
print(res[pos:pos+1600])

