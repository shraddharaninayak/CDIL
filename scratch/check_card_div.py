with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('<div class="framer-gtXe7')
print("Card div found at:", start)
snippet = text[start:start+2500]
print(snippet)
