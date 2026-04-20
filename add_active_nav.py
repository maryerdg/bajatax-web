import glob
import re

# Map of filename -> nav link href
page_nav_map = {
    'index.html': '/',
    'persona-fisica.html': '/persona-fisica',
    'empresas.html': '/empresas',
    'servicios.html': '/servicios',
    'nosotros.html': '/nosotros',
    'recursos.html': '/recursos',
    'contacto.html': '/contacto',
}

# CSS for the active nav state
active_css = """
    /* Active Nav Link */
    .nav-active {
      color: #002d4c !important;
      font-weight: 700 !important;
      border-bottom: 3px solid #006e27;
      padding-bottom: 4px;
    }
"""

for filename, active_href in page_nav_map.items():
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Skipped {filename} (not found)")
        continue

    # Inject CSS if not already present
    if '.nav-active' not in content:
        content = content.replace('/* Uniformidad', active_css + '    /* Uniformidad')

    # Desktop nav: Find all nav links and add/remove nav-active class
    # Pattern: <a class="..." href="/page">Label</a>
    def replace_desktop_nav(match):
        href = match.group('href')
        classes = match.group('classes')
        rest = match.group('rest')
        
        # Remove any existing nav-active
        classes = classes.replace(' nav-active', '').replace('nav-active ', '')
        
        # Add nav-active if this is the current page
        if href == active_href:
            classes = classes + ' nav-active'
        
        return f'<a class="{classes}" href="{href}">{rest}</a>'

    # Match desktop nav links specifically
    pattern = r'<a class="(?P<classes>[^"]*(?:text-on-surface-variant|nav-active)[^"]*)" href="(?P<href>/[^"]*?)">(?P<rest>[^<]+)</a>'
    content = re.sub(pattern, replace_desktop_nav, content)

    # Mobile nav: add active styling for the current page
    def replace_mobile_nav(match):
        full = match.group(0)
        href = match.group('href')
        label = match.group('label')
        
        if href == active_href:
            return f'<a href="{href}" class="text-secondary font-extrabold border-b-4 border-secondary pb-1">{label}</a>'
        else:
            return f'<a href="{href}" class="text-primary hover:text-secondary">{label}</a>'
    
    # Match mobile menu links
    mobile_pattern = r'<a href="(?P<href>/[^"]*?)" class="(?:text-primary hover:text-secondary|text-secondary font-extrabold border-b-4 border-secondary pb-1)">(?P<label>[^<]+)</a>'
    content = re.sub(mobile_pattern, replace_mobile_nav, content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filename} (active: {active_href})")

print("Done! Active nav states applied to all pages.")
