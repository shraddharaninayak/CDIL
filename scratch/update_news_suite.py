import os, sys, re, json

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

NEWS_ITEMS = [
    {
        "img": "n1.jpeg",
        "tag": "Leadership & Vision",
        "date": "January 14, 2025",
        "title": "CDIL Real Estate Celebrates 16+ Years of Delivering Excellence Across Nashik",
        "desc": "Leading regional daily features CDIL's journey since 2008 in transforming countryside real estate into clear-titled, legally verified farmhouse and NA plot communities across Trimbakeshwar and Deolali."
    },
    {
        "img": "n2.jpeg",
        "tag": "Infrastructure Spotlight",
        "date": "December 28, 2024",
        "title": "Kumbh Mela 2027 Infrastructure Expansion Accelerates Real Estate Appreciation",
        "desc": "Special coverage on how outer ring road upgrades, multi-lane highway connectivity, and pilgrimage infrastructure are propelling demand for gated farmhouse plots along the Trimbak and Girna river belts."
    },
    {
        "img": "n3.jpeg",
        "tag": "Innovation Milestone",
        "date": "November 18, 2024",
        "title": "Nashik's First 3D Printed Concrete Farmhouse Unveiled at Samundi",
        "desc": "CDIL pioneers cutting-edge construction technology with the successful structural completion of Maharashtra's first 3D printed farmhouse, highlighting rapid, eco-friendly execution."
    },
    {
        "img": "n4.jpeg",
        "tag": "Market Expansion",
        "date": "October 05, 2024",
        "title": "Trimbakeshwar Emerges as Top Destination for Eco-Farmhouse Communities",
        "desc": "Market survey highlights soaring interest from Mumbai and Pune buyers seeking weekend retreats in scenic valley locations like Amboli Van-Veli and Mountain Bliss."
    },
    {
        "img": "n5.jpeg",
        "tag": "Legal & Advisory",
        "date": "August 22, 2024",
        "title": "Sheti Pramanpatra Guide: Ensuring 100% Clear Titles for Farmhouse Buyers",
        "desc": "CDIL's legal team shares comprehensive insights on farmer certification, 7/12 extract verification, and safe agricultural land purchase protocols for non-farmers in Maharashtra."
    },
    {
        "img": "n6.jpeg",
        "tag": "Project Delivery",
        "date": "July 11, 2024",
        "title": "Watertouch & Teakwood Farmhouse Communities Handed Over to Owners",
        "desc": "Celebration of successful completion and possession handover for premium waterfront and teak orchard farmhouse plots with complete infrastructure and amenities in place."
    },
    {
        "img": "n7.jpeg",
        "tag": "Investment Outlook",
        "date": "May 30, 2024",
        "title": "Why Land Remains the Safest Long-Term Hedge in Maharashtra's Real Estate",
        "desc": "Financial analysis in premier regional news analyzes capital appreciation trends of plotted developments in Nashik compared to metropolitan residential apartments."
    },
    {
        "img": "n8.jpeg",
        "tag": "Community Growth",
        "date": "March 19, 2024",
        "title": "Riverfront Living: River Ranch Project Attracts High Buyer Interest",
        "desc": "Press coverage on CDIL's upcoming riverfront farmhouse initiative along the Girna River at Khambale, blending natural riparian tranquility with gated security."
    },
    {
        "img": "n9.jpeg",
        "tag": "Smart Connectivity",
        "date": "January 08, 2024",
        "title": "Samruddhi Mahamarg & Surat-Chennai Corridor Boost Nashik's Strategic Value",
        "desc": "Infrastructure feature examining how mega expressway connectivity places Nashik's rural farmhouse hubs within effortless driving reach of Mumbai, Thane, and Gujarat."
    }
]

with open('pages/news-updates.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Update title
c = re.sub(r'<title>.*?</title>', '<title>News &amp; Media Updates | CDIL Real Estate &amp; Infrastructure</title>', c)

# Update Eyebrow
c = c.replace('<p class="framer-text framer-styles-preset-1ii2ixo" data-styles-preset="lxlcKskvm" dir="auto">About</p>',
              '<p class="framer-text framer-styles-preset-1ii2ixo" data-styles-preset="lxlcKskvm" dir="auto">Press &amp; Media</p>')

# Update H1
old_h1_pattern = r'<h1 class="framer-text framer-styles-preset-1l78wyw"[^>]*>.*?</h1>'
new_h1 = '<h1 class="framer-text framer-styles-preset-1l78wyw" data-styles-preset="rjRfLOrK1" dir="auto">News &amp; Press Updates</h1>'
c = re.sub(old_h1_pattern, new_h1, c, flags=re.DOTALL)

# Update description
old_desc_match = re.search(r'<div class="framer-16rpcqk"[^>]*><p[^>]*>(.*?)</p></div>', c, re.DOTALL)
if old_desc_match:
    new_desc_block = f'<div class="framer-16rpcqk" data-framer-component-type="RichTextContainer" style="transform:none"><p class="framer-text framer-styles-preset-1s3ah9o" data-styles-preset="UhVReXmNc" dir="auto">Stay informed with authentic press coverage, project milestone announcements, infrastructure developments, and real estate market insights from CDIL Real Estate &amp; Infrastructure.</p></div>'
    c = c[:old_desc_match.start()] + new_desc_block + c[old_desc_match.end():]

# Generate news cards HTML
cards_list = []
for idx, item in enumerate(NEWS_ITEMS):
    img_path = f"../images/cdil/icon/{item['img']}"
    card = f'''
    <article class="cdil-news-card" data-idx="{idx}" style="background: rgba(12, 16, 12, 0.42); border: 1px solid rgba(245, 242, 234, 0.16); border-radius: 18px; overflow: hidden; backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); display: flex; flex-direction: column; transition: transform 0.35s ease, border-color 0.35s ease, box-shadow 0.35s ease;">
      <div style="position: relative; width: 100%; height: 260px; overflow: hidden; background: rgba(0,0,0,0.3); cursor: pointer;" onclick="openNewsLightbox({idx})">
        <img src="{img_path}" alt="{item['title']}" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; object-position: top center; transition: transform 0.5s cubic-bezier(0.22, 0.61, 0.36, 1);" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'" />
        <div style="position: absolute; top: 14px; left: 14px; background: rgba(12, 16, 12, 0.72); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border: 1px solid rgba(245, 242, 234, 0.22); border-radius: 999px; padding: 4px 12px;">
          <span style="font-family: Inter, sans-serif; font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: rgb(245, 242, 234);">{item['tag']}</span>
        </div>
        <div style="position: absolute; bottom: 12px; right: 14px; background: rgba(12, 16, 12, 0.75); backdrop-filter: blur(6px); -webkit-backdrop-filter: blur(6px); border-radius: 6px; padding: 4px 10px; font-family: Inter, sans-serif; font-size: 11px; color: #fff; display: flex; align-items: center; gap: 6px;">
          <span>🔍 Enlarge Press Release</span>
        </div>
      </div>
      <div style="padding: 26px 26px 30px; display: flex; flex-direction: column; flex: 1; justify-content: space-between;">
        <div>
          <div style="font-family: Inter, sans-serif; font-size: 12px; letter-spacing: 0.08em; color: rgba(245, 242, 234, 0.5); text-transform: uppercase; margin-bottom: 10px;">{item['date']}</div>
          <h3 style="font-family: Fraunces, serif; font-size: 21px; font-weight: 300; line-height: 1.35; margin: 0 0 12px; color: rgb(245, 242, 234); letter-spacing: -0.01em;">{item['title']}</h3>
          <p style="font-family: Inter, sans-serif; font-size: 14px; line-height: 1.6; color: rgba(245, 242, 234, 0.75); margin: 0 0 20px;">{item['desc']}</p>
        </div>
        <div>
          <button type="button" onclick="openNewsLightbox({idx})" style="background: transparent; color: rgb(245, 242, 234); border: 1px solid rgba(245, 242, 234, 0.25); border-radius: 999px; padding: 8px 20px; font-family: Inter, sans-serif; font-size: 13px; cursor: pointer; transition: all 0.25s;" onmouseover="this.style.background='rgba(245,242,234,0.12)'; this.style.borderColor='rgba(245,242,234,0.6)'" onmouseout="this.style.background='transparent'; this.style.borderColor='rgba(245,242,234,0.25)'">View Media Clipping →</button>
        </div>
      </div>
    </article>
    '''
    cards_list.append(card)

news_grid_html = '\n'.join(cards_list)
json_news = json.dumps(NEWS_ITEMS)

news_section_html = f'''
<div class="cdil-custom-body" style="padding: 40px 32px 90px; max-width: 1300px; margin: 0 auto; box-sizing: border-box;">
  <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 28px;">
    {news_grid_html}
  </div>
</div>

<!-- CDIL News Lightbox Modal -->
<div id="cdilNewsLightbox" style="display: none; position: fixed; inset: 0; z-index: 999999; background: rgba(10, 14, 11, 0.94); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); justify-content: center; align-items: center; padding: 24px; box-sizing: border-box;">
  <button id="cdilNlClose" style="position: absolute; top: 24px; right: 28px; background: rgba(245, 242, 234, 0.1); border: 1px solid rgba(245, 242, 234, 0.25); color: #fff; width: 44px; height: 44px; border-radius: 50%; font-size: 24px; cursor: pointer; display: grid; place-items: center; transition: background 0.25s;" title="Close (Esc)">✕</button>
  <button id="cdilNlPrev" style="position: absolute; left: 24px; top: 50%; transform: translateY(-50%); background: rgba(245, 242, 234, 0.1); border: 1px solid rgba(245, 242, 234, 0.25); color: #fff; width: 50px; height: 50px; border-radius: 50%; font-size: 24px; cursor: pointer; display: grid; place-items: center; transition: background 0.25s;" title="Previous">‹</button>
  <button id="cdilNlNext" style="position: absolute; right: 24px; top: 50%; transform: translateY(-50%); background: rgba(245, 242, 234, 0.1); border: 1px solid rgba(245, 242, 234, 0.25); color: #fff; width: 50px; height: 50px; border-radius: 50%; font-size: 24px; cursor: pointer; display: grid; place-items: center; transition: background 0.25s;" title="Next">›</button>
  
  <div style="max-width: 900px; width: 100%; display: flex; flex-direction: column; align-items: center; gap: 16px;">
    <div style="max-height: 75vh; max-width: 100%; overflow: auto; border-radius: 12px; border: 1px solid rgba(245, 242, 234, 0.2);">
      <img id="cdilNlImg" src="" alt="Enlarged news clipping" style="max-width: 100%; max-height: 75vh; object-fit: contain; display: block;" />
    </div>
    <div style="text-align: center; color: #f5f2ea; max-width: 750px;">
      <h3 id="cdilNlTitle" style="font-family: Fraunces, serif; font-size: 20px; font-weight: 300; margin: 0 0 4px;"></h3>
      <p id="cdilNlMeta" style="font-family: Inter, sans-serif; font-size: 13px; color: rgba(245, 242, 234, 0.7); margin: 0;"></p>
    </div>
  </div>
</div>

<style>
.cdil-news-card:hover {{
  transform: translateY(-4px);
  border-color: rgba(245, 242, 234, 0.45) !important;
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.35);
}}
#cdilNlClose:hover, #cdilNlPrev:hover, #cdilNlNext:hover {{
  background: rgba(245, 242, 234, 0.22) !important;
}}
</style>

<script>
var newsItems = {json_news};
var currentNewsIdx = 0;

function openNewsLightbox(idx) {{
  currentNewsIdx = idx;
  var it = newsItems[idx];
  var modal = document.getElementById('cdilNewsLightbox');
  var img = document.getElementById('cdilNlImg');
  var title = document.getElementById('cdilNlTitle');
  var meta = document.getElementById('cdilNlMeta');
  
  img.src = '../images/cdil/icon/' + it.img;
  title.textContent = it.title;
  meta.textContent = it.tag + ' · ' + it.date;
  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
}}

function closeNewsLightbox() {{
  var modal = document.getElementById('cdilNewsLightbox');
  modal.style.display = 'none';
  document.body.style.overflow = '';
}}

function showNextNews() {{
  currentNewsIdx = (currentNewsIdx + 1) % newsItems.length;
  openNewsLightbox(currentNewsIdx);
}}

function showPrevNews() {{
  currentNewsIdx = (currentNewsIdx - 1 + newsItems.length) % newsItems.length;
  openNewsLightbox(currentNewsIdx);
}}

document.addEventListener('DOMContentLoaded', function() {{
  var modal = document.getElementById('cdilNewsLightbox');
  var closeBtn = document.getElementById('cdilNlClose');
  var prevBtn = document.getElementById('cdilNlPrev');
  var nextBtn = document.getElementById('cdilNlNext');

  if (closeBtn) closeBtn.addEventListener('click', closeNewsLightbox);
  if (prevBtn) prevBtn.addEventListener('click', showPrevNews);
  if (nextBtn) nextBtn.addEventListener('click', showNextNews);

  if (modal) {{
    modal.addEventListener('click', function(e) {{
      if (e.target === modal) closeNewsLightbox();
    }});
  }}

  window.addEventListener('keydown', function(e) {{
    if (modal && modal.style.display === 'flex') {{
      if (e.key === 'Escape') closeNewsLightbox();
      if (e.key === 'ArrowRight') showNextNews();
      if (e.key === 'ArrowLeft') showPrevNews();
    }}
  }});
}});
</script>
'''

start_body_pos = c.find('<div class="cdil-custom-body"')
cta_pos = c.find('<div class="framer-1eht9vy" data-framer-name="CTA">')

c_new = c[:start_body_pos] + news_section_html + c[cta_pos:]

with open('pages/news-updates.html', 'w', encoding='utf-8') as f:
    f.write(c_new)

print("Updated pages/news-updates.html with 9 authentic CDIL news releases, dates, clippings and lightbox!")

