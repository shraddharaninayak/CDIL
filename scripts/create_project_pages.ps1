$pagesDir = "D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution\pages"

function rep([string]$old, [string]$new) { $script:content = $script:content.Replace($old, $new) }

# ─── LAXMI PUSHP (from the-olive-court.html) ─────────────────────────
$content = [System.IO.File]::ReadAllText("$pagesDir\the-olive-court.html", [System.Text.Encoding]::UTF8)

rep 'The Olive Court — Santa Barbara, CA | CDIL' 'Laxmi Pushp — Premium N.A. Plots, Deolali, Nashik | CDIL'
rep 'Laxmi Pushp' 'Laxmi Pushp'
rep 'Deolali, Nashik' 'Deolali, Nashik'
rep 'For sale' 'Ready for Registration'
rep 'Santa Barbara, CA' 'Deolali, Nashik'
rep 'Asking price' 'Rate Per War'
rep 'The residence' 'About the Project'
rep 'A limestone estate built around a courtyard of mature olive trees and a long reflecting pool.' 'Laxmi Pushp is a premium N.A. residential plot project located on Deolali Mahalaxmi Road, Nashik. Spread across 3.5 acres with 49 ready-to-register plots, this is an ideal investment for families and investors.'
rep 'Bedrooms' 'Total Area'
rep 'Bathrooms' 'Total Plots'
rep 'Interior' 'Plot Sizes'
rep 'Year built' 'Rate Per War'
rep 'About this home' 'Project Details'
rep 'Built around a courtyard of mature olive trees, with a reflecting pool down its long side. Every principal room opens onto it.' 'Laxmi Pushp offers premium N.A. plots on Deolali Mahalaxmi Road, near Palai Villas, Nashik. With ready infrastructure and clear legal documentation, it is the perfect choice for building your dream home or as a sound investment.'
rep 'The house is quiet in a way that photographs cannot carry — the courtyard does most of that work.' 'All plots are ready for immediate registration. The project is strategically located with easy access to schools, hospitals, malls, and the railway station.'
rep 'Highlights' 'Key Features'
rep 'Courtyard with mature olive trees' 'Clear title with complete legal documentation'
rep 'Reflecting pool and outdoor kitchen' 'Developed roads, water, and electricity access'
rep 'Separate studio above the garage' 'Near Mahalaxmi Temple — 1 km away'
rep 'Ocean visible from the upper terrace' 'Nashik Road Railway Station — 2 km away'
rep 'Your advisor' 'Contact Our Team'
rep 'Watertouch' 'CDIL Sales Team'
rep 'Farmhouse Project' 'N.A. Plot Specialist'
rep 'Arrange a private viewing' 'Schedule a Site Visit'
rep 'Tell us when suits you. Your advisor replies within one business day.' 'Tell us your requirements and our team will contact you within one business day.'

# Nav
rep '>Our Projects<' '>Projects<'
rep '>Residences<' '>Projects<'
rep '>Advisors<' '>About<'
rep '>Journal<' '>Insights<'
rep './residences.html' './projects.html'
rep './advisors.html' './about.html'
rep '../pages/residences.html' '../pages/projects.html'

[System.IO.File]::WriteAllText("$pagesDir\laxmi-pushp.html", $content, [System.Text.Encoding]::UTF8)
Write-Host "laxmi-pushp.html created"

# ─── 3 LEAF FARMHOUSE (from vista-grande.html) ───────────────────────
$content = [System.IO.File]::ReadAllText("$pagesDir\vista-grande.html", [System.Text.Encoding]::UTF8)

rep '3 Leaf Farmhouse — Trimbakeshwar, Nashik | CDIL' '3 Leaf Farmhouse — NA Farmhouse Plots, Trimbakeshwar, Nashik | CDIL'
rep 'For sale' 'Available Now'
rep 'Boulder, CO' 'Trimbakeshwar, Nashik'
rep 'Trimbakeshwar, Nashik' 'Trimbakeshwar, Nashik'
rep 'Asking price' 'Minimum Plot Size'
rep 'The residence' 'About the Project'
rep 'Bedrooms' 'Project Area'
rep 'Bathrooms' 'Minimum Plot'
rep 'Interior' 'Amenities'
rep 'Year built' 'Location'
rep 'About this home' 'Project Details'
rep 'Highlights' 'Key Features'
rep 'Your advisor' 'Contact Our Team'
rep '3 Leaf Farmhouse' 'CDIL Sales Team'
rep 'Farmhouse Project' 'Farmhouse Plot Specialist'
rep 'Arrange a private viewing' 'Schedule a Site Visit'
rep 'Tell us when suits you. Your advisor replies within one business day.' 'Share your requirements and our team will arrange a guided site visit for you.'
rep '>Our Projects<' '>Projects<'
rep '>Residences<' '>Projects<'
rep '>Advisors<' '>About<'
rep '>Journal<' '>Insights<'
rep './residences.html' './projects.html'
rep './advisors.html' './about.html'

[System.IO.File]::WriteAllText("$pagesDir\3-leaf-farmhouse.html", $content, [System.Text.Encoding]::UTF8)
Write-Host "3-leaf-farmhouse.html created"

# ─── WATERTOUCH (from lakeside-retreat.html) ─────────────────────────
$content = [System.IO.File]::ReadAllText("$pagesDir\lakeside-retreat.html", [System.Text.Encoding]::UTF8)

rep 'Watertouch — Nashik Highway, Nashik | CDIL' 'Watertouch — Dam-View Farmhouse Plots, Nashik | CDIL'
rep 'For sale' 'Available Now'
rep 'Nashik Highway, Nashik' 'Mahiravni, Nashik-Trimbak Highway, Nashik'
rep 'Asking price' 'Contact for Pricing'
rep 'The residence' 'About the Project'
rep 'Bedrooms' 'Location'
rep 'Bathrooms' 'Access'
rep 'Interior' 'Amenities'
rep 'Year built' 'Unique Feature'
rep 'About this home' 'Project Details'
rep 'Highlights' 'Key Features'
rep 'Your advisor' 'Contact Our Team'
rep 'Watertouch' 'CDIL Sales Team'
rep 'Farmhouse Project' 'Farmhouse Plot Specialist'
rep 'Arrange a private viewing' 'Schedule a Site Visit'
rep 'Tell us when suits you. Your advisor replies within one business day.' 'Share your requirements and our team will arrange a guided site visit for you.'
rep '>Our Projects<' '>Projects<'
rep '>Residences<' '>Projects<'
rep '>Advisors<' '>About<'
rep '>Journal<' '>Insights<'
rep './residences.html' './projects.html'
rep './advisors.html' './about.html'

[System.IO.File]::WriteAllText("$pagesDir\watertouch.html", $content, [System.Text.Encoding]::UTF8)
Write-Host "watertouch.html created"

# ─── AMBOLI VAN-VELI (from tomas-lindqvist.html — repurpose advisor page) ──
$content = [System.IO.File]::ReadAllText("$pagesDir\lakeside-retreat.html", [System.Text.Encoding]::UTF8)

rep 'Watertouch — Dam-View Farmhouse Plots, Nashik | CDIL' 'Amboli Van-Veli — Farmhouse Plots, Amboli, Maharashtra | CDIL'
rep 'Mahiravni, Nashik-Trimbak Highway, Nashik' 'Gunjal Farm, Amboli, Maharashtra'
rep 'Available Now' 'Available Now'
rep '>Our Projects<' '>Projects<'
rep '>Residences<' '>Projects<'
rep '>Advisors<' '>About<'
rep './residences.html' './projects.html'
rep './advisors.html' './about.html'

[System.IO.File]::WriteAllText("$pagesDir\amboli-van-veli.html", $content, [System.Text.Encoding]::UTF8)
Write-Host "amboli-van-veli.html created"

Write-Host "All CDIL project pages created"
