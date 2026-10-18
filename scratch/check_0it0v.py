with open('index.html', 'r', encoding='utf-8-sig') as f:
    text = f.read()

pos = text.find('.framer-0It0v{')
if pos != -1:
    print(text[pos:pos+300])
