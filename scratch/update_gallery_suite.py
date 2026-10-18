import os, sys, re, json

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

GALLERY_ITEMS = [
    # Amboli Van-Veli
    {"file": "av1.jpg", "category": "amboli", "cat_name": "Amboli Van-Veli", "title": "Riverside Farmhouse Estate", "loc": "Gunjal Farm, Amboli, Trimbakeshwar"},
    {"file": "av2.jpg", "category": "amboli", "cat_name": "Amboli Van-Veli", "title": "Green Countryside Plots", "loc": "Amboli Valley, Nashik"},
    {"file": "av4.png", "category": "amboli", "cat_name": "Amboli Van-Veli", "title": "Valley Mountain Horizon", "loc": "Trimbakeshwar Range, Nashik"},
    {"file": "av5.jpg", "category": "amboli", "cat_name": "Amboli Van-Veli", "title": "Plot Boundary & Orchard", "loc": "Amboli, Nashik"},
    {"file": "av7.jpg", "category": "amboli", "cat_name": "Amboli Van-Veli", "title": "Tree-Lined Internal Avenue", "loc": "Amboli Van-Veli Community"},
    {"file": "av.png", "category": "amboli", "cat_name": "Amboli Van-Veli", "title": "Master Layout & Landscape", "loc": "Amboli, Trimbakeshwar"},
    
    # Teakwood Farmhouse
    {"file": "teakwood1.jpeg", "category": "teakwood", "cat_name": "Teakwood Farmhouse", "title": "Finished Country Villa", "loc": "Wadivarhe, Nashik"},
    {"file": "tk3.jpeg", "category": "teakwood", "cat_name": "Teakwood Farmhouse", "title": "Timber Deck & Shaded Veranda", "loc": "Teakwood Farm Community"},
    {"file": "tk4.jpeg", "category": "teakwood", "cat_name": "Teakwood Farmhouse", "title": "Private Garden & Teak Grove", "loc": "Wadivarhe, Nashik"},
    {"file": "tk5.jpeg", "category": "teakwood", "cat_name": "Teakwood Farmhouse", "title": "Front Elevation & Manicured Lawn", "loc": "Teakwood Farm, Wadivarhe"},
    {"file": "tk6.jpeg", "category": "teakwood", "cat_name": "Teakwood Farmhouse", "title": "Outdoor Gazebo & Seating", "loc": "Teakwood Community"},
    {"file": "tk7.jpeg", "category": "teakwood", "cat_name": "Teakwood Farmhouse", "title": "Surrounding Nature Panorama", "loc": "Wadivarhe, Nashik"},
    
    # Watertouch Farmhouse
    {"file": "watertouch.jpeg", "category": "watertouch", "cat_name": "Watertouch Farmhouse", "title": "Direct Lakefront Living", "loc": "Mahiravni, Nashik"},
    {"file": "wt1.jpeg", "category": "watertouch", "cat_name": "Watertouch Farmhouse", "title": "Scenic Reservoir Edge", "loc": "Mahiravni Dam Waters"},
    {"file": "wt2.jpeg", "category": "watertouch", "cat_name": "Watertouch Farmhouse", "title": "Tranquil Water Shoreline", "loc": "Mahiravni, Nashik"},
    {"file": "wt3.jpeg", "category": "watertouch", "cat_name": "Watertouch Farmhouse", "title": "Sunset Reflections Across Water", "loc": "Watertouch Project"},
    {"file": "wt4.jpeg", "category": "watertouch", "cat_name": "Watertouch Farmhouse", "title": "Lush Greenery By The Water", "loc": "Mahiravni, Nashik"},
    {"file": "wt5.jpeg", "category": "watertouch", "cat_name": "Watertouch Farmhouse", "title": "Panoramic Dam View", "loc": "Mahiravni Reservoir, Nashik"},
    
    # River Ranch
    {"file": "riverranch.jpeg", "category": "riverranch", "cat_name": "River Ranch", "title": "Riverfront Estate Living", "loc": "Khambale, Girna River"},
    {"file": "rvr11.jpg", "category": "riverranch", "cat_name": "River Ranch", "title": "Flowing Girna Riverbank Plots", "loc": "Khambale, Nashik"},
    {"file": "rr2.jpg", "category": "riverranch", "cat_name": "River Ranch", "title": "Riparian Countryside Vista", "loc": "River Ranch Project"},
    {"file": "khand.jpg", "category": "riverranch", "cat_name": "River Ranch", "title": "Open Horizons & River Shore", "loc": "Khambale, Nashik"},
    
    # Mountain Bliss
    {"file": "mb1.jpeg", "category": "mountainbliss", "cat_name": "Mountain Bliss", "title": "Cone Dam View Panorama", "loc": "Cone Dam View, Vaghera"},
    {"file": "mb2.jpeg", "category": "mountainbliss", "cat_name": "Mountain Bliss", "title": "Mountain Peaks & Morning Mist", "loc": "Vaghera Hills, Nashik"},
    {"file": "mb4.jpeg", "category": "mountainbliss", "cat_name": "Mountain Bliss", "title": "Elevated Countryside Plot", "loc": "Mountain Bliss Project"},
    {"file": "hills.jpeg", "category": "mountainbliss", "cat_name": "Mountain Bliss", "title": "Vaghera Mountain Ridge", "loc": "Cone Dam View, Nashik"}
]

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Update page title
c = re.sub(r'<title>.*?</title>', '<title>Project Gallery | CDIL Real Estate &amp; Infrastructure</title>', c)

# Update Page Head heading and description
c = c.replace('<p class="framer-text framer-styles-preset-1ii2ixo" data-styles-preset="lxlcKskvm" dir="auto">About</p>',
              '<p class="framer-text framer-styles-preset-1ii2ixo" data-styles-preset="lxlcKskvm" dir="auto">Gallery</p>')

old_h1_pattern = r'<h1 class="framer-text framer-styles-preset-1l78wyw"[^>]*>.*?</h1>'
new_h1 = '<h1 class="framer-text framer-styles-preset-1l78wyw" data-styles-preset="rjRfLOrK1" dir="auto">Authentic Project Gallery</h1>'
c = re.sub(old_h1_pattern, new_h1, c, flags=re.DOTALL)

old_desc = 'CDIL Real Estate & Infrastructure was founded in 2008 in Nashik with a simple mission: help families find the perfect plot or farmhouse in scenic locations around Maharashtra.'
new_desc = 'Explore authentic photographs from CDIL’s signature farmhouse developments, lakeside retreats, and countryside plot communities across Nashik and Trimbakeshwar.'
c = c.replace(old_desc, new_desc)

# Generate gallery filter buttons
filter_bar_html = '''
<div class="cdil-gallery-filter-wrap" style="max-width: 1200px; margin: 0 auto 36px; padding: 0 32px; display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; box-sizing: border-box;">
  <button type="button" class="cdil-gal-btn is-active" data-gal-filter="all">All Projects (26)</button>
  <button type="button" class="cdil-gal-btn" data-gal-filter="amboli">Amboli Van-Veli (6)</button>
  <button type="button" class="cdil-gal-btn" data-gal-filter="teakwood">Teakwood Farmhouse (6)</button>
  <button type="button" class="cdil-gal-btn" data-gal-filter="watertouch">Watertouch Farmhouse (6)</button>
  <button type="button" class="cdil-gal-btn" data-gal-filter="riverranch">River Ranch (4)</button>
  <button type="button" class="cdil-gal-btn" data-gal-filter="mountainbliss">Mountain Bliss (4)</button>
</div>
'''

cards_html_list = []
for idx, item in enumerate(GALLERY_ITEMS):
    img_path = f"../images/cdil/gallery/{item['file']}"
    card = f'''
    <div class="cdil-gal-card" data-gal-cat="{item['category']}" data-idx="{idx}" style="cursor: pointer; background: rgba(12, 16, 12, 0.42); border: 1px solid rgba(245, 242, 234, 0.16); border-radius: 16px; overflow: hidden; backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); transition: transform 0.35s ease, border-color 0.35s ease, box-shadow 0.35s ease;">
      <div style="position: relative; width: 100%; height: 260px; overflow: hidden;">
        <img src="{img_path}" alt="{item['title']} — {item['cat_name']}" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.5s cubic-bezier(0.22, 0.61, 0.36, 1);" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform='scale(1)'" />
        <div style="position: absolute; top: 12px; left: 12px; background: rgba(12, 16, 12, 0.65); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); border: 1px solid rgba(245, 242, 234, 0.22); border-radius: 999px; padding: 4px 12px;">
          <span style="font-family: Inter, sans-serif; font-size: 11px; letter-spacing: 0.05em; color: rgb(245, 242, 234);">{item['cat_name']}</span>
        </div>
      </div>
      <div style="padding: 20px;">
        <h4 style="font-family: Fraunces, serif; font-size: 19px; font-weight: 300; margin: 0 0 6px; color: rgb(245, 242, 234); letter-spacing: -0.01em;">{item['title']}</h4>
        <p style="font-family: Inter, sans-serif; font-size: 13px; color: rgba(245, 242, 234, 0.65); margin: 0;">{item['loc']}</p>
      </div>
    </div>
    '''
    cards_html_list.append(card)

cards_grid_html = '\n'.join(cards_html_list)

json_items = json.dumps(GALLERY_ITEMS)

gallery_section_html = f'''
<div class="cdil-custom-body" style="padding: 40px 32px 90px; max-width: 1300px; margin: 0 auto; box-sizing: border-box;">
  {filter_bar_html}
  <div id="cdilGalleryGrid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(330px, 1fr)); gap: 26px;">
    {cards_grid_html}
  </div>
</div>

<!-- CDIL Lightbox Modal -->
<div id="cdilLightbox" class="cdil-lightbox" style="display: none; position: fixed; inset: 0; z-index: 999999; background: rgba(10, 14, 11, 0.94); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); justify-content: center; align-items: center; padding: 24px; box-sizing: border-box;">
  <button id="cdilLbClose" style="position: absolute; top: 24px; right: 28px; background: rgba(245, 242, 234, 0.1); border: 1px solid rgba(245, 242, 234, 0.25); color: #fff; width: 44px; height: 44px; border-radius: 50%; font-size: 24px; cursor: pointer; display: grid; place-items: center; transition: background 0.25s;" title="Close (Esc)">✕</button>
  <button id="cdilLbPrev" style="position: absolute; left: 24px; top: 50%; transform: translateY(-50%); background: rgba(245, 242, 234, 0.1); border: 1px solid rgba(245, 242, 234, 0.25); color: #fff; width: 50px; height: 50px; border-radius: 50%; font-size: 24px; cursor: pointer; display: grid; place-items: center; transition: background 0.25s;" title="Previous">‹</button>
  <button id="cdilLbNext" style="position: absolute; right: 24px; top: 50%; transform: translateY(-50%); background: rgba(245, 242, 234, 0.1); border: 1px solid rgba(245, 242, 234, 0.25); color: #fff; width: 50px; height: 50px; border-radius: 50%; font-size: 24px; cursor: pointer; display: grid; place-items: center; transition: background 0.25s;" title="Next">›</button>
  
  <div style="max-width: 1000px; width: 100%; display: flex; flex-direction: column; align-items: center; gap: 16px;">
    <div style="max-height: 75vh; max-width: 100%; overflow: hidden; border-radius: 12px; border: 1px solid rgba(245, 242, 234, 0.2);">
      <img id="cdilLbImg" src="" alt="Enlarged view" style="max-width: 100%; max-height: 75vh; object-fit: contain; display: block;" />
    </div>
    <div style="text-align: center; color: #f5f2ea;">
      <h3 id="cdilLbTitle" style="font-family: Fraunces, serif; font-size: 22px; font-weight: 300; margin: 0 0 4px;"></h3>
      <p id="cdilLbMeta" style="font-family: Inter, sans-serif; font-size: 14px; color: rgba(245, 242, 234, 0.7); margin: 0;"></p>
    </div>
  </div>
</div>

<style>
.cdil-gal-btn {{
  background: transparent;
  color: rgba(26, 38, 32, 0.75);
  border: 1px solid rgba(26, 38, 32, 0.2);
  font-family: Inter, sans-serif;
  font-size: 14px;
  font-weight: 400;
  padding: 8px 18px;
  border-radius: 999px;
  cursor: pointer;
  transition: all 0.25s ease;
}}
.cdil-gal-btn:hover {{
  border-color: rgb(26, 38, 32);
  color: rgb(26, 38, 32);
}}
.cdil-gal-btn.is-active {{
  background: rgb(26, 38, 32);
  color: rgb(243, 239, 228);
  border-color: rgb(26, 38, 32);
}}
.cdil-gal-card:hover {{
  transform: translateY(-4px);
  border-color: rgba(245, 242, 234, 0.45) !important;
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.35);
}}
#cdilLbClose:hover, #cdilLbPrev:hover, #cdilLbNext:hover {{
  background: rgba(245, 242, 234, 0.22) !important;
}}
</style>

<script>
(function() {{
  var items = {json_items};
  var currentIdx = 0;
  var visibleIndices = [];

  function updateVisibleIndices(cat) {{
    visibleIndices = [];
    items.forEach(function(item, idx) {{
      if (cat === 'all' || item.category === cat) {{
        visibleIndices.push(idx);
      }}
    }});
  }}
  updateVisibleIndices('all');

  var filterBtns = document.querySelectorAll('.cdil-gal-btn');
  var cards = document.querySelectorAll('.cdil-gal-card');

  filterBtns.forEach(function(btn) {{
    btn.addEventListener('click', function() {{
      filterBtns.forEach(function(b) {{ b.classList.remove('is-active'); }});
      btn.classList.add('is-active');
      var cat = btn.getAttribute('data-gal-filter');
      updateVisibleIndices(cat);
      cards.forEach(function(c) {{
        if (cat === 'all' || c.getAttribute('data-gal-cat') === cat) {{
          c.style.display = '';
        }} else {{
          c.style.display = 'none';
        }}
      }});
    }});
  }});

  var modal = document.getElementById('cdilLightbox');
  var lbImg = document.getElementById('cdilLbImg');
  var lbTitle = document.getElementById('cdilLbTitle');
  var lbMeta = document.getElementById('cdilLbMeta');
  var lbClose = document.getElementById('cdilLbClose');
  var lbPrev = document.getElementById('cdilLbPrev');
  var lbNext = document.getElementById('cdilLbNext');

  function openLightbox(idx) {{
    currentIdx = idx;
    var it = items[idx];
    lbImg.src = '../images/cdil/gallery/' + it.file;
    lbTitle.textContent = it.title;
    lbMeta.textContent = it.cat_name + ' · ' + it.loc;
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }}

  function closeLightbox() {{
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }}

  function showNext() {{
    var pos = visibleIndices.indexOf(currentIdx);
    if (pos === -1) pos = 0;
    var nextPos = (pos + 1) % visibleIndices.length;
    openLightbox(visibleIndices[nextPos]);
  }}

  function showPrev() {{
    var pos = visibleIndices.indexOf(currentIdx);
    if (pos === -1) pos = 0;
    var prevPos = (pos - 1 + visibleIndices.length) % visibleIndices.length;
    openLightbox(visibleIndices[prevPos]);
  }}

  cards.forEach(function(c) {{
    c.addEventListener('click', function() {{
      var idx = parseInt(c.getAttribute('data-idx'), 10);
      openLightbox(idx);
    }});
  }});

  if (lbClose) lbClose.addEventListener('click', closeLightbox);
  if (lbNext) lbNext.addEventListener('click', showNext);
  if (lbPrev) lbPrev.addEventListener('click', showPrev);

  if (modal) {{
    modal.addEventListener('click', function(e) {{
      if (e.target === modal) closeLightbox();
    }});
  }}

  window.addEventListener('keydown', function(e) {{
    if (modal && modal.style.display === 'flex') {{
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowRight') showNext();
      if (e.key === 'ArrowLeft') showPrev();
    }}
  }});
}})();
</script>
'''

start_body_pos = c.find('<div class="cdil-custom-body"')
cta_pos = c.find('<div class="framer-1eht9vy" data-framer-name="CTA">')

c_new = c[:start_body_pos] + gallery_section_html + c[cta_pos:]

with open('pages/gallery.html', 'w', encoding='utf-8') as f:
    f.write(c_new)

print("Updated pages/gallery.html with full 26 authentic CDIL project images, filters, and lightbox!")

