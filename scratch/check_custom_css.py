with open('index.html', 'r', encoding='utf-8-sig') as f:
    text = f.read()

import re

# Look for .cdil-why
why_css = re.search(r'/\* CDIL Why Choose Us Section \*/.*?</style>', text, re.DOTALL)
if why_css:
    print("Why Choose Us CSS:")
    print(why_css.group(0)[:1500])

# Look for footer styles
footer = re.search(r'data-framer-name="Footer".*?</div>\s*</div>\s*</div>', text, re.DOTALL)
if footer:
    print("\nFooter snippet:")
    print(footer.group(0)[:500])
