import os, sys, glob, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

# Mappings for each file
# Each mapping maps an AYLAAA hash to its replacement image path (relative to the file)

# Common mappings for pages/
PAGES_COMMON = {
    # Favicon
    "kLLCGbGu6fjY89G5W0bfPMNl6HA": "../images/cdil-logo.png",
    # Meta OG/Twitter preview
    "1WE8VVvhM5ILXM8zlwp4JTbDcg": "../images/cdil/banner/3leaf-layout.jpeg",
    # Bottom CTA background
    "HrKKcFQ3DVsJ9P9jkiiXZh5juE": "../images/cdil/bg/2.jpg",
}

# Root common for index.html
ROOT_COMMON = {
    "kLLCGbGu6fjY89G5W0bfPMNl6HA": "./images/cdil-logo.png",
    "1WE8VVvhM5ILXM8zlwp4JTbDcg": "./images/cdil/banner/3leaf-layout.jpeg",
    "HrKKcFQ3DVsJ9P9jkiiXZh5juE": "./images/cdil/bg/2.jpg",
}

FILE_MAPPINGS = {
    "index.html": {
        **ROOT_COMMON,
        "XdflLOICap9i3yayush9YNU6o": "./images/cdil/other/CD.jpeg",
        "KcexKs0xLJniVsGT2OwYYSwL4I": "./images/cdil/blog/smart.png",
        "rURwvrDaaU0CEAVcJ7aKoh4CFo": "./images/cdil/blog/Vineyard.png",
        "yp7gODnubKyOzhmsbHhfNC0RPeI": "./images/cdil/blog/why.png",
        "Xqe3z10c8F84k5DXRwTjeR3WYCw": "./images/projects/3leaf1.jpeg",
        "O5kbDDgCLmTDDKwDeuBnqIDG0Y": "./images/projects/water.jpg",
        # NOTE: ZiuHJRK3VDqMlK0bXLemGXGx8o MUST REMAIN UNCHANGED on index.html hero!
    },
    "pages/page.html": {
        "kLLCGbGu6fjY89G5W0bfPMNl6HA": "../images/cdil-logo.png",
        "1WE8VVvhM5ILXM8zlwp4JTbDcg": "../images/cdil/banner/3leaf-layout.jpeg",
        "HrKKcFQ3DVsJ9P9jkiiXZh5juE": "../images/cdil/bg/2.jpg",
        "XdflLOICap9i3yayush9YNU6o": "../images/cdil/other/CD.jpeg",
        "KcexKs0xLJniVsGT2OwYYSwL4I": "../images/cdil/blog/smart.png",
        "rURwvrDaaU0CEAVcJ7aKoh4CFo": "../images/cdil/blog/Vineyard.png",
        "yp7gODnubKyOzhmsbHhfNC0RPeI": "../images/cdil/blog/why.png",
        "Xqe3z10c8F84k5DXRwTjeR3WYCw": "../images/projects/3leaf1.jpeg",
        "O5kbDDgCLmTDDKwDeuBnqIDG0Y": "../images/projects/water.jpg",
        # NOTE: ZiuHJRK3VDqMlK0bXLemGXGx8o MUST REMAIN UNCHANGED on page.html hero!
    },
    "pages/3-leaf-farmhouse.html": {
        **PAGES_COMMON,
        "7Ob5jUxK0GfjhrfOQIFfzBI668o": "../images/cdil/banner/3leaf-layout.jpeg",
        "ZiuHJRK3VDqMlK0bXLemGXGx8o": "../images/projects/3leaf1.jpeg",
        "uzcv3F3dlHJZ9GsmosUxczA3lU": "../images/cdil/gallery/3l10.jpeg",
        "44IzJSemp73a6BgdeKY6t9A1Xk": "../images/cdil/gallery/3l2.png",
        "c2ENN0w6FyOgaTz5OytE1ye0flo": "../images/cdil/other/22.jpeg",
    },
    "pages/laxmi-pushp.html": {
        **PAGES_COMMON,
        "6gAYT1fHxFFVy3Ei5y2n9JlNs": "../images/projects/lp1.jpeg",
        "Xqe3z10c8F84k5DXRwTjeR3WYCw": "../images/projects/lp1.jpeg",
        "cCYedN2F79ejMcgWgXCOfU73a8": "../images/cdil/gallery/lp2.jpeg",
        "hntiEJ8LUjfWfuFyUy2KSsGrqDE": "../images/cdil/gallery/lp3.jpeg",
        "XiHIAV0HFUSKlrC1YLOOARfPj4": "../images/cdil/other/22.jpeg",
    },
    "pages/amboli-van-veli.html": {
        **PAGES_COMMON,
        "3fSSK360dEzMizQHdrXt1Dbhw0": "../images/cdil/gallery/av2.jpg",
        "O5kbDDgCLmTDDKwDeuBnqIDG0Y": "../images/cdil/gallery/av.png",
        "AjQp2dUVDzqj5LSzanz06FUWbU": "../images/cdil/gallery/av1.jpg",
        "uCarZ02wIibfZsAt8yCmnDEAwk": "../images/cdil/other/22.jpeg",
    },
    "pages/watertouch.html": {
        **PAGES_COMMON,
        "3fSSK360dEzMizQHdrXt1Dbhw0": "../images/cdil/gallery/wt2.jpeg",
        "O5kbDDgCLmTDDKwDeuBnqIDG0Y": "../images/projects/watertouch.jpeg",
        "AjQp2dUVDzqj5LSzanz06FUWbU": "../images/cdil/gallery/wt1.jpeg",
        "uCarZ02wIibfZsAt8yCmnDEAwk": "../images/cdil/other/22.jpeg",
    },
    "pages/projects.html": {
        **PAGES_COMMON,
        "2TOsdQ0l1UFLP08nIBuvp5YE0": "../images/cdil/gallery/mb1.jpeg",
        "PC9CvBmAqTkuV7nSuyR6cyq5ss": "../images/projects/riverranch.jpeg",
        "gynlhAwJLfMLFJEhh4xjXpPCPQ": "../images/cdil/product/ps1.jpeg",
    },
    "pages/about.html": {
        **PAGES_COMMON,
        "htqVoCdq8HKHyjSa8i9Qo4yCU8w": "../images/cdil/other/CD.jpeg",
        "up3HHBNHrsLu5dUK10kakAq7Y": "../images/cdil/banner/cdil-projects.jpeg",
    },
    "pages/3d-printed-farmhouse.html": {
        **PAGES_COMMON,
        "up3HHBNHrsLu5dUK10kakAq7Y": "../images/cdil/icon/3d2.jpeg",
    },
    "pages/contact.html": {
        **PAGES_COMMON,
        "IjxtO3SV152XjF7XWHpYAOLUJMg": "../images/cdil/other/22.jpeg",
    },
    "pages/gallery.html": {
        **PAGES_COMMON,
        "up3HHBNHrsLu5dUK10kakAq7Y": "../images/cdil/gallery/hills.jpeg",
    },
    "pages/journal.html": {
        **PAGES_COMMON,
        "KcexKs0xLJniVsGT2OwYYSwL4I": "../images/cdil/blog/smart.png",
        "rURwvrDaaU0CEAVcJ7aKoh4CFo": "../images/cdil/blog/Vineyard.png",
        "yp7gODnubKyOzhmsbHhfNC0RPeI": "../images/cdil/blog/why.png",
    },
    "pages/news-updates.html": {
        **PAGES_COMMON,
        "up3HHBNHrsLu5dUK10kakAq7Y": "../images/cdil/icon/n1.jpeg",
    },
    "pages/video-gallery.html": {
        **PAGES_COMMON,
        "up3HHBNHrsLu5dUK10kakAq7Y": "../images/projects/water.jpg",
    },
    "pages/privacy.html": {
        **PAGES_COMMON,
    },
    "pages/terms.html": {
        **PAGES_COMMON,
    }
}

def replace_hashes_in_html(content, mapping, file_path):
    new_content = content
    for h, repl in mapping.items():
        # Check if hero image on index.html or pages/page.html - DO NOT TOUCH!
        if h == "ZiuHJRK3VDqMlK0bXLemGXGx8o" and file_path in ["index.html", "pages/page.html", "pages\\page.html"]:
            continue
        
        # 1. Replace srcset entries
        # srcset="https://framerusercontent.com/images/HASH... 512w, ..."
        # Match srcset attribute containing this hash
        def replace_srcset(match):
            attr_val = match.group(1)
            if h in attr_val:
                return f'srcset="{repl}"'
            return match.group(0)
        new_content = re.sub(r'srcset="([^"]*' + re.escape(h) + r'[^"]*)"', replace_srcset, new_content)

        # 2. Replace src="..."
        def replace_src(match):
            return f'src="{repl}"'
        new_content = re.sub(r'src="[^"]*' + re.escape(h) + r'[^"]*"', replace_src, new_content)

        # 3. Replace href="..." (favicons)
        def replace_href(match):
            return f'href="{repl}"'
        new_content = re.sub(r'href="[^"]*' + re.escape(h) + r'[^"]*"', replace_href, new_content)

        # 4. Replace content="..." (meta og/twitter)
        def replace_content(match):
            return f'content="{repl}"'
        new_content = re.sub(r'content="[^"]*' + re.escape(h) + r'[^"]*"', replace_content, new_content)

        # 5. Replace url(...) in inline styles or css
        def replace_url(match):
            return f'url("{repl}")'
        new_content = re.sub(r'url\(["\']?[^"\')]*' + re.escape(h) + r'[^"\')]*["\']?\)', replace_url, new_content)

    return new_content

# Run replacement across all configured files
for rel_path, mapping in FILE_MAPPINGS.items():
    norm_path = rel_path.replace("/", os.sep)
    if not os.path.exists(norm_path):
        print(f"Warning: {norm_path} does not exist!")
        continue
    with open(norm_path, "r", encoding="utf-8") as f:
        original = f.read()
    
    updated = replace_hashes_in_html(original, mapping, rel_path)
    
    if updated != original:
        with open(norm_path, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"Updated {rel_path} ({len(original)} -> {len(updated)} bytes)")
    else:
        print(f"No changes in {rel_path}")

print("All replacements completed.")
