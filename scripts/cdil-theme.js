(function () {
  'use strict';

  var STORAGE_KEY = 'cdil-theme';

  var SUN_SVG  = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6"/></svg>';
  var MOON_SVG = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';

  function getStoredTheme() {
    try { return localStorage.getItem(STORAGE_KEY); } catch (e) { return null; }
  }

  function setStoredTheme(theme) {
    try { localStorage.setItem(STORAGE_KEY, theme); } catch (e) {}
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
  }

  function currentTheme() {
    return document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
  }

  function updateBtn(btn, theme) {
    if (theme === 'light') {
      btn.innerHTML = MOON_SVG;
      btn.setAttribute('aria-label', 'Switch to night mode');
    } else {
      btn.innerHTML = SUN_SVG;
      btn.setAttribute('aria-label', 'Switch to bright mode');
    }
  }

  function initToggle() {
    var btn = document.querySelector(
      'button[aria-label="Switch to bright mode"], button[aria-label="Switch to night mode"],' +
      'button[aria-label="Switch to light mode"], button[aria-label="Switch to dark mode"]'
    );
    if (!btn) return;

    updateBtn(btn, currentTheme());

    btn.addEventListener('click', function () {
      var next = currentTheme() === 'light' ? 'dark' : 'light';
      applyTheme(next);
      updateBtn(btn, next);
      setStoredTheme(next);
    });
  }

  /* Apply stored theme immediately (head script may have already done this,
     but this catches any cases where the head script ran before body loaded) */
  var stored = getStoredTheme();
  if (stored) {
    applyTheme(stored);
  } else {
    /* No stored preference — detect OS preference and make it explicit
       so our CSS token overrides stay consistent */
    var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    applyTheme(prefersDark ? 'dark' : 'light');
  }

  /* Mobile submenu: intercept Projects link click to expand submenu */
  function initMobileSubmenu() {
    var overlay = document.getElementById('cdil-menu-overlay');
    if (!overlay) return;
    var submenuLinks = overlay.querySelectorAll('.cdil-has-submenu .cdil-menu-link');
    submenuLinks.forEach(function (link) {
      link.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        var item = link.closest('.cdil-has-submenu');
        if (!item) return;
        var isExp = item.classList.toggle('is-expanded');
        var toggle = item.querySelector('.cdil-submenu-toggle');
        if (toggle) toggle.setAttribute('aria-expanded', isExp ? 'true' : 'false');
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { initToggle(); initMobileSubmenu(); });
  } else {
    initToggle();
    initMobileSubmenu();
  }
})();
