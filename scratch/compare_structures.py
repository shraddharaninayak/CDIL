import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

for fname in ['gallery.html', 'news-updates.html', 'about.html']:
    with open(f'pages/{fname}', 'r', encoding='utf-8') as f:
        c = f.read()
    pos_cta = c.find('Schedule a Site Visit')
    pos_footer = c.find('<footer')
    print(f"=== {fname} ===")
    print(f"Total: {len(c)}, pos_cta: {pos_cta}, pos_footer: {pos_footer}")
    print("Between CTA and footer:")
    # print the structure
    snippet = c[pos_cta:pos_footer]
    print(f"Length between CTA and footer: {len(snippet)}")

