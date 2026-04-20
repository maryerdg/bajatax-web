import glob
import re

html_files = glob.glob('*.html')

new_nav = '''
<!-- Standard Header -->
<nav class="fixed top-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-surface-dim/30">
  <div class="flex justify-between items-center px-6 py-3 md:px-8 md:py-4 max-w-7xl mx-auto">
    <!-- Logo -->
    <a href="/" class="flex-shrink-0">
      <img alt="Baja Tax Logo" class="h-8 md:h-10 w-auto object-contain" src="assets/logo1.png">
    </a>
    
    <!-- Link Desktop Container -->
    <div class="hidden md:flex gap-8 items-center">
      <a class="text-on-surface-variant hover:text-primary font-headline font-semibold text-sm transition-colors duration-200" href="/">Inicio</a>
      <a class="text-on-surface-variant hover:text-primary font-headline font-semibold text-sm transition-colors duration-200" href="/persona-fisica">Persona Física</a>
      <a class="text-on-surface-variant hover:text-primary font-headline font-semibold text-sm transition-colors duration-200" href="/empresas">Empresas</a>
      <a class="text-on-surface-variant hover:text-primary font-headline font-semibold text-sm transition-colors duration-200" href="/servicios">Servicios</a>
      <a class="text-on-surface-variant hover:text-primary font-headline font-semibold text-sm transition-colors duration-200" href="/nosotros">Nosotros</a>
      <a class="text-on-surface-variant hover:text-primary font-headline font-semibold text-sm transition-colors duration-200" href="/recursos">Recursos</a>
      <a class="text-on-surface-variant hover:text-primary font-headline font-semibold text-sm transition-colors duration-200" href="/contacto">Contacto</a>
      <a href="/contacto" class="bg-secondary text-white px-6 py-2.5 rounded-lg font-bold text-sm scale-95 hover:scale-100 transition-transform">Agenda tu asesoría</a>
    </div>

    <!-- Toggle Buttom (Mobile) -->
    <button onclick="document.getElementById('mobile-dropdown').classList.toggle('hidden')" class="md:hidden flex items-center justify-center p-2 text-primary bg-surface-container-low rounded-lg focus:outline-none focus:ring-2 focus:ring-secondary/50">
      <span class="material-symbols-outlined text-2xl">menu</span>
    </button>
  </div>

  <!-- Dropdown Menú (Mobile) - Se esconde por defecto -->
  <div id="mobile-dropdown" class="hidden md:hidden bg-white w-full border-t border-surface-dim/30 shadow-xl max-h-[80vh] overflow-y-auto">
    <div class="flex flex-col px-6 py-6 space-y-5 font-headline font-bold text-lg text-primary">
      <a href="/" class="hover:text-secondary">Inicio</a>
      <a href="/persona-fisica" class="hover:text-secondary">Persona Física</a>
      <a href="/empresas" class="hover:text-secondary">Empresas</a>
      <a href="/servicios" class="hover:text-secondary">Servicios</a>
      <a href="/nosotros" class="hover:text-secondary">Nosotros</a>
      <a href="/recursos" class="hover:text-secondary">Recursos</a>
      <a href="/contacto" class="hover:text-secondary">Contacto</a>
      <a href="/contacto" class="bg-secondary text-white text-center py-4 rounded-xl mt-4 font-extrabold shadow-md">Agenda tu asesoría</a>
    </div>
  </div>
</nav>
'''

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Replace nav completely
    nav_pattern = r'<nav\b[^>]*class="fixed top-0\b[^>]*>.*?</nav>'
    content = re.sub(nav_pattern, new_nav, content, flags=re.DOTALL)
    
    # Remove old script
    content = re.sub(r'<!-- Mobile Menu Script -->.*?</script>', '', content, flags=re.DOTALL)
    
    # 2. Fix Text Sizing and Spacing logic globally for Mobile
    content = content.replace('clamp(36px, 8vw, 64px)', 'clamp(28px, 6vw, 56px)')
    content = content.replace('clamp(28px, 5vw, 48px)', 'clamp(22px, 5vw, 40px)')
    
    # Target large card components and their spacings
    content = content.replace('p-8 md:p-12', 'p-6 md:p-12')
    content = content.replace('p-12 ', 'p-6 md:p-12 ')
    content = content.replace('p-10 ', 'p-5 md:p-10 ')
    content = content.replace('gap-10 ', 'gap-5 md:gap-10 ')
    content = content.replace('gap-24 ', 'gap-10 md:gap-24 ')
    content = content.replace('gap-20 ', 'gap-8 md:gap-20 ')
    content = content.replace('py-24 ', 'py-12 md:py-24 ')
    content = content.replace('pb-24 lg:pb-32', 'pb-14 lg:pb-32')
    
    # Target the top padding so it doesn't leave massive white space
    content = content.replace('pt-[180px]', 'pt-[120px] md:pt-[180px]')
    content = content.replace('pt-32', 'pt-28 md:pt-32')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Applied fix_layout_and_nav script")
