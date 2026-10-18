import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    master = f.read()

def create_subpage(status_key, title_text, filename):
    content = master
    # Update title
    content = re.sub(r'<title>.*?</title>', f'<title>{title_text} | CDIL Real Estate &amp; Infrastructure</title>', content)
    
    # Update initial button active styles
    for f in ['all', 'ongoing', 'completed', 'upcoming']:
        is_active = (f == status_key)
        old_pattern = rf'<button type="button" aria-pressed="[^"]*" class="rf-c-R6malp" data-filter="{f}"[^>]*>'
        active_style = 'style="background: var(--token-025422ea-d283-4879-b332-741cb1c834c7, rgb(26, 38, 32)); color: var(--token-ed5af0b1-8875-4b9b-a8d0-dd29f7c8c608, rgb(243, 239, 228)); border-color: var(--token-025422ea-d283-4879-b332-741cb1c834c7, rgb(26, 38, 32)); font-family: Inter, sans-serif; font-size: 15px; font-weight: 400; letter-spacing: 0em; line-height: 1em;"'
        inactive_style = 'style="background: transparent; color: var(--token-b8cfd3da-418b-4999-a7f7-4bf97baf1624, rgba(26, 38, 32, 0.74)); border-color: var(--token-d34888b7-6c91-4dbc-95a1-370fba2352b1, rgba(26, 38, 32, 0.16)); font-family: Inter, sans-serif; font-size: 15px; font-weight: 400; letter-spacing: 0em; line-height: 1em;"'
        repl = f'<button type="button" aria-pressed="{str(is_active).lower()}" class="rf-c-R6malp" data-filter="{f}" {active_style if is_active else inactive_style}>'
        content = re.sub(old_pattern, repl, content)
    
    # Hide non-matching cards by default (SSR fallback)
    for card_status in ['ongoing', 'completed', 'upcoming']:
        if card_status != status_key:
            content = content.replace(f'data-cdil-status="{card_status}"', f'data-cdil-status="{card_status}" style="display:none"')

    with open(f'pages/{filename}', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated pages/{filename} ({len(content)} bytes)")

create_subpage('ongoing', 'Ongoing Projects', 'ongoing-projects.html')
create_subpage('completed', 'Completed Projects', 'completed-projects.html')
create_subpage('upcoming', 'Upcoming Projects', 'upcoming-projects.html')

