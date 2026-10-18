import os, sys, glob

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

print("Files in scratch:")
for f in os.listdir("scratch"):
    print(" -", f)

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx_about = c.find('data-framer-name="About"')
idx_test = c.find('data-framer-name="Testimonials"')
print('About index:', idx_about)
print('Testimonials index:', idx_test)
print('Context around junction:')
print(repr(c[idx_test - 150 : idx_test + 150]))
