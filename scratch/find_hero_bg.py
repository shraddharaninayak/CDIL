with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'ZiuHJRK3VDqMlK0bXLemGXGx8o.jpg' in line:
        print(f"Line {idx+1}:")
        start = max(0, idx - 5)
        end = min(len(lines), idx + 10)
        for j in range(start, end):
            print(f"  {j+1}: {lines[j][:160]}")
        print("="*60)
