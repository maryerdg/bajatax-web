import glob
import re

html_files = glob.glob('*.html')

hamburger_script = """
<!-- Mobile Menu Script -->
<script>
function toggleMobileMenu() {
    const menu = document.getElementById('mobile-menu');
    const isHidden = menu.classList.contains('translate-x-full');
    if (isHidden) {
        menu.classList.remove('translate-x-full');
        document.body.style.overflow = 'hidden';
    } else {
        menu.classList.add('translate-x-full');
        document.body.style.overflow = '';
    }
}
</script>
"""

new_nav_block = """<nav class="fixed top-0 w-full z-50 bg-white/90 backdrop-blur-md shadow-sm">
<div class="flex justify-between items-center px-6 md:px-8 py-3 md:py-4 max-w-7xl mx-auto">
<div class="flex items-center h-8 md:h-10">
<a href="/"><img alt="Baja Tax Logo" class="h-8 md:h-10 w-auto object-contain" src="assets/logo1.png"></a>
</div>
<div class="hidden md:flex gap-8 items-center">
<a class="text-on-surface-variant hover:text-primary font-headline font-semibold text-sm transition-colors duration-200" href="/">Inicio</a>
<a class="text-on-surface-variant hover:text-primary font-headline font-semibold text-sm transition-colors duration-200" href="/persona-fisica">Persona Física</a>
<a class="text-on-surface-variant hover:text-primary font-headline font-semibold text-sm transition-colors duration-200" href="/empresas">Empresas</a>
<a class="text-on-surface-variant hover:text-primary font-headline font-semibold text-sm transition-colors duration-200" href="/servicios">Servicios</a>
<a class="text-on-surface-variant hover:text-primary font-headline font-semibold text-sm transition-colors duration-200" href="/nosotros">Nosotros</a>
<a class="text-on-surface-variant hover:text-primary font-headline font-semibold text-sm transition-colors duration-200" href="/recursos">Recursos</a>
<a class="text-on-surface-variant hover:text-primary font-headline font-semibold text-sm transition-colors duration-200" href="/contacto">Contacto</a>
</div>
<a href="/contacto" class="hidden md:block text-white px-6 py-2.5 rounded-lg font-bold text-sm scale-95 hover:scale-100 transition-transform" style="background-color: #006e27;">
    Agenda tu asesoría
</a>
<button onclick="toggleMobileMenu()" class="md:hidden flex flex-col justify-center items-center w-10 h-10 space-y-1.5 focus:outline-none z-[60] bg-surface-container-low rounded-lg">
<span class="w-6 h-0.5 bg-primary rounded"></span>
<span class="w-6 h-0.5 bg-primary rounded"></span>
<span class="w-6 h-0.5 bg-primary rounded"></span>
</button>
</div>

<!-- Mobile Menu Overlay -->
<div id="mobile-menu" class="fixed inset-0 bg-white z-[55] transform translate-x-full transition-transform duration-300 md:hidden flex flex-col items-center justify-center space-y-6 text-2xl font-headline font-bold">
<button onclick="toggleMobileMenu()" class="absolute top-6 right-6 p-2 bg-surface-container-low rounded-full">
<span class="material-symbols-outlined text-primary">close</span>
</button>
<a href="/" class="text-primary hover:text-secondary">Inicio</a>
<a href="/persona-fisica" class="text-primary hover:text-secondary">Persona Física</a>
<a href="/empresas" class="text-primary hover:text-secondary">Empresas</a>
<a href="/servicios" class="text-primary hover:text-secondary">Servicios</a>
<a href="/nosotros" class="text-primary hover:text-secondary">Nosotros</a>
<a href="/recursos" class="text-primary hover:text-secondary">Recursos</a>
<a href="/contacto" class="text-primary hover:text-secondary">Contacto</a>
<a href="/contacto" class="mt-4 bg-secondary text-white px-8 py-4 rounded-xl font-bold text-lg">Agenda tu asesoría</a>
</div>
</nav>
"""

pages = ['index', 'nosotros', 'servicios', 'contacto', 'recursos', 'persona-fisica', 'empresas', 'privacidad', 'terminos']

for f in html_files:
    print(f"Processing {f}...")
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        with open(f, 'r', encoding='latin-1') as file:
            content = file.read()
    
    # Clean URLs
    for page in pages:
        if page == 'index':
             content = content.replace('href="index.html"', 'href="/"')
        else:
             content = content.replace(f'href="{page}.html"', f'href="/{page}"')
             
    # Replace Nav block
    # We find the <nav class="fixed top-0...>...</nav> block
    nav_pattern = r'<nav\b[^>]*class="fixed top-0\b[^>]*>.*?</nav>'
    content = re.sub(nav_pattern, new_nav_block, content, flags=re.DOTALL)
    
    # Inject mobile script before </body>
    if 'toggleMobileMenu' not in content:
        content = content.replace('</body>', hamburger_script + '\\n</body>')

    # Fix global sizing (H1 and H2 clamps) to scale down more on mobile
    content = content.replace('clamp(56px, 8vw, 64px)', 'clamp(36px, 8vw, 64px)')
    content = content.replace('clamp(48px, 6vw, 64px)', 'clamp(32px, 6vw, 64px)')
    content = content.replace('clamp(32px, 5vw, 48px)', 'clamp(28px, 5vw, 48px)')

    # Emulate apple button sizing for mobile by replacing `px-10 py-4` with `px-8 py-3 md:px-10 md:py-4` specifically in index.html hero
    if f == 'index.html':
         content = content.replace('px-10 py-4', 'px-6 py-3 md:px-10 md:py-4')
         content = content.replace('text-lg hover:brightness-105', 'text-base md:text-lg hover:brightness-105')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
print("Updated all html files for Mobile Layout and Clean URLs.")
