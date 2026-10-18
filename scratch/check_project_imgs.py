import os
from PIL import Image

for path in ['images/cdil/gallery/av2.jpg', 'images/cdil/product/22.webp', 'images/projects/av3.jpg', 'images/projects/3leaf1.jpeg', 'images/projects/water.jpg', 'images/projects/lp1.jpeg']:
    if os.path.exists(path):
        im = Image.open(path)
        print(f"{path}: size={im.size}, format={im.format}")
