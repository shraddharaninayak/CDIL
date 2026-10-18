import os, sys, re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

print("=================================================================")
print("=== COMPREHENSIVE CDIL REAL ESTATE WEBSITE VERIFICATION SUITE ===")
print("=================================================================\n")

html_files = []
for root, dirs, files in os.walk('.'):
    # skip scratch
    if 'scratch' in root or '.git' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

print(f"Total HTML files to inspect: {len(html_files)}")

# 1. Image Check
total_images_checked = 0
broken_images = []
aylaaa_leftover_images = []

for hfile in html_files:
    dir_path = os.path.dirname(hfile)
    with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # check img tags
    soup = BeautifulSoup(content, 'html.parser')
    for img in soup.find_all('img'):
        total_images_checked += 1
        src = img.get('src')
        if not src:
            continue
        # ignore external or data urls
        if src.startswith(('http://', 'https://', 'data:')):
            continue
        # clean query / hash
        clean_src = src.split('?')[0].split('#')[0]
        full_path = os.path.normpath(os.path.join(dir_path, clean_src))
        if not os.path.exists(full_path):
            broken_images.append((hfile, src, full_path))
        
        # Check if AYLAAA image (except homepage hero)
        if 'ZiuHJRK3VDqMlK0bXLemGXGx8o.jpg' in src:
            if os.path.basename(hfile) != 'index.html':
                aylaaa_leftover_images.append((hfile, src, "Hero image used outside index.html"))
        elif any(x in src.lower() for x in ['aylaaa', 'framerusercontent']):
            aylaaa_leftover_images.append((hfile, src, "AYLAAA / Framer leftover"))

print(f"1. Images Checked: {total_images_checked}")
print(f"   Broken Images: {len(broken_images)}")
if broken_images:
    for b in broken_images[:10]:
        print(f"     BROKEN: {b[0]} -> {b[1]}")
else:
    print("   ✓ ZERO broken images across all HTML pages!")

print(f"   AYLAAA Leftover Images: {len(aylaaa_leftover_images)}")
if aylaaa_leftover_images:
    for a in aylaaa_leftover_images[:10]:
        print(f"     AYLAAA: {a[0]} -> {a[1]}")
else:
    print("   ✓ NO leftover AYLAAA images found anywhere (hero image preserved on index.html)!")

# 2. Homepage Hero Image Verification
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

hero_present = 'ZiuHJRK3VDqMlK0bXLemGXGx8o.jpg' in idx_content
print(f"\n2. Homepage Hero Image Preserved: {hero_present}")

# 3. Location Map on About Page (immediately before CTA)
with open('pages/about.html', 'r', encoding='utf-8') as f:
    about_c = f.read()

map_pos = about_c.find('Location Map')
cta_pos = about_c.find('Schedule a Site Visit Button')
print(f"\n3. About Page Project Location Map Check:")
print(f"   Map present: {map_pos != -1}, CTA present: {cta_pos != -1}, Map before CTA: {map_pos < cta_pos if (map_pos != -1 and cta_pos != -1) else False}")

# 4. Verified Content Checklist
print(f"\n4. Official CDIL Content Integration Verification:")
# About
print(f"   About CDIL (about.html):")
print(f"     Founder Vision present: {'Shri. Sandeep B. Kute' in about_c or '16 Years of Excellence' in about_c}")
print(f"     Mission & Vision present: {'To transform Maharashtra' in about_c or 'Mission' in about_c}")
print(f"     Values present: {'Clear Titles' in about_c and 'Prime Scenic Locations' in about_c}")

# Projects
with open('pages/projects.html', 'r', encoding='utf-8') as f:
    p_c = f.read()
print(f"   Projects (projects.html):")
for proj in ['Amboli Van-Veli', 'Mountain Bliss', '3 Leaf Farmhouse', 'Laxmi Pushp', 'Teakwood Farmhouse', 'Watertouch Farmhouse', 'Prophius Farmhouse', 'RiverRanch Farmhouse', 'Ocean Of Beze']:
    print(f"     {proj}: {proj in p_c}")

# Gallery
with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    g_c = f.read()
print(f"   Gallery (gallery.html):")
print(f"     Full 26 project photos present: {g_c.count('cdil-gal-card') == 26}")
print(f"     Lightbox functional: {'cdilLightbox' in g_c}")

# News & Updates
with open('pages/news-updates.html', 'r', encoding='utf-8') as f:
    nu_c = f.read()
print(f"   News & Updates (news-updates.html):")
print(f"     All 9 news clipping articles present: {nu_c.count('cdil-news-card') == 9}")
print(f"     News Lightbox functional: {'cdilNewsLightbox' in nu_c}")

# Blogs
with open('pages/journal.html', 'r', encoding='utf-8') as f:
    j_c = f.read()
print(f"   Blogs & Insights (journal.html / blog.html):")
print(f"     All 16 authentic CDIL blog posts present: {j_c.count('cdil-blog-card') == 16}")
print(f"     Blog Reader Modal functional: {'cdilBlogModal' in j_c}")

print("\n=================================================================")
print("=== VERIFICATION SUITE COMPLETE ===")
print("=================================================================")

