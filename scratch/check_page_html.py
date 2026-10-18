with open('pages/page.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("page.html length:", len(text))
print("Hero in page.html:", 'data-framer-name="Hero"' in text)
print("Card in page.html:", 'framer-gtXe7' in text)
