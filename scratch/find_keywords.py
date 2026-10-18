import os

for root, dirs, files in os.walk('images'):
    for f in files:
        if any(keyword in f.lower() for keyword in ['amboli', 'av', 'leaf', 'water', 'pushp', 'palm', 'sunset']):
            print(os.path.join(root, f))
