import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

report_path = r"C:\Users\nshra\.gemini\antigravity\brain\007ee1d0-9729-45f4-9a80-ff5db8d72ad4\CDIL_WEBSITE_DELIVERY_REPORT.md"

with open(report_path, 'r', encoding='utf-8') as f:
    c = f.read()

update_entry = '''
### 16. Removal of "VIEW →" Link from Hero Featured Project Card
- **User Instruction**: Remove the "VIEW →" link from the floating hero featured project card without removing the card component itself.
- **Implementation**:
  - Removed the `VIEW →` text element and its associated horizontal divider line (`--border-top-width: 1px`) across all carousel slides (*Laxmi Pushp*, *3 Leaf Farmhouse*, *Watertouch*).
  - Adjusted the slide container height from fixed `118px` to `72px` to ensure the project title, location, and the slide indicator bars (`framer-1wgasjr`) maintain balanced spacing without residual empty whitespace.
  - Converted the outer card element to `cursor: default;` so it functions as an informational floating property badge without an active link.
  - Preserved the entire glass card component, its blurred backdrop styling, title, category, location, and slide progress indicators intact on [`index.html`](file:///d:/INTERNSHIPS/SOCIAL%20MEDIA%20MANANGMENT%5BSKILLNEX%5D/WEBSITES/CDIL-Constrution/index.html) and [`pages/page.html`](file:///d:/INTERNSHIPS/SOCIAL%20MEDIA%20MANANGMENT%5BSKILLNEX%5D/WEBSITES/CDIL-Constrution/pages/page.html).
'''

if '### 16. Removal of "VIEW →"' not in c:
    c = c.replace('## Final Verification Checklist', update_entry + '\n## Final Verification Checklist')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated delivery report artifact with item 16.")
else:
    print("Already in report.")

