import urllib.request, re, os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request("https://cdilrealestate.com/", headers=headers)
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

links = re.findall(r'href=["\']([^"\']+)["\']', html)
print("Homepage links:")
for l in sorted(set(links)):
    if not l.startswith("#") and not l.startswith("javascript"):
        print("  ", l)

imgs = re.findall(r'src=["\']([^"\']+\.(?:jpg|jpeg|png|webp))["\']', html)
print("\nHomepage images:")
for img in sorted(set(imgs)):
    print("  ", img)
