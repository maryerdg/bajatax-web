import glob
import re

standard_nav_class = 'class="fixed top-0 w-full z-50 bg-white/90 backdrop-blur-md"'
standard_inner_div = 'class="flex justify-between items-center px-8 py-4 max-w-7xl mx-auto"'
standard_logo = 'class="h-10 w-auto object-contain"'

standard_wa = '''<!-- Floating WhatsApp Button -->
<a class="fixed bottom-8 right-8 z-[60] bg-[#25D366] text-white w-16 h-16 rounded-full flex items-center justify-center shadow-2xl hover:scale-110 active:scale-95 transition-all group" href="https://wa.me/526647338483">
<span class="material-symbols-outlined text-4xl" style="font-variation-settings: 'FILL' 1;">chat</span>
<span class="absolute right-full mr-4 bg-white text-on-surface px-4 py-2 rounded-lg text-sm font-bold shadow-xl opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap pointer-events-none">¿Dudas? Habla con un experto</span>
</a>'''

html_files = glob.glob('*.html')
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Floating WhatsApp (Encontrar la ancla completa y reemplazarla)
    content = re.sub(r'<!-- Floating WhatsApp.*?</a>', standard_wa, content, flags=re.DOTALL | re.IGNORECASE)
    
    # Handle older comment format in persona-fisica
    if f == 'persona-fisica.html' and 'Floating WhatsApp' not in content:
        # Fallback for manual replacement if needed, but grep showed it's there
        pass
        
    # 2. Nav class 
    # Sustituye TODO lo del <nav class="...">
    content = re.sub(r'<nav class="[^"]+"[^>]*>', f'<nav {standard_nav_class}>', content)

    # 3. Inner Container
    # En index.html es <div class="flex justify-between items-center px-8 w-full max-w-[1400px] mx-auto">
    # En nosotros.html hay un segundo nav, tenemos que ser cuidadosos
    if f == 'index.html':
         content = content.replace('class="flex justify-between items-center px-8 w-full max-w-[1400px] mx-auto"', standard_inner_div)
         content = content.replace('class="h-10 w-auto"', standard_logo)
         
    elif f == 'empresas.html':
         content = content.replace('class="flex justify-between items-center px-8 py-4 max-w-7xl mx-auto"', standard_inner_div)
         content = content.replace('class="h-full object-contain"', standard_logo)
         
    elif f == 'contacto.html':
         content = content.replace('class="h-[32px] w-auto"', standard_logo)
         
    elif f == 'nosotros.html':
         content = content.replace('class="h-[32px] w-auto object-contain"', standard_logo)
         
    elif f == 'servicios.html':
         content = content.replace('class="h-8 w-auto object-contain"', standard_logo)
         
    elif f == 'recursos.html':
         content = content.replace('class="h-10 w-auto object-contain"', standard_logo)

    elif f == 'persona-fisica.html':
         content = content.replace('class="h-full object-contain"', standard_logo)

    # Quitar el h-[100px] o parecidos del header si hay
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
print("Updated all html files.")
