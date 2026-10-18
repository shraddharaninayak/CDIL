with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.rfind('</body>')
print(text[max(0, pos-1500):pos+7].encode('ascii', 'ignore').decode('ascii'))
