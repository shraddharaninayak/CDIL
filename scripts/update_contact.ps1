$filePath = "D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution\pages\contact.html"
$content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)

function rep([string]$old, [string]$new) { $script:content = $script:content.Replace($old, $new) }

# Title
rep 'Contact Us — CDIL' 'Contact CDIL Real Estate — Nashik'
rep 'Private viewing — CDIL' 'Contact CDIL Real Estate — Nashik'

# Intro
rep 'Tell us what you are looking for — or what you are hoping to sell — and an advisor will reply within one business day.' 'Tell us about the plot or farmhouse you are looking for and our team will get back to you within one business day.'
rep 'One advisor, one conversation. No call centres, no hand-offs.' 'One dedicated team member. Personal service from first enquiry to plot registration.'

# Studio/Office
rep 'Studio' 'Office'
rep 'Mon–Fri, 9:00–18:00. Saturdays by appointment.' 'Mon–Sat, 10:00–19:00. Sundays by appointment.'

# Office address
$content = [regex]::Replace($content, 'href="[^"]*google.*?maps[^"]*"', 'href="https://maps.google.com/?q=Divine+Tej+701+College+Road+Nashik"')

# FAQs
rep 'Common questions' 'Frequently Asked Questions'
rep 'Do I need to be pre-approved before viewing?' 'Do I need any documents before visiting a project site?'
rep 'No. You can view anything on our books without a pre-approval. We will tell you honestly when it makes sense to get one — usually before you make an offer, not before you look.' 'No. You are welcome to visit any of our project sites without prior paperwork. Our team will guide you through documentation requirements when you are ready to proceed.'
rep 'How do you price a home?' 'What types of plots does CDIL offer?'
rep 'We look at comparable sales in the same streets, the condition of the property, and what has actually closed in the last ninety days. You get the full comparison sheet, not just a number.' 'CDIL offers N.A. (Non-Agricultural) residential plots, farmhouse plots, and agri-farm plots across scenic locations near Nashik — including dam-touch, river-touch, and highway-accessible properties.'
rep 'What are your fees?' 'Are the plots legally verified?'
rep 'Standard commission, disclosed in writing before you sign, with no marketing surcharges or admin fees added later.' 'Yes. All our plots come with clear titles, legal documentation, and transparency on all approvals and registrations. We share the complete documentation before you sign anything.'
rep 'Do you work with international buyers?' 'Can I visit the project site before buying?'
rep 'Yes. Four of our advisors work in Arabic and English, and we can handle remote viewings and documentation.' 'Absolutely. We encourage all buyers to visit the site before making a decision. Contact us to arrange a guided site visit at your convenience.'

# Enquiry form
rep 'Share a few details and the right advisor will reply within one business day.' 'Share your requirements and our team will contact you within one business day.'
rep 'Full name' 'Full Name'
rep 'Interested in' 'Project of Interest'
rep 'Amsterdam' 'Laxmi Pushp (N.A. Plots, Deolali)'
rep 'Barcelona' '3 Leaf Farmhouse (Trimbakeshwar)'
rep 'Send enquiry' 'Send Enquiry'

# Navigation
rep '>Residences<' '>Projects<'
rep '>Advisors<' '>About<'
rep '>Journal<' '>Insights<'

# Footer newsletter
rep 'Never miss a residence' 'Stay Updated with CDIL'
rep 'New homes in your inbox before they reach the portals.' 'Get the latest project launches and investment insights from CDIL.'
rep 'Designed by Riyad Sbeitan' 'CDIL Real Estate &amp; Infrastructure'
rep 'Made in Framer' 'Nashik, Maharashtra, India'
rep 'Create a free website with Framer, the website builder loved by startups, designers and agencies.' ''

# Navigation links
rep './residences.html' './projects.html'
rep './advisors.html' './about.html'

[System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
Write-Host "contact.html updated"
