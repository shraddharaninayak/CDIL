import os, sys, re, json

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('scratch/authentic_blogs.json', 'r', encoding='utf-8') as f:
    blogs = json.load(f)

# Categories and dates for the 16 blogs
METAS = [
    {"cat": "Real Estate Trends", "date": "Jan 18, 2025"},
    {"cat": "Investment Guide", "date": "Jan 05, 2025"},
    {"cat": "Nashik Market", "date": "Dec 22, 2024"},
    {"cat": "Legal & NA Titles", "date": "Dec 10, 2024"},
    {"cat": "Vastu & Architecture", "date": "Nov 28, 2024"},
    {"cat": "Farmhouse Hub", "date": "Nov 15, 2024"},
    {"cat": "Nature & Living", "date": "Oct 30, 2024"},
    {"cat": "Market Trends", "date": "Oct 12, 2024"},
    {"cat": "Deal Negotiation", "date": "Sep 25, 2024"},
    {"cat": "Tech & AI", "date": "Sep 08, 2024"},
    {"cat": "Farmer Certificate", "date": "Aug 20, 2024"},
    {"cat": "Kumbh Mela 2027", "date": "Aug 04, 2024"},
    {"cat": "Smart Infrastructure", "date": "Jul 19, 2024"},
    {"cat": "Vineyard Tourism", "date": "Jul 02, 2024"},
    {"cat": "Land Security", "date": "Jun 16, 2024"},
    {"cat": "Lifestyle & Growth", "date": "May 28, 2024"}
]

for i in range(len(blogs)):
    blogs[i]['cat'] = METAS[i]['cat']
    blogs[i]['date'] = METAS[i]['date']

def generate_blog_card_html(b, idx):
    return f'''<!--$--><a class="framer-sdggsy framer-f7ld5o cdil-blog-card" href="javascript:void(0)" onclick="openBlogModal({idx})" data-idx="{idx}"><div class="ssr-variant"><div class="framer-1m7zod3" data-framer-name="Cover"><div style="position:absolute;border-radius:inherit;corner-shape:inherit;top:0;right:0;bottom:0;left:0" data-framer-background-image-wrapper="true"><img decoding="auto" width="1600" height="1067" sizes="(min-width: 1440px) max((100vw - 160px) / 3, 280px), (max-width: 809.98px) max(100vw - 40px, 280px), (min-width: 810px) and (max-width: 1439.98px) max((100vw - 88px) / 2, 280px)" srcset="{b['img']}" src="{b['img']}" alt="{b['title']}" style="display:block;width:100%;height:100%;border-radius:inherit;corner-shape:inherit;object-position:center;object-fit:cover"></div></div></div><div class="framer-13x3m4h" data-framer-name="Meta"><div class="framer-e00v1v" data-framer-component-type="RichTextContainer" style="transform:none"><p class="framer-text framer-styles-preset-1ii2ixo" data-styles-preset="lxlcKskvm" dir="auto">{b['cat']}</p></div><div class="framer-143nwhj" data-framer-component-type="RichTextContainer" style="transform:none"><p class="framer-text framer-styles-preset-1ii2ixo" data-styles-preset="lxlcKskvm" dir="auto">·</p></div><div class="framer-1e4c3xe" data-framer-component-type="RichTextContainer" style="transform:none"><p class="framer-text framer-styles-preset-1ii2ixo" data-styles-preset="lxlcKskvm" dir="auto"><time>{b['date']}</time></p></div></div><div class="framer-7znp9z" data-framer-name="Title" data-framer-component-type="RichTextContainer" style="transform:none"><h3 class="framer-text framer-styles-preset-1c1kudq" data-styles-preset="ppMvKx6r4" dir="auto">{b['title']}</h3></div><div class="framer-1f5owst" data-framer-component-type="RichTextContainer" style="transform:none"><p class="framer-text framer-styles-preset-hijxov" data-styles-preset="Fm9TsQ8Q1" dir="auto">{b['desc']}</p></div></a><!--/$-->'''

cards_html = '\n'.join([generate_blog_card_html(b, i) for i, b in enumerate(blogs)])

with open('pages/journal.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Update page title
c = re.sub(r'<title>.*?</title>', '<title>CDIL Insights &amp; Real Estate Blog | Official Publications</title>', c)

# Update Eyebrow and Headings
c = c.replace('<p class="framer-text framer-styles-preset-1ii2ixo" data-styles-preset="lxlcKskvm" dir="auto">Journal</p>',
              '<p class="framer-text framer-styles-preset-1ii2ixo" data-styles-preset="lxlcKskvm" dir="auto">Insights &amp; Blog</p>')

old_h1_pattern = r'<h1 class="framer-text framer-styles-preset-1l78wyw"[^>]*>.*?</h1>'
new_h1 = '<h1 class="framer-text framer-styles-preset-1l78wyw" data-styles-preset="rjRfLOrK1" dir="auto">Articles, Guides &amp; Market Insights</h1>'
c = re.sub(old_h1_pattern, new_h1, c, flags=re.DOTALL)

# Locate the articles grid container
# Inside `<div class="framer-i8hefr" data-framer-name="Articles"><div class="framer-d0tomr"><!--$--><!--$-->`
grid_start = c.find('<div class="framer-i8hefr" data-framer-name="Articles"><div class="framer-d0tomr"><!--$--><!--$-->')
if grid_start == -1:
    print("Could not find Articles container in journal.html!")
    sys.exit(1)

cards_start = grid_start + len('<div class="framer-i8hefr" data-framer-name="Articles"><div class="framer-d0tomr"><!--$--><!--$-->')
cards_end = c.find('<!--/$--></div></div><div class="framer-fojgj7" data-framer-name="CTA">', cards_start)

if cards_end == -1:
    # Try finding CTA
    cards_end = c.find('<div class="framer-fojgj7" data-framer-name="CTA">', cards_start)
    # look back for the closing div
    cards_end = c.rfind('</div></div>', cards_start, cards_end)

print(f"Replacing journal cards from {cards_start} to {cards_end}")

json_blogs = json.dumps(blogs)

modal_html = f'''
<!-- CDIL Blog Reader Modal -->
<div id="cdilBlogModal" style="display: none; position: fixed; inset: 0; z-index: 999999; background: rgba(10, 14, 11, 0.94); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); justify-content: center; align-items: center; padding: 24px; box-sizing: border-box;">
  <div style="background: rgba(26, 38, 32, 0.95); border: 1px solid rgba(245, 242, 234, 0.2); border-radius: 20px; max-width: 820px; width: 100%; max-height: 88vh; overflow-y: auto; padding: 36px 32px; box-sizing: border-box; position: relative; color: rgb(245, 242, 234);">
    <button onclick="closeBlogModal()" style="position: absolute; top: 20px; right: 20px; background: rgba(245, 242, 234, 0.1); border: 1px solid rgba(245, 242, 234, 0.25); color: #fff; width: 40px; height: 40px; border-radius: 50%; font-size: 20px; cursor: pointer; display: grid; place-items: center; transition: background 0.25s;" title="Close">✕</button>
    <div style="margin-bottom: 20px; border-radius: 14px; overflow: hidden; max-height: 380px;">
      <img id="bmImg" src="" alt="Blog cover" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
    </div>
    <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 12px;">
      <span id="bmCat" style="background: rgba(53, 83, 63, 0.6); border: 1px solid rgba(245, 242, 234, 0.2); padding: 4px 12px; border-radius: 999px; font-family: Inter, sans-serif; font-size: 12px; text-transform: uppercase; letter-spacing: 0.08em;"></span>
      <span style="color: rgba(245,242,234,0.4);">·</span>
      <span id="bmDate" style="font-family: Inter, sans-serif; font-size: 13px; color: rgba(245, 242, 234, 0.6);"></span>
    </div>
    <h2 id="bmTitle" style="font-family: Fraunces, serif; font-size: clamp(24px, 3.5vw, 32px); font-weight: 300; line-height: 1.3; margin: 0 0 20px; color: rgb(245, 242, 234);"></h2>
    <div id="bmBody" style="font-family: Inter, sans-serif; font-size: 16px; line-height: 1.8; color: rgba(245, 242, 234, 0.85); white-space: pre-line;"></div>
    <div style="margin-top: 32px; padding-top: 24px; border-top: 1px solid rgba(245, 242, 234, 0.15); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
      <a href="./contact.html" style="background: rgb(245, 242, 234); color: rgb(26, 38, 32); text-decoration: none; padding: 12px 28px; border-radius: 999px; font-family: Inter, sans-serif; font-size: 14px; font-weight: 500; transition: transform 0.2s;">Inquire with CDIL Advisors →</a>
      <button onclick="closeBlogModal()" style="background: transparent; border: 1px solid rgba(245, 242, 234, 0.3); color: rgb(245, 242, 234); padding: 12px 24px; border-radius: 999px; font-family: Inter, sans-serif; font-size: 14px; cursor: pointer;">Close Article</button>
    </div>
  </div>
</div>

<script>
var cdilBlogs = {json_blogs};

function openBlogModal(idx) {{
  var b = cdilBlogs[idx];
  if (!b) return;
  var modal = document.getElementById('cdilBlogModal');
  document.getElementById('bmImg').src = b.img;
  document.getElementById('bmCat').textContent = b.cat;
  document.getElementById('bmDate').textContent = b.date;
  document.getElementById('bmTitle').textContent = b.title;
  document.getElementById('bmBody').textContent = b.desc;
  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
}}

function closeBlogModal() {{
  var modal = document.getElementById('cdilBlogModal');
  if (modal) modal.style.display = 'none';
  document.body.style.overflow = '';
}}

window.addEventListener('keydown', function(e) {{
  if (e.key === 'Escape') closeBlogModal();
}});
</script>
'''

c_new = c[:cards_start] + cards_html + c[cards_end:]
# inject modal before </body>
c_new = c_new.replace('</body></html>', modal_html + '\n</body></html>')

with open('pages/journal.html', 'w', encoding='utf-8') as f:
    f.write(c_new)

print(f"Updated pages/journal.html with {len(blogs)} authentic CDIL blog posts and reader modal!")

# Also update pages/blog.html to mirror journal.html
with open('pages/blog.html', 'w', encoding='utf-8') as f:
    f.write(c_new)

print("Updated pages/blog.html to mirror journal.html!")

