import os

# Search all files in images/cdil
for root, dirs, files in os.walk('images'):
    for f in files:
        full_path = os.path.join(root, f)
        # print if size is similar to any of the 3 images
        size = os.path.getsize(full_path)
        # sizes of uploaded: 398964, 471616, 473515
        if abs(size - 398964) < 10000 or abs(size - 471616) < 10000 or abs(size - 473515) < 10000:
            print(f"Similar size: {full_path} ({size})")
