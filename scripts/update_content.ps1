param([string]$FilePath, [string]$OutPath = $null)
if (-not $OutPath) { $OutPath = $FilePath }

$content = [System.IO.File]::ReadAllText($FilePath, [System.Text.Encoding]::UTF8)

function rep([string]$old, [string]$new) {
    $script:content = $script:content.Replace($old, $new)
}

# META / HEAD
$content = [regex]::Replace($content, '<title>AYLAAA[^<]*</title>', '<title>CDIL Real Estate - Building Dreams, One Plot at a Time</title>')
rep 'AYLAAA — Rare homes, quietly presented' 'CDIL Real Estate - Building Dreams, One Plot at a Time'
rep 'A private brokerage for architect-designed homes. Every residence walked, verified and presented by a senior advisor.' 'Your trusted partner in real estate and plot sales in Nashik, serving excellence for over 17 years.'
rep 'https://aylaaa.framer.website/' 'https://cdilrealestate.com/'
rep 'https://aylaaa.framer.website' 'https://cdilrealestate.com'

# BRAND NAME
rep 'AYLAAA' 'CDIL'

# NAV / HERO
rep 'Private residences' 'Our Projects'
rep 'View residences' 'View Projects'
rep 'Private viewing' 'Contact Us'
rep 'Now presenting' 'Featured Projects'
rep 'Handpicked, just for you' 'Premium plots and farmhouses across Nashik'
rep 'View all residences' 'View All Projects'

# FEATURED PROPERTIES
rep 'The Olive Court' 'Laxmi Pushp'
rep 'Santa Barbara, CA' 'Deolali, Nashik'
rep 'Vista Grande' '3 Leaf Farmhouse'
rep 'Boulder, CO' 'Trimbakeshwar, Nashik'
rep 'Lakeside Retreat' 'Watertouch'
rep 'Austin, TX' 'Nashik Highway, Nashik'

# FILTERS
rep 'All locations' 'All Locations'
rep 'Portland' 'Deolali'
rep 'Austin' 'Trimbakeshwar'
rep 'Boulder' 'Amboli'
rep 'Seattle' 'Igatpuri'
rep 'Santa Barbara' 'Nashik Highway'
rep 'Property type' 'Project Type'
rep 'All types' 'All Types'
rep 'Waterfront' 'River-touch'
rep 'Price range' 'Project Type'
rep 'Any price' 'All Types'
rep 'Under $1.2m' 'Farmhouse Plot'
rep 'Architect-designed' 'N.A. Plot'
rep 'Move-in ready' 'Gated Community'
rep 'Off-market' 'Dam-touch'
rep 'Historic homes' 'Agri-Farm'
rep 'New this week' 'Featured'

# ABOUT SECTION
rep 'Design-led search' 'Expert Guidance'
rep 'We start from how you want to live, not from a price band.' 'We guide you to the right plot for your lifestyle and investment goals with 17+ years of expertise.'
rep 'Structure and survey' 'Prime Locations'
rep 'Every home is read by someone who knows what a crack means.' 'All our projects are situated in scenic, accessible locations around Nashik near dams, rivers, and highways.'
rep 'Energy and longevity' 'Quality Infrastructure'
rep 'Running costs and retrofit potential, before you commit.' 'Every project includes developed roads, water supply, electricity, and complete legal documentation.'

# STATS
rep 'Residences placed' 'Plots Sold'
rep 'Years in business' 'Years of Experience'
rep 'States licensed' 'Happy Families'
rep 'Senior advisors' 'Completed Projects'

# SERVICES SECTION
rep 'What else we do' 'Our Services'
rep 'Support beyond buying and selling' 'Complete Real Estate Solutions'
rep 'Mortgage and finance' 'Farmhouse Plots'
rep 'Introductions to lenders who understand architect-designed and unusual homes.' 'Premium farmhouse plots in scenic locations near Nashik with dam views, river-touch, and mountain landscapes.'
rep 'Property management' 'N.A. Plots'
rep 'Quiet, careful management for owners who live elsewhere part of the year.' 'Non-Agricultural plots with clear titles, legal approvals, and ready infrastructure for immediate construction.'
rep 'Renovation and development' '3D Printed Farmhouse'
rep 'Architects and builders we have worked with for years, briefed before you buy.' 'Nashik first 3D printed farmhouse - revolutionary construction technology combining speed, strength, and sustainability.'

# ADVISORS SECTION
rep 'Our advisors' 'Our Projects'
rep 'The people behind every introduction' 'Explore Our Premium Properties'
rep 'Four senior advisors, four markets, one standard of service.' 'From scenic farmhouses to NA plots - discover the right investment for your future.'
rep 'Daniel Reyes' 'Laxmi Pushp'
rep 'Managing broker' 'N.A. Project'
rep 'Amara Whitfield' '3 Leaf Farmhouse'
rep 'Senior advisor' 'Farmhouse Project'
rep 'Tomas Lindqvist' 'Amboli Van-Veli'
rep 'Luxury specialist' 'Farmhouse Project'
rep 'Priya Raghavan' 'Watertouch'
rep "Buyer's advisor" 'Farmhouse Project'
rep 'Meet all advisors' 'View All Projects'

# TESTIMONIALS
rep 'CDIL made selling our first home feel simple instead of stressful.' 'The prime location and excellent amenities exceeded my expectations. CDIL professionalism and commitment to quality is truly outstanding.'
rep 'Marcus &amp; Elena R.' 'Dr. Prashant Birla'
rep 'Sold in Portland, OR' 'Watertouch, Nashik'
rep 'They talked us out of a house we loved. Six weeks later we understood why.' 'My dream of owning a dam-touch plot finally became reality. The breathtaking views and seamless support made every step worthwhile.'
rep 'Priya N.' 'Mr. Prashant Kale'
rep 'Bought in Seattle, WA' 'Ex-Army Officer - Watertouch, Nashik'
rep 'The first brokerage that asked how we wanted to live before asking what we could spend.' 'The river-touch farmhouse plot with stunning mountain views provides the perfect serene environment for unwinding from city life.'
rep 'Omar &amp; Leila H.' 'Mr. Rajiv Sutar'
rep 'Bought in Austin, TX' 'Teakwood Farm, Nashik'

# JOURNAL / BLOG
rep 'The Journal' 'Insights and Updates'
rep 'Notes for buyers and sellers' 'Stay informed with our latest news and market insights'
rep 'Written by the advisors doing the work, not by a content team.' 'Market insights, project updates, and real estate guidance from CDIL experienced team.'
rep 'What rising inventory means for buyers this autumn' 'How AI and Digital Tools Are Transforming Real Estate in 2025'
rep 'Inventory is up nineteen per cent. In two of our four markets that means leverage; in the other two it mostly means the wrong homes are sitting.' 'AI-powered tools and digital platforms are changing how buyers discover and evaluate real estate and how developers like CDIL are adapting.'
rep 'Market report' 'Real Estate Trends'
rep 'Seven questions to ask before your first showing' 'How to Get a Farmer Certificate (Sheti Pramanpatra) in India'
rep 'The useful questions are duller than the kitchen, and they are about the parts of the house you cannot see.' 'A step-by-step guide to obtaining the Sheti Pramanpatra - an essential document for purchasing farmhouse or agricultural land in India.'
rep 'Buying guide' 'Legal Guide'
rep 'Staging that actually moves the price' 'Why Invest in a Nashik Farmhouse Plot in 2025?'
rep 'Most staging spend does not come back. Three things reliably do' 'Nashik growing infrastructure, the upcoming Kumbh Mela 2027, and rising demand for weekend homes make farmhouse plots a compelling investment.'
rep 'Read the Journal' 'Read All Insights'

# CTA SECTION
rep 'Private viewings' 'Schedule a Site Visit'
rep 'Ready to find your next chapter?' 'Ready to Own Your Dream Plot?'
rep 'Tell us what you are looking for and we will match you with the advisor who knows that area best.' 'Tell us about your requirements and our experienced team will help you find the perfect farmhouse or NA plot.'
rep 'Arrange a private viewing' 'Schedule a Site Visit'

# FOOTER
rep 'A private brokerage for architect-designed homes. Licensed in 12 states.' 'CDIL Real Estate and Infrastructure. Nashik trusted farmhouse and plot developer since 2008.'
rep 'hello@aylaaa.com' 'cdilconstructionhub2008@gmail.com'
rep 'hello@cdil.com' 'cdilconstructionhub2008@gmail.com'
rep '+1 503 555 0142' '+91 80878 25105'
rep 'Licensed in 12 states' 'Nashik, Maharashtra, India'
rep 'A house built the slow way: one office, one advisor per client, and a rule that nobody presents a home they have not walked through.' 'Building dreams through honest guidance, quality plots, and over 17 years of trusted real estate expertise in Nashik.'

# NAVIGATION LINKS
rep './pages/residences.html' './pages/projects.html'
rep './pages/advisors.html' './pages/projects.html'
rep './pages/the-olive-court.html' './pages/laxmi-pushp.html'
rep './pages/vista-grande.html' './pages/3-leaf-farmhouse.html'
rep './pages/lakeside-retreat.html' './pages/watertouch.html'
rep './pages/daniel-reyes.html' './pages/laxmi-pushp.html'
rep './pages/amara-whitfield.html' './pages/3-leaf-farmhouse.html'
rep './pages/tomas-lindqvist.html' './pages/amboli-van-veli.html'
rep './pages/priya-raghavan.html' './pages/watertouch.html'
rep './pages/rising-inventory-autumn.html' './pages/journal.html'
rep './pages/seven-questions-first-showing.html' './pages/journal.html'
rep './pages/staging-that-moves-the-price.html' './pages/journal.html'
rep './pages/..html' './pages/projects.html'

$content = [regex]::Replace($content, '\./pages/mailto:[^"]+', 'mailto:cdilconstructionhub2008@gmail.com')
$content = [regex]::Replace($content, '\./pages/tel:[^"]+', 'tel:+918087825105')
rep 'mailto:hello@aylaaa.com' 'mailto:cdilconstructionhub2008@gmail.com'
rep 'tel:+15035550142' 'tel:+918087825105'

# FRAMER CREDITS
rep 'https://framer.link/riyad-sbeitan' 'https://cdilrealestate.com/'
rep 'https://riyadsbitan.com' 'https://cdilrealestate.com/'

[System.IO.File]::WriteAllText($OutPath, $content, [System.Text.Encoding]::UTF8)
Write-Host "Done: $OutPath"
