import re
import glob

page_mapping = {
    'index.html': 'Inicio',
    'persona-fisica.html': 'Persona Física',
    'empresas.html': 'Empresas',
    'servicios.html': 'Servicios',
    'nosotros.html': 'Nosotros',
    'recursos.html': 'Recursos',
    'contacto.html': 'Contacto'
}

for f in page_mapping:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        current_page = page_mapping[f]
        
        # We need to find the specific <a>...CurrentPage</a> inside the navigation.
        # It's safer to just do a string replacement on the exact anchor tag if we can predict it.
        # Desktop links have class="text-on-surface-variant ..."
        # What if we just search for '>CurrentPage</a>' and replace its class?
        # Let's use re.sub with a function that checks the tag contents.
        
        def process_a_tag(match):
            full_tag = match.group(0)
            inner_text = match.group(2)
            
            # If this is not the current page link, return it unchanged
            if inner_text.strip() != current_page:
                # wait, let me fix the mangled mobile link first if it exists
                if 'class="" class=""hover:text-secondary' in full_tag:
                    full_tag = full_tag.replace('class="" class=""hover:text-secondary', 'class="hover:text-secondary"')
                return full_tag
                
            # If it IS the current page:
            if 'text-on-surface-variant' in full_tag:
                # Desktop link
                new_tag = full_tag.replace('text-on-surface-variant', 'text-secondary font-bold border-b-2 border-secondary pb-1')
                return new_tag
            elif 'hover:text-secondary' in full_tag:
                # Mobile link
                new_tag = full_tag.replace('hover:text-secondary', 'text-secondary font-bold border-l-4 border-secondary pl-2')
                return new_tag
            elif 'class="" class=""hover:text-secondary' in full_tag:
                # Fix mangled mobile link
                new_tag = full_tag.replace('class="" class=""hover:text-secondary', 'class="text-secondary font-bold border-l-4 border-secondary pl-2"')
                return new_tag
            else:
                return full_tag
                
        # Regex to match ALL anchor tags
        # group 1: everything up to >
        # group 2: inner text
        # group 3: </a>
        content = re.sub(r'(<a\b[^>]*>)(.*?)(</a>)', process_a_tag, content, flags=re.DOTALL)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
            
    except Exception as e:
        print(f"Error {f}: {e}")

print("Active nav states fully fixed.")
