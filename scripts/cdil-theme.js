(function () {
  var SUN_SVG = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="4.2" /><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6" /></svg>';
  var MOON_SVG = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    try { localStorage.setItem('cdil-theme', theme); } catch (e) {}
  }

  function updateButton(btn, theme) {
    if (theme === 'dark') {
      btn.innerHTML = SUN_SVG;
      btn.setAttribute('aria-label', 'Switch to light mode');
    } else {
      btn.innerHTML = MOON_SVG;
      btn.setAttribute('aria-label', 'Switch to dark mode');
    }
  }

  function init() {
    var saved;
    try { saved = localStorage.getItem('cdil-theme'); } catch (e) {}
    var theme = saved || 'dark';
    applyTheme(theme);

    var btns = document.querySelectorAll(
      'button[aria-label="Switch to light mode"], button[aria-label="Switch to dark mode"]'
    );
    btns.forEach(function (btn) {
      updateButton(btn, theme);
      btn.addEventListener('click', function () {
        var current = document.documentElement.getAttribute('data-theme') || 'dark';
        var next = current === 'dark' ? 'light' : 'dark';
        applyTheme(next);
        btns.forEach(function (b) { updateButton(b, next); });
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
