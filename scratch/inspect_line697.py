with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

line697 = content.splitlines()[696] # 0-indexed

idx = 0
matches = []
while True:
    pos = line697.find('ZiuHJRK3VDqMlK0bXLemGXGx8o.jpg', idx)
    if pos == -1:
        break
    matches.append(pos)
    idx = pos + 1

print(f"Total matches in line 697: {len(matches)}")
for pos in matches:
    start = max(0, pos - 150)
    end = min(len(line697), pos + 150)
    print("Match at", pos)
    print(line697[start:end])
    print("-" * 50)
