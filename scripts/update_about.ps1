$filePath = "D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution\pages\about.html"
$content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)

function rep([string]$old, [string]$new) { $script:content = $script:content.Replace($old, $new) }

# Page title
rep 'About — CDIL' 'About CDIL — Real Estate & Infrastructure, Nashik'

# About intro paragraph
rep 'CDIL started with one office, one advisor and a refusal to present a home nobody had stood inside.' 'CDIL Real Estate & Infrastructure was founded in 2008 in Nashik with a simple mission: help families find the perfect plot or farmhouse in scenic locations around Maharashtra.'

# Founding year
rep 'We started in 2011' 'Founded in 2008'

# How we work
rep 'How we work' 'How We Work'
rep 'Every residence is re-checked weekly. Every buyer gets one advisor, not a queue. Every offer is explained in plain language before it is signed — including the parts that are not in your favour.' 'Every client receives personalised guidance from our experienced team. Every project is legally verified with clear documentation. Every plot is personally visited and assessed before we list it. We believe in transparency, trust, and delivering exactly what we promise.'

# Where we are going
rep 'Where we are going' 'Our Vision'
rep 'Twelve states, forty advisors, and no ambition to become a portal. We would rather be the house people call back than the one with the most listings.' 'To be the most trusted real estate partner in Nashik and Maharashtra, recognized for our innovation, excellence, and commitment to sustainable land development that truly serves our clients.'

# What we hold to
rep 'What we hold to' 'Our Values'
rep 'Four promises, kept on every home.' 'Four commitments, honoured on every project.'
rep 'Say the hard thing' 'Transparency First'
rep 'If a home is priced wrong, you hear it from us first.' 'We give you honest, straightforward advice even when it means recommending against a purchase.'
rep 'One advisor, start to finish' 'Personalised Service'
rep 'No hand-offs between departments halfway through.' 'One dedicated team member guides you from your first enquiry to successful registration.'
rep 'No fees you did not see coming' 'No Hidden Costs'
rep 'Every cost is on the table before you sign anything.' 'All costs, documentation requirements, and timelines are clearly explained before you commit.'
rep 'An answer within a day' 'Prompt Response'
rep 'Calls, emails and messages — one business day, every time.' 'We respond to all calls, emails, and WhatsApp messages within one business day, every time.'

# Navigation labels in footer/nav
rep '>Residences<' '>Projects<'
rep '>Advisors<' '>About<'
rep '>Journal<' '>Insights<'

# Footer newsletter
rep 'Never miss a residence' 'Stay Updated with CDIL'
rep 'New homes in your inbox before they reach the portals.' 'Get the latest project launches, plot availability, and investment insights.'
rep 'Your email' 'Your Email'
rep 'Subscribe' 'Subscribe'

# Footer branding
rep 'Designed by Riyad Sbeitan' 'CDIL Real Estate &amp; Infrastructure'
rep 'Made in Framer' 'Nashik, Maharashtra, India'
rep 'Create a free website with Framer, the website builder loved by startups, designers and agencies.' ''

# Contact Us links text
rep 'Contact Uss' 'Contact Us'

# Navigation links
rep './residences.html' './projects.html'
rep './advisors.html' './about.html'
rep './journal.html' './journal.html'
rep '../pages/residences.html' '../pages/projects.html'
rep '../pages/advisors.html' '../pages/about.html'

[System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
Write-Host "about.html updated"
