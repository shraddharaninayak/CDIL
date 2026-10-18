import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/about.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Page Head updates
# Replace heading "A house built the slow way." with "About CDIL Real Estate & Infrastructure"
c = c.replace(
    'A house built the slow way.',
    'About CDIL Real Estate & Infrastructure'
)

# Replace head paragraph
old_head_p = 'CDIL Real Estate &amp; Infrastructure was founded in 2008 in Nashik with a simple mission: help families find the perfect plot or farmhouse in scenic locations around Maharashtra.'
new_head_p = 'Reflecting on over 17 years of dedication to excellence, our journey began with a vision to offer the finest farmhouse plots in scenic, lovable locations across Nashik, delivering verified land developments with uncompromised trust.'
c = c.replace(old_head_p, new_head_p)

# 2. Story Chapter 1
c = c.replace(
    'Founded in 2008',
    'Founder’s Vision &amp; Journey'
)
old_story_1 = 'One office above a bakery in Deolali, one advisor, and a rule that has not changed since: nobody presents a home they have not walked through themselves. It made us slower than the portals. It also made us right more often.'
new_story_1 = 'As the founder of CDIL, I am proud to reflect on over 17 years of dedication to excellence. Our journey began with a vision to offer the finest farmhouse plots in beautiful, lovable locations across Nashik, creating not just properties, but cherished homes where families thrive and create lasting memories.'
c = c.replace(old_story_1, new_story_1)

# Story Chapter 2
c = c.replace(
    'How We Work',
    'CDIL Mission'
)
old_story_2 = 'Every residence is re-checked weekly. Every buyer gets one advisor, not a queue. Every offer is explained in plain language before it is signed, including all terms and conditions.'
new_story_2 = 'At CDIL Construction Hub, our mission is to revolutionize the real estate industry by offering unparalleled quality, innovative architectural designs, and sustainable developments with 100% verified legal documentation and transparent customer service.'
c = c.replace(old_story_2, new_story_2)

# Story Chapter 3
c = c.replace(
    'Our Vision',
    'CDIL Vision'
)
old_story_3 = 'To be the most trusted real estate partner in Nashik and Maharashtra, recognized for our innovation, excellence, and commitment to sustainable land development that truly serves our clients.'
new_story_3 = 'Our vision at CDIL Construction Hub is to be a trusted leader in the real estate industry, recognized across Maharashtra for our innovation, environmental stewardship, and enduring commitment to customer-centric development.'
c = c.replace(old_story_3, new_story_3)

# 3. Values Headline
c = c.replace(
    'Four commitments, honoured on every project.',
    'Four core values, honoured on every CDIL development.'
)

# Values cards
c = c.replace(
    'Transparency First',
    'Integrity &amp; Clear Titles'
)
old_val_1 = 'We give you honest, straightforward advice even when it means recommending against a purchase.'
new_val_1 = 'Every plot is 100% sanctioned collector NA with clear legal titles and transparent documentation explained before you commit.'
c = c.replace(old_val_1, new_val_1)

c = c.replace(
    'Personalised Service',
    'Prime Scenic Locations'
)
old_val_2 = 'One dedicated team member guides you from your first enquiry to successful registration.'
new_val_2 = 'Strategically situated across Trimbakeshwar, dam perimeters, wine tourism corridors, and major highway connectivity in Nashik.'
c = c.replace(old_val_2, new_val_2)

c = c.replace(
    'No Hidden Costs',
    'Comprehensive Amenities'
)
old_val_3 = 'All costs, documentation requirements, and timelines are clearly explained before you commit.'
new_val_3 = 'Fully developed gated community layouts featuring wide internal asphalt roads, uninterrupted water, power, and security.'
c = c.replace(old_val_3, new_val_3)

c = c.replace(
    'Prompt Response',
    'Expert Guidance &amp; Care'
)
old_val_4 = 'Calls, emails and messages answered within one business day.'
new_val_4 = 'Over 250+ happy families guided from personalized site walkthroughs through to complete legal registration and possession.'
c = c.replace(old_val_4, new_val_4)

with open('pages/about.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated pages/about.html with authentic CDIL content successfully.")
