import os

for root, dirs, files in os.walk('images/cdil'):
    for f in files:
        print(os.path.join(root, f))
