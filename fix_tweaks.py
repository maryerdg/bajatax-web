import re
import glob

# For persona-fisica: "Soluciones fiscales para personas físicas"
# -> "Soluciones fiscales para <span class="text-[#2e628e]">personas físicas</span>"
# For empresas: "Gestión fiscal integral para empresas"
# -> "Gestión fiscal integral para <span class="text-[#2e628e]">empresas</span>"

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if f == 'persona-fisica.html':
        content = content.replace(
            'Soluciones fiscales para personas físicas', 
            'Soluciones fiscales para <span class="text-surface-tint">personas físicas</span>'
        )
    elif f == 'empresas.html':
        content = content.replace(
            'Gestión fiscal integral para empresas', 
            'Gestión fiscal integral para <span class="text-surface-tint">empresas</span>'
        )

    # The user noted that the header is "muy grande" (too tall) in servicios.html
    # This is because the hero image height was forced to lg:h-[600px], making the whole section unnecessarily tall.
    # We will reduce it to lg:h-[450px] or h-[400px] across all secondary pages, and shrink padding.
    if f != 'index.html':
        # Reduce image forced height down from 600px to 400px to condense the header vertically
        content = content.replace('lg:h-[600px]', 'lg:h-[400px]')
        content = content.replace('h-[500px] lg:h-[400px]', 'h-[300px] lg:h-[400px]')
        
        # Shrink the massive bottom padding created by lg:pb-32 on these headers
        content = content.replace('pb-14 lg:pb-32', 'pb-14 lg:pb-20')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Tweaks applied successfully.")
