import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()

# find body
body_pos = c.find('<body')
cta_pos = c.find('<div class="framer-1eht9vy" data-framer-name="CTA">')

body_content = c[body_pos:cta_pos]
print("Body content length:", len(body_content))

# Look for gallery container or headings
headings = re.findall(r'<h[123][^>]*>(.*?)</h[123]>', body_content)
print("Headings in gallery:", headings)

# Look for image tags
imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"][^>]*>', body_content)
print("Images count in gallery body:", len(imgs))
for img in imgs[:15]:
    print("  Img:", img)

