import os, sys, glob, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

framer_hashes = [
    "1WE8VVvhM5ILXM8zlwp4JTbDcg",
    "2TOsdQ0l1UFLP08nIBuvp5YE0",
    "3fSSK360dEzMizQHdrXt1Dbhw0",
    "44IzJSemp73a6BgdeKY6t9A1Xk",
    "6gAYT1fHxFFVy3Ei5y2n9JlNs",
    "7Ob5jUxK0GfjhrfOQIFfzBI668o",
    "AjQp2dUVDzqj5LSzanz06FUWbU",
    "HrKKcFQ3DVsJ9P9jkiiXZh5juE",
    "IjxtO3SV152XjF7XWHpYAOLUJMg",
    "KcexKs0xLJniVsGT2OwYYSwL4I",
    "O5kbDDgCLmTDDKwDeuBnqIDG0Y",
    "PC9CvBmAqTkuV7nSuyR6cyq5ss",
    "XdflLOICap9i3yayush9YNU6o",
    "XiHIAV0HFUSKlrC1YLOOARfPj4",
    "Xqe3z10c8F84k5DXRwTjeR3WYCw",
    "ZiuHJRK3VDqMlK0bXLemGXGx8o",
    "c2ENN0w6FyOgaTz5OytE1ye0flo",
    "cCYedN2F79ejMcgWgXCOfU73a8",
    "gynlhAwJLfMLFJEhh4xjXpPCPQ",
    "hntiEJ8LUjfWfuFyUy2KSsGrqDE",
    "htqVoCdq8HKHyjSa8i9Qo4yCU8w",
    "kLLCGbGu6fjY89G5W0bfPMNl6HA",
    "rURwvrDaaU0CEAVcJ7aKoh4CFo",
    "uCarZ02wIibfZsAt8yCmnDEAwk",
    "up3HHBNHrsLu5dUK10kakAq7Y",
    "uzcv3F3dlHJZ9GsmosUxczA3lU",
    "yp7gODnubKyOzhmsbHhfNC0RPeI"
]

all_html = glob.glob("**/*.html", recursive=True)
print(f"Total HTML files: {len(all_html)}")

for hf in sorted(all_html):
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    present = [h for h in framer_hashes if h in c]
    if present:
        print(f"{hf}: {len(present)} hashes -> {present}")
    else:
        print(f"{hf}: 0 hashes")
