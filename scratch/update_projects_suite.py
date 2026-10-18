import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

# Definitions of all 9 authentic CDIL projects
PROJECTS = [
    # Ongoing
    {
        "id": "amboli-van-veli",
        "status": "ongoing",
        "badge": "Ongoing Project",
        "category": "Ongoing Farmhouse Plots",
        "title": "Amboli Van-Veli",
        "loc1": "Gunjal Farm Amboli",
        "loc2": "Trimbakeshwar, Nashik",
        "img": "../images/projects/av3.jpg",
        "alt": "Amboli Van-Veli — Scenic Riverside Farmhouse Community in Trimbakeshwar Nashik",
        "link": "../pages/amboli-van-veli.html"
    },
    {
        "id": "mountain-bliss",
        "status": "ongoing",
        "badge": "Ongoing Project",
        "category": "Scenic Mountain Retreat",
        "title": "Mountain Bliss",
        "loc1": "Cone Dam View Vaghera",
        "loc2": "Nashik",
        "img": "../images/cdil/gallery/mb1.jpeg",
        "alt": "Mountain Bliss — Elevated Panorama Farmhouse Plots at Cone Dam View Nashik",
        "link": "../pages/amboli-van-veli.html"
    },
    {
        "id": "3-leaf-farmhouse",
        "status": "ongoing",
        "badge": "Ongoing Project",
        "category": "Luxury Gated Farmhouse",
        "title": "3 Leaf Farmhouse",
        "loc1": "Kharoli Road, Samundi",
        "loc2": "Trimbakeshwar, Nashik",
        "img": "../images/projects/3leaf1.jpeg",
        "alt": "3 Leaf Farmhouse — Exclusive Countryside Living in Trimbakeshwar Nashik",
        "link": "../pages/3-leaf-farmhouse.html"
    },
    {
        "id": "laxmi-pushp",
        "status": "ongoing",
        "badge": "Ongoing Project",
        "category": "Premium Villa & Farmhouse Plots",
        "title": "Laxmi Pushp",
        "loc1": "Trambak Road",
        "loc2": "Nashik",
        "img": "../images/projects/lp1.jpeg",
        "alt": "Laxmi Pushp — Premium Farmhouse Plots on Trambak Road Nashik",
        "link": "../pages/laxmi-pushp.html"
    },
    # Completed
    {
        "id": "teakwood-farmhouse",
        "status": "completed",
        "badge": "Completed Project",
        "category": "Delivered Farmhouse Community",
        "title": "Teakwood Farmhouse",
        "loc1": "Wadivarhe",
        "loc2": "Nashik",
        "img": "../images/projects/teakwood.jpeg",
        "alt": "Teakwood Farmhouse Project — Fully Developed Farmhouse Haven in Wadivarhe Nashik",
        "link": "../pages/watertouch.html"
    },
    {
        "id": "watertouch-farmhouse",
        "status": "completed",
        "badge": "Completed Project",
        "category": "Waterfront Living",
        "title": "Watertouch Farmhouse",
        "loc1": "Mahiravni",
        "loc2": "Nashik",
        "img": "../images/projects/water.jpg",
        "alt": "Watertouch Farmhouse Project — Waterfront Living in Mahiravni Nashik",
        "link": "../pages/watertouch.html"
    },
    {
        "id": "prophius-farmhouse",
        "status": "completed",
        "badge": "Completed Project",
        "category": "Exclusive Farmhouse Living",
        "title": "Prophius Farmhouse",
        "loc1": "Khambale",
        "loc2": "Nashik",
        "img": "../images/cdil/project/ps33.jpeg",
        "alt": "Prophius Farmhouse Project — Delivered Countryside Estates in Khambale Nashik",
        "link": "../pages/watertouch.html"
    },
    # Upcoming
    {
        "id": "riverranch-farmhouse",
        "status": "upcoming",
        "badge": "Upcoming Project",
        "category": "Riverfront Farmhouse Plots",
        "title": "RiverRanch Farmhouse",
        "loc1": "Khambale, Girna River",
        "loc2": "Nashik",
        "img": "../images/projects/riverranch.jpeg",
        "alt": "RiverRanch Farmhouse Project — Scenic Riverside Farmhouse Plots in Nashik",
        "link": "../pages/watertouch.html"
    },
    {
        "id": "ocean-of-beze",
        "status": "upcoming",
        "badge": "Upcoming Project",
        "category": "Serene Lakeside Haven",
        "title": "Ocean Of Beze",
        "loc1": "Beze Trambak",
        "loc2": "Nashik",
        "img": "../images/cdil/banner/ocean_of_beze.png",
        "alt": "Ocean Of Beze — Upcoming Serene Retreat Near Beze Dam Trimbakeshwar Nashik",
        "link": "../pages/watertouch.html"
    }
]

def generate_card_html(p):
    return f'''<!--$--><a class="framer-zzaslx framer-1u6c2pf" href="{p['link']}" data-cdil-project="{p['id']}" data-cdil-status="{p['status']}"><div class="ssr-variant"><div class="framer-8gewg3" data-framer-name="Card Photo"><div style="position:absolute;border-radius:inherit;corner-shape:inherit;top:0;right:0;bottom:0;left:0" data-framer-background-image-wrapper="true"><img decoding="auto" width="2560" height="1429" sizes="(min-width: 1440px) max((100vw - 160px) / 3, 280px), (max-width: 809.98px) max(100vw - 40px, 280px), (min-width: 810px) and (max-width: 1439.98px) max((100vw - 88px) / 2, 280px)" srcset="{p['img']}" src="{p['img']}" alt="{p['alt']}" style="display:block;width:100%;height:100%;border-radius:inherit;corner-shape:inherit;object-position:center;object-fit:cover"></div><div class="framer-z9yopn ay-glass" data-border="true" data-framer-name="Status Badge"><div class="framer-1rh0iaj" data-framer-component-type="RichTextContainer" style="transform:none"><p class="framer-text framer-styles-preset-11shj4z" data-styles-preset="IcUkpNqYv" dir="auto">{p['badge']}</p></div></div></div></div><div class="framer-6zj54n" data-framer-component-type="RichTextContainer" style="transform:none"><p class="framer-text framer-styles-preset-oif7b2" data-styles-preset="AekMMZ7SL" dir="auto">{p['category']}</p></div><div class="framer-14jhv5h" data-framer-name="Name" data-framer-component-type="RichTextContainer" style="transform:none"><h3 class="framer-text framer-styles-preset-1c1kudq" data-styles-preset="ppMvKx6r4" dir="auto">{p['title']}</h3></div><div class="framer-1izul6b" data-framer-name="Address Row"><div class="framer-jomb0w" data-framer-component-type="RichTextContainer" style="transform:none"><p class="framer-text framer-styles-preset-hijxov" data-styles-preset="Fm9TsQ8Q1" dir="auto">{p['loc1']}</p></div><div class="framer-115upqx" data-framer-component-type="RichTextContainer" style="transform:none"><p class="framer-text framer-styles-preset-hijxov" data-styles-preset="Fm9TsQ8Q1" dir="auto">·</p></div><div class="framer-19ompee" data-framer-component-type="RichTextContainer" style="transform:none"><p class="framer-text framer-styles-preset-hijxov" data-styles-preset="Fm9TsQ8Q1" dir="auto">{p['loc2']}</p></div></div></a><!--/$-->'''

all_cards_html = '\n'.join([generate_card_html(p) for p in PROJECTS])

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the grid container
grid_start = content.find('<div class="framer-111okhc">')
if grid_start == -1:
    print("Could not find <div class=\"framer-111okhc\"> in projects.html!")
    sys.exit(1)

# Find where the cards end - before the next container
# Look for the last card's closing </a>
last_a_pos = content.find('Deolali, Nashik</p></div></div></a>', grid_start)
if last_a_pos == -1:
    # try finding River Ranch
    rr_pos = content.find('River Ranch', grid_start)
    if rr_pos != -1:
        last_a_pos = content.find('</a><!--/$-->', rr_pos)

# Let's find exactly the range of cards
first_card_start = content.find('<a class="framer-zzaslx framer-1u6c2pf"', grid_start)
last_card_end = content.find('</div><div class="framer-1j1p29n', first_card_start)

print(f"Replacing cards from {first_card_start} to {last_card_end}")
new_grid_content = content[:first_card_start] + all_cards_html + content[last_card_end:]

with open('pages/projects.html', 'w', encoding='utf-8') as f:
    f.write(new_grid_content)

print(f"Updated pages/projects.html with {len(PROJECTS)} authentic CDIL project cards!")

# Now create/update dedicated category pages
def make_category_page(cat_key, cat_title, filename):
    cat_cards_html = '\n'.join([generate_card_html(p) for p in PROJECTS if p['status'] == cat_key])
    cat_page = new_grid_content
    # Replace title
    cat_page = re.sub(r'<title>.*?</title>', f'<title>{cat_title} | CDIL Real Estate &amp; Infrastructure</title>', cat_page)
    # Set default filter button styles in the HTML
    # In button list:
    for btn_filter in ['all', 'ongoing', 'completed', 'upcoming']:
        is_active = (btn_filter == cat_key)
        old_btn_pattern = rf'<button type="button" aria-pressed="[^"]*" class="rf-c-R6malp" data-filter="{btn_filter}"[^>]*>'
        active_style = 'style="background: var(--token-025422ea-d283-4879-b332-741cb1c834c7, rgb(26, 38, 32)); color: var(--token-ed5af0b1-8875-4b9b-a8d0-dd29f7c8c608, rgb(243, 239, 228)); border-color: var(--token-025422ea-d283-4879-b332-741cb1c834c7, rgb(26, 38, 32)); font-family: Inter, sans-serif; font-size: 15px; font-weight: 400; letter-spacing: 0em; line-height: 1em;"'
        inactive_style = 'style="background: transparent; color: var(--token-b8cfd3da-418b-4999-a7f7-4bf97baf1624, rgba(26, 38, 32, 0.74)); border-color: var(--token-d34888b7-6c91-4dbc-95a1-370fba2352b1, rgba(26, 38, 32, 0.16)); font-family: Inter, sans-serif; font-size: 15px; font-weight: 400; letter-spacing: 0em; line-height: 1em;"'
        replacement_btn = f'<button type="button" aria-pressed="{str(is_active).lower()}" class="rf-c-R6malp" data-filter="{btn_filter}" {active_style if is_active else inactive_style}>'
        cat_page = re.sub(old_btn_pattern, replacement_btn, cat_page)
    
    with open(f'pages/{filename}', 'w', encoding='utf-8') as f:
        f.write(cat_page)
    print(f"Created pages/{filename} with pre-selected filter: {cat_key}!")

make_category_page('ongoing', 'Ongoing Projects', 'ongoing-projects.html')
make_category_page('completed', 'Completed Projects', 'completed-projects.html')
make_category_page('upcoming', 'Upcoming Projects', 'upcoming-projects.html')

print("All project pages updated successfully.")

