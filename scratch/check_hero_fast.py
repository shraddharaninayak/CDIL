import os

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')

with open('pages/ongoing-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('=== CONTEXT OF "hero" (offset 153666) ===')
print(html[153666-200:153666+200])

print('\n=== CONTEXT OF "slides" (offset 138966) ===')
print(html[138966-200:138966+200])

print('\n=== FINDING framer-1eht9vy in CSS ===')
idx = 0
while True:
    idx = html.find('framer-1eht9vy', idx)
    if idx == -1:
        break
    start = max(0, idx - 100)
    end = min(len(html), idx + 200)
    print(f'Match at {idx}:')
    print(html[start:end])
    idx += 14

print('\n=== FINDING framer-10dozng in CSS ===')
idx = 0
while True:
    idx = html.find('framer-10dozng', idx)
    if idx == -1:
        break
    start = max(0, idx - 100)
    end = min(len(html), idx + 200)
    print(f'Match at {idx}:')
    print(html[start:end])
    idx += 14
