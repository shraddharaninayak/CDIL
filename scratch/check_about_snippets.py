import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/about.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Let's inspect Page Head
s_head = c.find('data-framer-name="Page Head"')
s_story = c.find('data-framer-name="Story"')
s_values = c.find('data-framer-name="Values"')
s_banner = c.find('data-framer-name="Banner"')
s_cta = c.find('data-framer-name="CTA"')

print("Page Head snippet:")
print(repr(c[s_head:s_head+400]))

print("\nStory snippet:")
print(repr(c[s_story:s_story+400]))

print("\nValues snippet:")
print(repr(c[s_values:s_values+400]))
