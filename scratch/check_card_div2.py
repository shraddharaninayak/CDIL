with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('framer-25sh2b')
print(text[start:start+1500])
