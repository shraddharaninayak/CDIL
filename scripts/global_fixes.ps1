$rootDir = "D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
$pagesDir = "$rootDir\pages"

$allFiles = @("$rootDir\index.html") + [System.IO.Directory]::GetFiles($pagesDir, "*.html")

foreach ($fp in $allFiles) {
    $c = [System.IO.File]::ReadAllText($fp, [System.Text.Encoding]::UTF8)

    $c = $c.Replace('Contact Uss', 'Contact Us')
    $c = $c.Replace('>Residences<', '>Projects<')
    $c = $c.Replace('>Advisors<', '>About<')
    $c = $c.Replace('Designed by Riyad Sbeitan', 'CDIL Real Estate')
    $c = $c.Replace('Made in Framer', 'Nashik, Maharashtra')
    $c = $c.Replace('Create a free website with Framer, the website builder loved by startups, designers and agencies.', '')
    $c = $c.Replace('Never miss a residence', 'Stay Updated')
    $c = $c.Replace('New homes in your inbox before they reach the portals.', 'Get latest CDIL project updates and investment insights.')
    $c = $c.Replace('./residences.html', './projects.html')
    $c = $c.Replace('./advisors.html', './about.html')
    $c = $c.Replace('./rising-inventory-autumn.html', './journal.html')
    $c = $c.Replace('./seven-questions-first-showing.html', './journal.html')
    $c = $c.Replace('./staging-that-moves-the-price.html', './journal.html')
    $c = $c.Replace('./lakeside-retreat.html', './watertouch.html')
    $c = $c.Replace('./the-olive-court.html', './laxmi-pushp.html')
    $c = $c.Replace('./vista-grande.html', './3-leaf-farmhouse.html')
    $c = $c.Replace('./daniel-reyes.html', './laxmi-pushp.html')
    $c = $c.Replace('./amara-whitfield.html', './3-leaf-farmhouse.html')
    $c = $c.Replace('./tomas-lindqvist.html', './amboli-van-veli.html')
    $c = $c.Replace('./priya-raghavan.html', './watertouch.html')
    $c = [regex]::Replace($c, 'href="mailto:hello@cdil\.com"', 'href="mailto:cdilconstructionhub2008@gmail.com"')
    $c = [regex]::Replace($c, 'href="tel:\+15035550142"', 'href="tel:+918087825105"')
    $c = $c.Replace('https://framer.link/riyad-sbeitan', 'https://cdilrealestate.com/')
    $c = $c.Replace('https://riyadsbitan.com', 'https://cdilrealestate.com/')

    [System.IO.File]::WriteAllText($fp, $c, [System.Text.Encoding]::UTF8)
    Write-Host "$([System.IO.Path]::GetFileName($fp)) - OK"
}

Write-Host "`nAll $($allFiles.Count) files processed"
