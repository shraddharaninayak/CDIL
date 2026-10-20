# Patch all HTML files: remove language switcher, add theme CSS + JS + init

$base = "D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT`[SKILLNEX`]\WEBSITES\CDIL-Constrution"

# Exact language switcher HTML (literal string match, no regex)
$langSwitcher = '<div role="group" aria-label="Language" style="display:flex;padding:3px;border:1px solid var(--ay-ink-line, rgba(245, 242, 234, 0.3));border-radius:999px;transition:border-color .35s"><button style="background:var(--ay-ink, rgb(245, 242, 234));border:0;cursor:pointer;padding:5px 9px;font:500 10px/1 Inter, sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--ay-ink-bg, rgba(12,16,12,.92));border-radius:999px;transition:background .35s, color .35s" aria-pressed="true">EN</button><button style="background:none;border:0;cursor:pointer;padding:5px 9px;font:500 10px/1 Inter, sans-serif;letter-spacing:0;text-transform:uppercase;color:var(--ay-ink, rgb(245, 242, 234));border-radius:999px;transition:background .35s, color .35s;font-size:12px;font-family:&quot;Cairo&quot;, sans-serif" aria-pressed="false">&#1593;</button></div>'

# Inline init — prevents flash of wrong theme before CSS loads
$initScript = '<script>!function(){var t;try{t=localStorage.getItem("cdil-theme")}catch(e){}document.documentElement.setAttribute("data-theme",t||"dark")}();</script>'

$patchedCount = 0
$skippedCount = 0

function Patch-File([string]$filePath, [string]$cssHref, [string]$jsHref) {
    $enc = [System.Text.Encoding]::UTF8
    $bytes = [System.IO.File]::ReadAllBytes($filePath)
    # strip UTF-8 BOM if present
    if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
        $bytes = $bytes[3..($bytes.Length-1)]
    }
    $content = $enc.GetString($bytes)
    $original = $content

    # 1. Remove language switcher (try literal Arabic char first, then &#1593;)
    $arabicLiteral = [char]0x0639  # ع
    $langLiteral = $langSwitcher.Replace('&#1593;', $arabicLiteral)
    if ($content.Contains($langLiteral)) {
        $content = $content.Replace($langLiteral, '')
    } elseif ($content.Contains($langSwitcher)) {
        $content = $content.Replace($langSwitcher, '')
    }

    # 2. Add CSS link if not already present
    if (-not $content.Contains('cdil-theme.css')) {
        $cssLink = "<link rel=`"stylesheet`" href=`"$cssHref`">"
        $content = $content.Replace('</head>', "$cssLink`n</head>")
    }

    # 3. Add inline init script if not already present
    if (-not $content.Contains('cdil-theme')) {
        # already added via check above; this is a fallback
    }
    if (-not $content.Contains($initScript)) {
        $content = $content.Replace('</head>', "$initScript`n</head>")
    }

    # 4. Add JS script before </body> if not already present
    if (-not $content.Contains('cdil-theme.js')) {
        $jsTag = "<script src=`"$jsHref`" defer></script>"
        $content = $content.Replace('</body>', "$jsTag`n</body>")
    }

    if ($content -ne $original) {
        [System.IO.File]::WriteAllText($filePath, $content, (New-Object System.Text.UTF8Encoding $false))
        return $true
    }
    return $false
}

# Patch index.html (root level — relative paths without ../)
$indexPath = "D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution\index.html"
$result = Patch-File $indexPath "./styles/cdil-theme.css" "./scripts/cdil-theme.js"
if ($result) { $patchedCount++; Write-Host "Patched: index.html" } else { $skippedCount++; Write-Host "Skipped: index.html" }

# Patch all pages/*.html (one level deep — use ../ prefix)
$pagesDir = "D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution\pages"
$pageFiles = Get-ChildItem -LiteralPath $pagesDir -Filter "*.html"
foreach ($file in $pageFiles) {
    $result = Patch-File $file.FullName "../styles/cdil-theme.css" "../scripts/cdil-theme.js"
    if ($result) { $patchedCount++; Write-Host "Patched: pages/$($file.Name)" } else { $skippedCount++; Write-Host "Skipped: pages/$($file.Name)" }
}

Write-Host ""
Write-Host "Done. Patched: $patchedCount | Skipped (already done): $skippedCount"
