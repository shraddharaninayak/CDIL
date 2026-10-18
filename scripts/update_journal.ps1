$filePath = "D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution\pages\journal.html"
$content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
function rep([string]$old, [string]$new) { $script:content = $script:content.Replace($old, $new) }

# Fix title
rep 'Insights and Updates — CDIL' 'Insights and Updates — CDIL Real Estate, Nashik'

# Fix doubled-s typo
rep 'Real Estate Trendss,' 'Real Estate Trends,'

# Fix article description with leftover text
rep 'Nashik growing infrastructure, the upcoming Kumbh Mela 2027, and rising demand for weekend homes make farmhouse plots a compelling investment. — and one of them costs sixty dollars.' 'Nashik is fast emerging as one of the most exciting real estate destinations in Maharashtra. Growing infrastructure, Kumbh Mela 2027 development, and rising demand for weekend homes make farmhouse plots a compelling investment.'

# Fix Selling category label
rep '>Selling<' '>Investment Guide<'

# Fix "market, street street." leftover
rep 'market,
street
street.' 'real estate market insights and project updates from CDIL.'

# Fix double "Contact Us"
rep 'Contact Uss' 'Contact Us'

# Navigation footer labels
rep '>Residences<' '>Projects<'
rep '>Advisors<' '>About<'
rep '>Journal<' '>Insights<'

# Newsletter
rep 'Never miss a residence' 'Stay Updated with CDIL'
rep 'New homes in your inbox before they reach the portals.' 'Get the latest project launches and investment insights from CDIL.'

# Footer credits
rep 'Designed by Riyad Sbeitan' 'CDIL Real Estate'
rep 'Made in Framer' 'Nashik, Maharashtra'
rep 'Create a free website with Framer, the website builder loved by startups, designers and agencies.' ''

# Nav links
rep './residences.html' './projects.html'
rep './advisors.html' './about.html'

[System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
Write-Host "journal.html updated"
