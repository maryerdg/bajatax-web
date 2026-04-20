import glob
import os
import re

PRIVACIDAD_CONTENT = """
  <!-- Privacy Section -->
  <section class="py-24 bg-white mt-16">
    <div class="max-w-[800px] mx-auto px-8">
      <h1 class="font-headline text-primary mb-8">Aviso de Privacidad</h1>
      
      <div class="space-y-6 text-on-surface-variant text-lg leading-relaxed">
        <p><strong>Última actualización: Abril 2026</strong></p>
        
        <p>En cumplimiento con la <strong>Ley Federal de Protección de Datos Personales en Posesión de los Particulares (LFPDPPP)</strong>, Baja Tax (en adelante "La Firma"), con domicilio en Plaza Insurgentes, Blvd. Insurgentes 18098, Río Tijuana 3.ª Etapa, Tijuana, B.C., es responsable de recabar sus datos personales, del uso que se le dé a los mismos y de su protección.</p>
        
        <h3 class="font-headline text-2xl text-primary mt-8 mb-4">1. Datos Personales que recabamos</h3>
        <p>Para las finalidades señaladas en el presente aviso de privacidad, podemos recabar sus datos personales de distintas formas: cuando usted nos los proporciona directamente, cuando visita nuestro sitio web o utiliza nuestros servicios en línea. Los datos incluyen: Nombre, teléfono, correo electrónico, RFC, y datos fiscales/contables relevantes para el servicio.</p>
        
        <h3 class="font-headline text-2xl text-primary mt-8 mb-4">2. Finalidades del tratamiento</h3>
        <p>Sus datos personales serán utilizados para las siguientes finalidades secundarias que nos permiten y facilitan brindarle un mejor servicio:</p>
        <ul class="list-disc pl-6 space-y-2">
            <li>Proveer los servicios contables y fiscales que ha solicitado.</li>
            <li>Notificarle sobre nuevos servicios o productos fiscales.</li>
            <li>Comunicarle cambios en la normativa fiscal del SAT.</li>
            <li>Evaluar la calidad del servicio que brindamos.</li>
        </ul>
        
        <h3 class="font-headline text-2xl text-primary mt-8 mb-4">3. Derechos ARCO</h3>
        <p>Usted tiene derecho de acceder, rectificar y cancelar sus datos personales, así como de oponerse al tratamiento de los mismos o revocar el consentimiento que nos ha otorgado (Derechos ARCO), a través del correo electrónico: <a href="mailto:info@bajatax.com" class="text-secondary font-bold hover:underline">info@bajatax.com</a>.</p>
        
        <h3 class="font-headline text-2xl text-primary mt-8 mb-4">4. Modificaciones al aviso</h3>
        <p>Nos reservamos el derecho de efectuar en cualquier momento modificaciones o actualizaciones al presente aviso de privacidad, para la atención de novedades legislativas o políticas internas. Estas modificaciones estarán disponibles al público en nuestra página de internet.</p>
      </div>
    </div>
  </section>
"""

TERMINOS_CONTENT = """
  <!-- Terms Section -->
  <section class="py-24 bg-white mt-16">
    <div class="max-w-[800px] mx-auto px-8">
      <h1 class="font-headline text-primary mb-8">Términos y Condiciones / Aviso Legal</h1>
      
      <div class="space-y-6 text-on-surface-variant text-lg leading-relaxed">
        <p><strong>Última actualización: Abril 2026</strong></p>
        
        <p>El acceso y uso del sitio web <strong>www.bajatax.com</strong> atribuye la condición de usuario e implica la aceptación de los siguientes términos y condiciones. Si no está de acuerdo con estos términos, le rogamos no utilizar nuestra página web.</p>
        
        <h3 class="font-headline text-2xl text-primary mt-8 mb-4">1. Uso del sitio web e información</h3>
        <p>El contenido publicado en esta página, incluyendo artículos de blog, boletines y descripciones de servicios, tiene una finalidad <strong>estrictamente informativa y educativa</strong>. La información aquí presentada no constituye asesoría fiscal, contable ni legal específica ("Disclaimer").</p>
        <p>La interpretación y aplicación de las leyes y normas del SAT cambian constantemente. Recomendamos encarecidamente consultar a nuestro equipo de contadores para analizar su situación particular antes de tomar decisiones en base al contenido de esta página web.</p>
        
        <h3 class="font-headline text-2xl text-primary mt-8 mb-4">2. Relación Contador - Cliente</h3>
        <p>El uso de este sitio web, llenar el formulario de contacto, o enviar correos electrónicos a la firma no crea automáticamente una relación contractual de Contador-Cliente. Dicha relación inicia formalmente cuando se firma una propuesta de servicios o contrato entre ambas partes.</p>
        
        <h3 class="font-headline text-2xl text-primary mt-8 mb-4">3. Propiedad Intelectual</h3>
        <p>Todos los logotipos, textos, diseños, boletines y materiales visuales contenidos en este sitio web son propiedad intelectual de Baja Tax. Queda prohibida su reproducción, distribución o uso para fines comerciales sin la autorización expresa y por escrito de la firma.</p>
        
        <h3 class="font-headline text-2xl text-primary mt-8 mb-4">4. Límite de responsabilidad</h3>
        <p>Baja Tax no se hace responsable por daños o contingencias fiscales que el usuario pueda sufrir derivados de la aplicación de la información general contenida en este sitio. Las resoluciones fiscales dependen enteramente del criterio de la autoridad competente (SAT) al revisar el caso específico del contribuyente.</p>
      </div>
    </div>
  </section>
"""

def generate_page(template_file, new_file, insert_html, title):
    with open(template_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract exactly navigation (from <nav> to </nav>)
    nav_match = re.search(r'(<nav.*?</nav>)', content, flags=re.DOTALL)
    nav_html = nav_match.group(1) if nav_match else ""

    # Extract exactly footer (from <footer> to </footer>)
    footer_match = re.search(r'(<footer.*</footer>)', content, flags=re.DOTALL)
    footer_html = footer_match.group(1) if footer_match else ""

    # Extract whatsapp button
    wa_match = re.search(r'(<a.*?floating whatsapp.*?</a.*?>)', content, flags=re.DOTALL | re.IGNORECASE)
    if not wa_match:
        wa_match = re.search(r'(<!-- Floating WhatsApp Button -->.*?</a>)', content, flags=re.DOTALL)
    wa_html = wa_match.group(1) if wa_match else ""

    # Generate head
    head = f"""<!DOCTYPE html>
<html class="scroll-smooth" lang="es">
<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>{title} | Baja Tax</title>
  <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">
"""
    
    # Extract tailwind config from index
    tw_match = re.search(r'(<script id="tailwind-config">.*?</script>)', content, flags=re.DOTALL)
    tw_html = tw_match.group(1) if tw_match else ""

    style = """
  <style>
    .material-symbols-outlined {
      font-variation-settings: 'FILL' 0, 'wght' 500, 'GRAD' 0, 'opsz' 24;
    }
    h1 { font-size: clamp(40px, 6vw, 48px) !important; font-weight: 800 !important; letter-spacing: -0.04em !important; line-height: 1.05 !important; }
    h2 { font-size: clamp(32px, 5vw, 48px) !important; font-weight: 700 !important; letter-spacing: -0.03em !important; }
    h3 { font-size: 28px !important; font-weight: 700 !important; letter-spacing: -0.02em !important; }
    body { font-size: 17px; }
  </style>
</head>
<body class="bg-white text-on-surface font-body leading-relaxed">
"""
    
    full_html = head + tw_html + style + nav_html + "\n" + insert_html + "\n" + footer_html + "\n\n" + wa_html + "\n</body>\n</html>"
    
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Created {new_file}")

def update_footers():
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Try multiple variations of the links in case there are subtle differences
        # Target:
        # <li><a class="hover:text-white transition-colors" href="/">Privacidad</a></li>
        # <li><a class="hover:text-white transition-colors" href="/">Términos</a></li>

        # Replace 'Privacidad' href
        content = re.sub(r'href="[^"]*"(>Privacidad<\/a>)', r'href="privacidad.html"\1', content)
        
        # Replace 'Términos' href
        content = re.sub(r'href="[^"]*"(>Términos<\/a>)', r'href="terminos.html"\1', content)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated footer in {file}")

if __name__ == "__main__":
    generate_page('index.html', 'privacidad.html', PRIVACIDAD_CONTENT, "Aviso de Privacidad")
    generate_page('index.html', 'terminos.html', TERMINOS_CONTENT, "Términos y Condiciones")
    update_footers()
    print("Done")
