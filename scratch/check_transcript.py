import json

with open(r'C:\Users\nshra\.gemini\antigravity\brain\007ee1d0-9729-45f4-9a80-ff5db8d72ad4\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'USER_INPUT':
            txt = data.get('content', '')
            if 'hero' in txt.lower() or 'slideshow' in txt.lower() or 'remove this bg' in txt.lower() or 'bg from homepage' in txt.lower():
                print("USER INPUT:", txt[:200])
                print("-" * 40)
