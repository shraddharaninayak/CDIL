with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect where hero background is in index.html
start = text.find('data-framer-name="Hero"')
print("Found Hero at:", start)
snippet = text[start:start+4000]
print(snippet[:2500])
