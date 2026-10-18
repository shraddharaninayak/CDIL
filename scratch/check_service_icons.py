import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

print("Files in images/cdil/service/:")
if os.path.exists("images/cdil/service"):
    for f in os.listdir("images/cdil/service"):
        p = os.path.join("images/cdil/service", f)
        print(f" - {f}: {os.path.getsize(p)} bytes")
