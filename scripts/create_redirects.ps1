$pagesDir = "D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution\pages"

function MakeRedirect([string]$dest, [string]$title) {
    return @"
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$title — CDIL Real Estate</title>
<meta http-equiv="refresh" content="0; url=$dest">
<link rel="canonical" href="$dest">
<style>
html,body{margin:0;padding:0;background:#f3efe4;font-family:Inter,sans-serif;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center}
.wrap{padding:2rem}
h1{font-family:Fraunces,serif;font-weight:300;font-size:2rem;color:#1a2620;margin:0 0 1rem}
p{color:#1a2620;opacity:.7;margin:0 0 1.5rem}
a{color:#35533f;text-decoration:none;border-bottom:1px solid currentColor}
</style>
</head>
<body>
<div class="wrap">
<h1>CDIL Real Estate</h1>
<p>Redirecting you to the right page&hellip;</p>
<p><a href="$dest">Click here if not redirected automatically</a></p>
</div>
</body>
</html>
"@
}

# Advisor pages → projects
$redirects = @{
    "advisors.html"                        = @("./projects.html", "Projects")
    "amara-whitfield.html"                 = @("./3-leaf-farmhouse.html", "3 Leaf Farmhouse")
    "daniel-reyes.html"                    = @("./laxmi-pushp.html", "Laxmi Pushp")
    "priya-raghavan.html"                  = @("./watertouch.html", "Watertouch")
    "tomas-lindqvist.html"                 = @("./amboli-van-veli.html", "Amboli Van-Veli")
    "lakeside-retreat.html"                = @("./watertouch.html", "Watertouch")
    "the-olive-court.html"                 = @("./laxmi-pushp.html", "Laxmi Pushp")
    "vista-grande.html"                    = @("./3-leaf-farmhouse.html", "3 Leaf Farmhouse")
    "rising-inventory-autumn.html"         = @("./journal.html", "Insights & Updates")
    "seven-questions-first-showing.html"   = @("./journal.html", "Insights & Updates")
    "staging-that-moves-the-price.html"    = @("./journal.html", "Insights & Updates")
}

foreach ($file in $redirects.Keys) {
    $dest = $redirects[$file][0]
    $title = $redirects[$file][1]
    $html = MakeRedirect $dest $title
    [System.IO.File]::WriteAllText("$pagesDir\$file", $html, [System.Text.Encoding]::UTF8)
    Write-Host "$file → $dest"
}

Write-Host "`nAll redirect pages created"
