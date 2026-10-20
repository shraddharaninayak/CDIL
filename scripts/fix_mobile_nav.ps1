# Fix 1: Mobile nav Projects dropdown + Fix 2: Submenu link destinations + Fix 3: Responsive layout

$base = "D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT`[SKILLNEX`]\WEBSITES\CDIL-Constrution"

# ── JS snippet to insert after the submenuToggles.forEach block ─────────────
$jsInsertAfter = @'
    submenuToggles.forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        var parentItem = btn.closest('.cdil-has-submenu');
        if (parentItem) {
          var isExp = parentItem.classList.toggle('is-expanded');
          btn.setAttribute('aria-expanded', isExp ? 'true' : 'false');
        }
      });
    });
'@

$jsNewBlock = @'
    submenuToggles.forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        var parentItem = btn.closest('.cdil-has-submenu');
        if (parentItem) {
          var isExp = parentItem.classList.toggle('is-expanded');
          btn.setAttribute('aria-expanded', isExp ? 'true' : 'false');
        }
      });
    });

    // Intercept parent nav links that have submenus — expand instead of navigate
    var submenuParentLinks = overlay.querySelectorAll('.cdil-has-submenu .cdil-menu-link');
    submenuParentLinks.forEach(function(link) {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        var parentItem = link.closest('.cdil-has-submenu');
        if (parentItem) {
          var toggleBtn = parentItem.querySelector('.cdil-submenu-toggle');
          var isExp = parentItem.classList.toggle('is-expanded');
          if (toggleBtn) toggleBtn.setAttribute('aria-expanded', isExp ? 'true' : 'false');
        }
      });
    });
'@

# ── Mobile layout CSS to append to the 3 project pages ─────────────────────
$mobileLayoutCSS = @'
<style id="cdil-mobile-fix">
/* Responsive width fix — prevents Framer's 390px fixed width from causing overflow */
@media (max-width: 809.98px) {
  html, body { overflow-x: hidden; }
  .framer-NbQct.framer-67z4u0 {
    width: 100% !important;
    min-width: 0 !important;
    box-sizing: border-box !important;
  }
  /* Reduce card image height for cleaner mobile card proportions */
  .framer-NbQct .framer-8gewg3 {
    height: 220px !important;
  }
  /* Ensure card grid fills width */
  .framer-NbQct .framer-111okhc {
    width: 100% !important;
  }
  /* Filter buttons wrapping */
  .rf-c-R6malp {
    font-size: 13px !important;
    padding: 7px 14px !important;
  }
}
</style>
'@

$fixed = 0
$skipped = 0

function Patch-HtmlFile {
  param([string]$path, [string]$rootPrefix)
  $enc = [System.Text.Encoding]::UTF8
  $bytes = [System.IO.File]::ReadAllBytes($path)
  if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
    $bytes = $bytes[3..($bytes.Length-1)]
  }
  $content = $enc.GetString($bytes)
  $original = $content

  # Fix 1: Add submenu-parent-link JS intercept (if not already patched)
  if ($content.Contains($jsInsertAfter) -and -not $content.Contains('submenuParentLinks')) {
    $content = $content.Replace($jsInsertAfter, $jsNewBlock)
  }

  # Fix 2a: Update submenu link hrefs — index.html uses ./pages/ prefix
  if ($rootPrefix -eq 'pages') {
    $content = $content.Replace('href="./pages/projects.html#ongoing"', 'href="./pages/ongoing-projects.html"')
    $content = $content.Replace('href="./pages/projects.html#completed"', 'href="./pages/completed-projects.html"')
    $content = $content.Replace('href="./pages/projects.html#upcoming"', 'href="./pages/upcoming-projects.html"')
  }
  # Fix 2b: pages/ files use ./ prefix (same directory)
  else {
    $content = $content.Replace('href="./projects.html#ongoing"', 'href="./ongoing-projects.html"')
    $content = $content.Replace('href="./projects.html#completed"', 'href="./completed-projects.html"')
    $content = $content.Replace('href="./projects.html#upcoming"', 'href="./upcoming-projects.html"')
  }

  if ($content -ne $original) {
    [System.IO.File]::WriteAllText($path, $content, (New-Object System.Text.UTF8Encoding $false))
    return $true
  }
  return $false
}

function Add-MobileCSS {
  param([string]$path)
  $enc = [System.Text.Encoding]::UTF8
  $bytes = [System.IO.File]::ReadAllBytes($path)
  if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
    $bytes = $bytes[3..($bytes.Length-1)]
  }
  $content = $enc.GetString($bytes)
  if ($content.Contains('cdil-mobile-fix')) { return $false }
  # Insert before </head>
  $content = $content.Replace('</head>', "$mobileLayoutCSS`n</head>")
  [System.IO.File]::WriteAllText($path, $content, (New-Object System.Text.UTF8Encoding $false))
  return $true
}

# ── Patch index.html ────────────────────────────────────────────────────────
$indexPath = "D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution\index.html"
$r = Patch-HtmlFile $indexPath 'pages'
if ($r) { $fixed++; Write-Host "Fixed: index.html" } else { $skipped++; Write-Host "Skipped: index.html" }

# ── Patch all pages/*.html ──────────────────────────────────────────────────
$pagesDir = "D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution\pages"
$pageFiles = Get-ChildItem -LiteralPath $pagesDir -Filter "*.html"
foreach ($file in $pageFiles) {
  $r = Patch-HtmlFile $file.FullName 'subpage'
  if ($r) { $fixed++; Write-Host "Fixed: pages/$($file.Name)" } else { $skipped++; Write-Host "Skipped: pages/$($file.Name)" }
}

Write-Host ""
Write-Host "=== Nav fix pass: Fixed=$fixed, Skipped=$skipped ==="

# ── Add mobile layout CSS to the 3 project pages ───────────────────────────
$projectPages = @("ongoing-projects.html", "completed-projects.html", "upcoming-projects.html")
$cssFix = 0
foreach ($pg in $projectPages) {
  $fp = "D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution\pages\$pg"
  $r = Add-MobileCSS $fp
  if ($r) { $cssFix++; Write-Host "CSS fix added: $pg" } else { Write-Host "CSS fix skipped (already done): $pg" }
}
Write-Host "=== Mobile CSS fix: $cssFix pages updated ==="
