import os, sys, glob, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

print("--- Listing files in images/ ---")
img_files = []
for root, dirs, files in os.walk("images"):
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), ".")
        img_files.append(rel)

print(f"Total image files on disk in images/: {len(img_files)}")
for f in sorted(img_files):
    size_kb = os.path.getsize(f) / 1024
    print(f"  {f} ({size_kb:.1f} KB)")

print("\n--- Scanning HTML/CSS files for image references ---")
all_files = glob.glob("**/*.html", recursive=True) + glob.glob("**/*.css", recursive=True)

referenced_images = set()
for file_path in all_files:
    if "scratch" in file_path or ".system_generated" in file_path:
        continue
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    # Find src="...", srcset="...", url(...)
    srcs = re.findall(r'(?:src|href)=["\']([^"\']+\.(?:png|jpg|jpeg|webp|svg|gif))["\']', content, re.IGNORECASE)
    urls = re.findall(r'url\(["\']?([^"\'\)\?#]+\.(?:png|jpg|jpeg|webp|svg|gif))', content, re.IGNORECASE)
    # also srcset
    srcsets = re.findall(r'srcset=["\']([^"\']+)["\']', content, re.IGNORECASE)
    for s in srcsets:
        for part in s.split(','):
            tokens = part.strip().split()
            if tokens and re.search(r'\.(?:png|jpg|jpeg|webp|svg|gif)', tokens[0], re.IGNORECASE):
                referenced_images.add(tokens[0])
    for s in srcs:
        referenced_images.add(s)
    for u in urls:
        referenced_images.add(u)

print(f"Total unique referenced image paths found: {len(referenced_images)}")
for r in sorted(referenced_images):
    print("  Ref:", r)
