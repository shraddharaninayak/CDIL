import os

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')

with open('pages/ongoing-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect all <style> blocks in ongoing-projects.html
import re
styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
print(f'Total styles: {len(styles)}')
for i, s in enumerate(styles):
    # Print the first 100 chars and last 100 chars of each style tag, plus length
    print(f'Style #{i}: length {len(s)}')
    # Let's search inside this style for anything matching '10dozng' or '1eht9vy' or 'CTA' or 'absolute' or 'fixed'
    for term in ['10dozng', '1eht9vy', 'CTA', 'Background Photo']:
        if term in s:
            print(f'   -> FOUND {term} in style #{i}!')
