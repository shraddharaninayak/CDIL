import os, re

root_dir = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"

files = [
    "index.html",
    "pages/3-leaf-farmhouse.html",
    "pages/3d-printed-farmhouse.html",
    "pages/about.html",
    "pages/amboli-van-veli.html",
    "pages/blog.html",
    "pages/completed-projects.html",
    "pages/contact.html",
    "pages/gallery.html",
    "pages/journal.html",
    "pages/laxmi-pushp.html",
    "pages/news-updates.html",
    "pages/ongoing-projects.html",
    "pages/page.html",
    "pages/privacy.html",
    "pages/projects.html",
    "pages/terms.html",
    "pages/upcoming-projects.html",
    "pages/video-gallery.html",
    "pages/watertouch.html"
]

for rel in files:
    fpath = os.path.join(root_dir, rel)
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    has_lang = 'aria-label="Language"' in text
    has_theme = 'Switch to light mode' in text or 'aria-label="Toggle theme"' in text
    has_nav = 'framer-ck16ym-container' in text
    print(f"{rel:35} | Nav: {has_nav} | Lang: {has_lang} | Theme: {has_theme}")
