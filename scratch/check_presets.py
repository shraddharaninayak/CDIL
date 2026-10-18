with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for preset in ['1jyh6nr', '159ll4e', '11shj4z']:
    pos = text.find(preset)
    if pos != -1:
        start = max(0, pos - 50)
        end = min(len(text), pos + 250)
        print(f"Preset {preset}:")
        print(text[start:end])
        print("=" * 40)
