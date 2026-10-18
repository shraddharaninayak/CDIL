import os
import hashlib
from PIL import Image

uploaded_dir = r'C:\Users\nshra\.gemini\antigravity\brain\007ee1d0-9729-45f4-9a80-ff5db8d72ad4\.user_uploaded'
files = os.listdir(uploaded_dir)
print("Uploaded files:")
for f in files:
    path = os.path.join(uploaded_dir, f)
    size = os.path.getsize(path)
    try:
        im = Image.open(path)
        print(f"  {f}: {im.size}, format={im.format}, size={size} bytes")
    except Exception as e:
        print(f"  {f}: size={size} bytes (error opening image: {e})")

# Check if these files match any file in the workspace
def hash_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

workspace_images = []
for root, dirs, ws_files in os.walk('images'):
    for file in ws_files:
        workspace_images.append(os.path.join(root, file))

print(f"\nChecking against {len(workspace_images)} workspace images...")
for f in files:
    if f.endswith(('.jpg', '.jpeg', '.png')):
        up_path = os.path.join(uploaded_dir, f)
        up_hash = hash_file(up_path)
        found = False
        for wp in workspace_images:
            if hash_file(wp) == up_hash:
                print(f"MATCH: {f} == {wp}")
                found = True
                break
        if not found:
            print(f"NO DIRECT HASH MATCH for {f}")
