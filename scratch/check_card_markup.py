with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('framer-gtXe7')
print(text[start:start+3500])
