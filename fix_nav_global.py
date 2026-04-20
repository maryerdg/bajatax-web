import glob
import re

html_files = glob.glob('*.html')

nav_template = '''<nav class="fixed top-0 w-full z-50 bg-white/90 backdrop-blur-md">
<div class="flex justify-between items-center px-8 py-4 max-w-7xl mx-auto">
<div class="flex items-center h-10">
<img alt="Baja Tax Logo" class="h-10 w-auto object-contain" src="assets/logo1.png">
</div>
<div class="hidden md:flex gap-8 items-center">
<a class="{c_inicio}" href="index.html">Inicio</a>
<a class="{c_persona}" href="persona-fisica.html">Persona Física</a>
<a class="{c_empresas}" href="empresas.html">Empresas</a>
<a class="{c_servicios}" href="servicios.html">Servicios</a>
<a class="{c_nosotros}" href="nosotros.html">Nosotros</a>
<a class="{c_recursos}" href="recursos.html">Recursos</a>
<a class="{c_contacto}" href="contacto.html">Contacto</a>
</div>
<a href="contacto.html" class="hidden md:block text-white px-6 py-2.5 rounded-lg font-bold text-sm scale-95 hover:scale-100 transition-transform" style="background-color: #006e27;">
    Agenda tu asesoría
</a>
</div>
</nav>'''

wa_template = '''<!-- Floating WhatsApp Button -->
<a class="fixed bottom-8 right-8 z-[60] bg-[#25D366] text-white w-16 h-16 rounded-full flex items-center justify-center shadow-2xl hover:scale-110 active:scale-95 transition-all group" href="https://wa.me/526647338483">
<span class="material-symbols-outlined text-4xl" style="font-variation-settings: 'FILL' 1;">chat</span>
<span class="absolute right-full mr-4 bg-white text-on-surface px-4 py-2 rounded-lg text-sm font-bold shadow-xl opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap pointer-events-none">¿Dudas? Habla con un experto</span>
</a>'''

inactive_class = "text-on-surface-variant hover:text-primary font-headline font-semibold text-sm transition-colors duration-200"
active_class = "text-primary border-b-2 border-secondary pb-1 font-headline font-bold text-sm"

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Format the template for the active file
    context = {
        'c_inicio': active_class if f == 'index.html' else inactive_class,
        'c_persona': active_class if f == 'persona-fisica.html' else inactive_class,
        'c_empresas': active_class if f == 'empresas.html' else inactive_class,
        'c_servicios': active_class if f == 'servicios.html' else inactive_class,
        'c_nosotros': active_class if f == 'nosotros.html' else inactive_class,
        'c_recursos': active_class if f == 'recursos.html' else inactive_class,
        'c_contacto': active_class if f == 'contacto.html' else inactive_class,
    }
    nav_injected = nav_template.format(**context)
    
    # Clean up old blocks
    # En nosotros.html and index.html they had <header> or weird wrappers.
    if '<header' in content and '<!-- Top Navigation -->' in content:
        # Just in case, index.html had Top Navigation but header was for hero
         content = re.sub(r'<!-- Top Navigation -->[\s\S]*?</nav>', nav_injected, content, flags=re.IGNORECASE)
    elif f == 'nosotros.html':
         # Delete the entire <header>...</header> block since it contains the nav
         content = re.sub(r'<header class="fixed top-0[\s\S]*?</header>', nav_injected, content, flags=re.IGNORECASE)
    else:
         # Standard greedy replacement for <nav> to </nav>
         content = re.sub(r'<nav class=[\s\S]*?</nav>', nav_injected, content, flags=re.IGNORECASE)
         
    # Fix the missing Top Navigation comment cleanup just in case
    content = content.replace('<!-- Top Navigation -->\n', '')
         
    # Replace WhatsApp
    content = re.sub(r'<!-- Floating WhatsApp.*?</a>', wa_template, content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<!-- WhatsApp Floating.*?</a>', wa_template, content, flags=re.DOTALL | re.IGNORECASE)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Nav standardized!")
