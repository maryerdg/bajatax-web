import re

# We will define a master template injector.
# All heroes will have:
# <header class="relative pt-[120px] md:pt-[180px] pb-14 lg:pb-32 overflow-hidden bg-white">
#   <div class="max-w-[1280px] mx-auto px-8 relative z-10">
#     <div class="grid lg:grid-cols-2 gap-10 md:gap-24 items-center">
#       <div class="space-y-6 md:space-y-10">
#         ... content ...
#       </div>
#       <div class="hidden lg:block w-full h-[600px] overflow-hidden rounded-[2.5rem] shadow-2xl">
#         ... image ...
#       </div>
#     </div>
#   </div>
# </header>

definitions = {
    'servicios.html': {
        'content': '''
          <p class="text-secondary font-bold tracking-[0.2em] uppercase text-xs">Nuestra Pericia</p>
          <h1 class="font-headline text-primary">Servicios contables y fiscales</h1>
          <p class="text-lg md:text-xl text-on-surface-variant leading-relaxed max-w-[500px]">
            Brindamos soluciones contables y fiscales para ayudarte a mantener tus finanzas en orden, cumplir correctamente y tomar decisiones con claridad.
          </p>
        ''',
        'image': 'https://plus.unsplash.com/premium_photo-1661608678096-7bb0a221fdd9'  # Based on standard business image
    },
    'nosotros.html': {
        'content': '''
          <p class="text-secondary font-bold tracking-[0.2em] uppercase text-xs">Nuestra Firma</p>
          <h1 class="font-headline text-primary">Claridad, orden y confianza para tus decisiones fiscales</h1>
          <p class="text-lg md:text-xl text-on-surface-variant leading-relaxed max-w-[500px]">
             Somos una firma local de contadores en Tijuana, Baja California, especializada en impuestos, nóminas, contabilidad, servicios legales y asesoría para negocios. Acompañamos a personas físicas y empresas con un enfoque claro, profesional y bilingüe.
          </p>
        ''',
        'image': 'https://images.unsplash.com/photo-1554224155-8d04cb21cd6c'
    },
    'persona-fisica.html': {
        'content': '''
          <p class="text-secondary font-bold tracking-[0.2em] uppercase text-xs">Servicios Especializados</p>
          <h1 class="font-headline text-primary">Soluciones fiscales para personas físicas</h1>
          <p class="text-lg md:text-xl text-on-surface-variant leading-relaxed max-w-[500px]">
             Te ayudamos a cumplir correctamente con tus obligaciones fiscales, mantener tus finanzas en orden y tomar decisiones con claridad y seguridad.
          </p>
          <div class="flex flex-col sm:flex-row gap-6 pt-2 items-center">
            <a href="/contacto" class="w-full sm:w-auto inline-flex justify-center bg-secondary text-white px-6 py-3 md:px-10 md:py-4 rounded-xl font-bold text-base md:text-lg hover:brightness-105 transition-all shadow-sm">Agendar asesoría</a>
            <a href="#servicios" class="w-full sm:w-auto inline-flex justify-center bg-slate-200 text-primary px-6 py-3 md:px-10 md:py-4 rounded-xl font-bold text-base md:text-lg hover:brightness-105 transition-all">Ver servicios</a>
          </div>
        ''',
        'image': 'https://images.unsplash.com/photo-1434626881859-194d67b2b86f'
    },
    'empresas.html': {
        'content': '''
          <p class="text-secondary font-bold tracking-[0.2em] uppercase text-xs">Soluciones Corporativas</p>
          <h1 class="font-headline text-primary">Gestión fiscal integral para empresas</h1>
          <p class="text-lg md:text-xl text-on-surface-variant leading-relaxed max-w-[500px]">
             Garantizamos el cumplimiento fiscal, contable y laboral de tu negocio para que puedas operar con total tranquilidad y proyección, desde Tijuana para el mundo.
          </p>
          <div class="flex flex-col sm:flex-row gap-6 pt-2 items-center">
            <a href="/contacto" class="w-full sm:w-auto inline-flex justify-center bg-secondary text-white px-6 py-3 md:px-10 md:py-4 rounded-xl font-bold text-base md:text-lg hover:brightness-105 transition-all shadow-sm">Agendar asesoría</a>
            <a href="#soluciones" class="w-full sm:w-auto inline-flex justify-center bg-slate-200 text-primary px-6 py-3 md:px-10 md:py-4 rounded-xl font-bold text-base md:text-lg hover:brightness-105 transition-all">Ver soluciones</a>
          </div>
        ''',
        'image': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40'
    },
    'recursos.html': {
        'content': '''
          <p class="text-secondary font-bold tracking-[0.2em] uppercase text-xs">Centro de Conocimiento</p>
          <h1 class="font-headline text-primary">Información fiscal clara</h1>
          <p class="text-lg md:text-xl text-on-surface-variant leading-relaxed max-w-[500px]">
             Accede a contenido práctico para entender tus obligaciones fiscales, evitar errores y tomar decisiones con mayor claridad.
          </p>
        ''',
        'image': 'https://images.unsplash.com/photo-1554224155-8d04cb21cd6c' # Reusing tax-related photo
    }
}

for filename, info in definitions.items():
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Capture existing image if available inside the original header to preserve what user chose!
        # Find all <img src="..."> in the header block.
        header_match = re.search(r'<header[^>]*>.*?</header>', content, flags=re.DOTALL)
        if header_match:
            original_header = header_match.group(0)
            img_match = re.search(r'<img[^>]+src="([^"]+)"', original_header)
            if img_match:
                info['image'] = img_match.group(1)
        
        # We replace the entire header block seamlessly!
        master_template = f'''<header class="relative pt-[120px] md:pt-[180px] pb-14 lg:pb-32 overflow-hidden bg-white">
    <div class="max-w-[1280px] mx-auto px-8 relative z-10">
      <div class="grid lg:grid-cols-2 gap-10 md:gap-24 items-center">
        <div class="space-y-6 md:space-y-10">
          {info['content']}
        </div>
        <div class="hidden lg:block w-full h-[500px] lg:h-[600px] rounded-[2.5rem] overflow-hidden shadow-2xl">
          <img alt="Hero Image" class="w-full h-full object-cover" src="{info['image']}">
        </div>
      </div>
    </div>
  </header>'''

        # perform RegExp replace, ignoring everything in the original header
        new_content = re.sub(r'<header[^>]*>.*?</header>', master_template, content, flags=re.DOTALL)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
    except Exception as e:
        print(f"Error modifying {filename}: {e}")

print("Hero unification complete successfully.")

