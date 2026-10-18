import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    g = f.read()

cta_idx = g.find('<div class="framer-1eht9vy" data-framer-name="CTA">')
common_tail = g[cta_idx:]

filter_script = '''
<script>
/* CDIL Interactive Project Status Filter */
(function() {
  function initProjectFilters() {
    var buttons = document.querySelectorAll('.rf-c-R6malp[data-filter]');
    var cards = document.querySelectorAll('[data-cdil-project]');

    function filterBy(status) {
      status = (status || 'all').toLowerCase();
      buttons.forEach(function(btn) {
        var btnFilter = btn.getAttribute('data-filter');
        var isActive = (btnFilter === status);
        btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
        if (isActive) {
          btn.style.background = 'var(--token-025422ea-d283-4879-b332-741cb1c834c7, rgb(26, 38, 32))';
          btn.style.color = 'var(--token-ed5af0b1-8875-4b9b-a8d0-dd29f7c8c608, rgb(243, 239, 228))';
          btn.style.borderColor = 'var(--token-025422ea-d283-4879-b332-741cb1c834c7, rgb(26, 38, 32))';
        } else {
          btn.style.background = 'transparent';
          btn.style.color = 'var(--token-b8cfd3da-418b-4999-a7f7-4bf97baf1624, rgba(26, 38, 32, 0.74))';
          btn.style.borderColor = 'var(--token-d34888b7-6c91-4dbc-95a1-370fba2352b1, rgba(26, 38, 32, 0.16))';
        }
      });

      cards.forEach(function(card) {
        var cardStatus = card.getAttribute('data-cdil-status');
        if (status === 'all' || cardStatus === status) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    }

    buttons.forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        var f = btn.getAttribute('data-filter');
        window.location.hash = (f === 'all') ? '' : f;
        filterBy(f);
      });
    });

    var hash = window.location.hash.replace('#', '').toLowerCase();
    if (hash === 'ongoing' || hash === 'completed' || hash === 'upcoming') {
      filterBy(hash);
    }

    window.addEventListener('hashchange', function() {
      var h = window.location.hash.replace('#', '').toLowerCase();
      if (h === 'ongoing' || h === 'completed' || h === 'upcoming' || h === '') {
        filterBy(h || 'all');
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initProjectFilters);
  } else {
    initProjectFilters();
  }
})();
</script>
'''

# append filter_script right before </body>
tail_with_filter = common_tail.replace('</body></html>', filter_script + '\n</body></html>')

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    curr_p = f.read()

# in curr_p, the last card ends at:
last_card_end = curr_p.rfind('<!--/$-->') + len('<!--/$-->')
print("Current projects head to last card end:", last_card_end)

assembled = curr_p[:last_card_end] + '</div></div></div>' + tail_with_filter

with open('pages/projects.html', 'w', encoding='utf-8') as f:
    f.write(assembled)

print("Successfully reconstructed pages/projects.html! New length:", len(assembled))

