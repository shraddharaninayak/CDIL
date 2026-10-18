with open('index.html', 'r', encoding='utf-8-sig') as f:
    text = f.read()

pos = text.find('.cdil-why-choose-us')
if pos != -1:
    print("Found .cdil-why-choose-us at", pos)
    print(text[pos:pos+800].encode('ascii', 'ignore').decode('ascii'))
