import re
import glob

# Map filenames to their respective menu names for active states
page_mapping = {
    'index.html': 'Inicio',
    'persona-fisica.html': 'Persona Física',
    'empresas.html': 'Empresas',
    'servicios.html': 'Servicios',
    'nosotros.html': 'Nosotros',
    'recursos.html': 'Recursos',
    'contacto.html': 'Contacto'
}

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # --- 1. Fix the top padding and vertical alignment ---
    # The user felt that Servicios text was pushed too far down.
    # By changing items-center to items-start, the text will hug the top margin
    # Alternatively, we can just reduce the top padding from pt-[180px] to pt-[140px]
    # Let's reduce the top padding on secondary pages so it feels snappier.
    if f != 'index.html':
        content = content.replace('md:pt-[180px]', 'md:pt-[150px]')
        # Remove items-center so the text starts naturally at the top of the grid 
        # alongside the image, preventing it from being pushed down by empty space.
        content = content.replace('items-center', 'items-start')

    # --- 2. Add Active State to Navigation ---
    # We will find the links in the Desktop Menu and Mobile Menu
    # Desktop links class: text-on-surface-variant hover:text-primary font-headline font-semibold text-sm transition-colors duration-200
    # Mobile links class: hover:text-secondary
    
    if f in page_mapping:
        current_page_name = page_mapping[f]
        
        # 2a. Desktop Menu Highlight
        # We need to find the specific link and change its text color and add an underline layout.
        # We'll use regex to target the exact anchor tag whose text is the current page name.
        
        def highlight_desktop(match):
            pre = match.group(1)
            href = match.group(2)
            classes = match.group(3)
            post = match.group(4)
            # The active class will drop 'text-on-surface-variant' and add specific green active states
            new_classes = classes.replace('text-on-surface-variant', 'text-secondary border-b-2 border-secondary pb-1')
            return f"{pre}{href}\" class=\"{new_classes}\"{post}"

        # Match anchor tags in the header
        # pattern: (<a[^>]*href=")([^"]*)("\s*class=")([^"]*)("[^>]*>CurrentPageName</a>)
        pattern_desktop = r'(<a[^>]*href=")([^"]*)("\s*class=")([^"]*)("[^>]*>' + re.escape(current_page_name) + r'</a>)'
        
        content = re.sub(pattern_desktop, highlight_desktop, content)
        
        # 2b. Mobile Menu Highlight
        def highlight_mobile(match):
            pre = match.group(1)
            return f"{pre} class=\"text-secondary border-l-4 border-secondary pl-2\""
            
        # Match mobile anchors (they don't have a class attribute in our current template actually, or they have 'hover:text-secondary')
        pattern_mobile = r'(<a[^>]*href="[^"]*)"\s*class="hover:text-secondary"([^>]*>' + re.escape(current_page_name) + r'</a>)'
        content = re.sub(pattern_mobile, highlight_mobile, content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Active states and hero layout tweaks applied.")
