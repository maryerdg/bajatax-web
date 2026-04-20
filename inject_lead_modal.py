import os
import re

html_file = 'recursos.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Reemplazar Boletín Laboral
old_laboral = '<a href="assets/boletines/boletin-jornada-laboral-2026/boletin-jornada-laboral-2026.pdf" download class="bg-secondary text-white hover:bg-[#00531b] transition-colors duration-300 w-full sm:w-auto px-8 py-4 rounded-lg font-bold text-base md:text-lg text-center flex justify-center items-center gap-3 shadow-lg hover:shadow-xl hover:-translate-y-1 transform">'
new_laboral = '<button onclick="openLeadModal(\'assets/boletines/boletin-jornada-laboral-2026/boletin-jornada-laboral-2026.pdf\', \'Boletin_Laboral_2026\')" class="bg-secondary text-white hover:bg-[#00531b] transition-colors duration-300 w-full sm:w-auto px-8 py-4 rounded-lg font-bold text-base md:text-lg text-center flex justify-center items-center gap-3 shadow-lg hover:shadow-xl hover:-translate-y-1 transform">'
if old_laboral in content:
    content = content.replace(old_laboral, new_laboral)
    content = content.replace('Descargar PDF\n</a>', 'Descargar PDF\n</button>', 1) # only replace the first closed </a> for this button or do it via regex

# Better regex approach
# This regex finds the specific <a> tags with 'download' and replaces them with <button> elements
content = re.sub(
    r'<a href="([^"]+\.pdf)" download([^>]*)>(.*?)</a>',
    lambda m: f'<button type="button" onclick="openLeadModal(\'{m.group(1)}\', \'Recurso__{os.path.basename(m.group(1))}\')" {m.group(2)}>{m.group(3)}</button>',
    content,
    flags=re.DOTALL
)

modal_html = """
<!-- Lead Capture Modal -->
<div id="leadModalOverlay" class="fixed inset-0 bg-[#001d34]/80 z-[100] hidden items-center justify-center backdrop-blur-sm px-4 transition-opacity duration-300 opacity-0">
  <div class="bg-surface-container-lowest rounded-2xl p-8 md:p-10 max-w-md w-full shadow-2xl relative transform scale-95 transition-transform duration-300" id="leadModalBox">
    <!-- Close Button -->
    <button onclick="closeLeadModal()" class="absolute top-4 right-4 text-outline hover:text-primary transition-colors bg-surface-container rounded-full p-1">
      <span class="material-symbols-outlined">close</span>
    </button>
    
    <div class="text-center mb-6">
      <div class="bg-primary/5 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4 text-primary">
         <span class="material-symbols-outlined text-3xl">picture_as_pdf</span>
      </div>
      <h3 class="font-headline font-bold text-2xl text-primary mb-2">Desbloquea tu Documento</h3>
      <p class="text-on-surface-variant text-sm">Déjanos tu nombre y WhatsApp para acceder al instante. Solo te enviaremos información relevante.</p>
    </div>
    
    <form id="leadForm" class="space-y-4" onsubmit="handleLeadSubmit(event)">
      <input type="hidden" id="leadPdfUrl" name="pdfUrl">
      <input type="hidden" id="leadRecurso" name="recurso">
      
      <div>
        <label class="block text-xs font-bold text-primary mb-1 uppercase tracking-wider">Nombre completo</label>
        <input type="text" id="leadName" required placeholder="Ej. Juan Pérez" class="w-full bg-surface text-on-surface border border-outline-variant/30 rounded-xl px-4 py-3 focus:outline-none focus:border-secondary focus:ring-1 focus:ring-secondary transition-colors">
      </div>
      
      <div>
        <label class="block text-xs font-bold text-primary mb-1 uppercase tracking-wider">Número de WhatsApp</label>
        <div class="flex">
          <span class="inline-flex items-center px-4 rounded-l-xl border border-r-0 border-outline-variant/30 bg-surface-container-low text-on-surface-variant text-sm font-bold">
            +52
          </span>
          <input type="tel" id="leadPhone" required pattern="[0-9]{10}" placeholder="10 dígitos (Ej. 6640000000)" class="w-full bg-surface text-on-surface border border-outline-variant/30 rounded-r-xl px-4 py-3 focus:outline-none focus:border-secondary focus:ring-1 focus:ring-secondary transition-colors" title="Debe contener 10 números estadísticos">
        </div>
      </div>
      
      <button type="submit" id="leadSubmitBtn" class="w-full bg-secondary hover:bg-[#00531b] text-white font-bold py-4 rounded-xl mt-4 flex items-center justify-center gap-2 transition-colors shadow-lg">
        <span class="material-symbols-outlined text-lg">download</span>
        <span>Continuar y Descargar</span>
      </button>
      
      <p class="text-[10px] text-center text-on-surface-variant mt-4">
        Los datos recopilados están protegidos de acuerdo a nuestro <a href="/privacidad" class="text-secondary font-bold hover:underline">Aviso de Privacidad</a>.
      </p>
    </form>
  </div>
</div>

<script>
  const GOOGLE_SCRIPT_URL = 'PONER_AQUI_LA_URL_DEL_SCRIPT'; // <--- Placeholder para la de Google

  function openLeadModal(pdfUrl, recursoName) {
    document.getElementById('leadPdfUrl').value = pdfUrl;
    document.getElementById('leadRecurso').value = recursoName;
    
    const overlay = document.getElementById('leadModalOverlay');
    const box = document.getElementById('leadModalBox');
    
    overlay.classList.remove('hidden');
    // peqeño timeout para la transición
    setTimeout(() => {
      overlay.classList.remove('opacity-0');
      box.classList.remove('scale-95');
    }, 10);
  }

  function closeLeadModal() {
    const overlay = document.getElementById('leadModalOverlay');
    const box = document.getElementById('leadModalBox');
    
    overlay.classList.add('opacity-0');
    box.classList.add('scale-95');
    
    setTimeout(() => {
      overlay.classList.add('hidden');
    }, 300);
  }

  async function handleLeadSubmit(e) {
    e.preventDefault();
    
    const btn = document.getElementById('leadSubmitBtn');
    const originalText = btn.innerHTML;
    
    const name = document.getElementById('leadName').value;
    const phone = document.getElementById('leadPhone').value;
    const pdfUrl = document.getElementById('leadPdfUrl').value;
    const recurso = document.getElementById('leadRecurso').value;
    
    // UI Estado de carga
    btn.innerHTML = '<span class="material-symbols-outlined animate-spin">sync</span><span>Procesando...</span>';
    btn.disabled = true;
    
    try {
      // Si aún no hemos configurado la URL real de Google Script
      if(GOOGLE_SCRIPT_URL.includes('PONER_AQUI_LA_URL_DEL_SCRIPT')) {
          console.warn("Falta URL del Script! Simulando registro...");
          triggerDownload(pdfUrl);
          return;
      }

      // Enviar datos al Google Script
      const formData = new FormData();
      formData.append('nombre', name);
      formData.append('telefono', phone);
      formData.append('recurso', recurso);
      
      // Enviamos con fetch a modo no-cors o con cors manejado
      await fetch(GOOGLE_SCRIPT_URL, {
        method: 'POST',
        body: formData,
        mode: 'no-cors' // Usamos no-cors porque google script manda redirect
      });
      
      // Una vez "enviado", disparamos la descarga
      triggerDownload(pdfUrl);
      
    } catch(err) {
      console.error('Error al registrar lead:', err);
      // Aun si falla la conexion por algo eventual, que el cliente no se quede sin descargar
      triggerDownload(pdfUrl);
    } finally {
      // Limpiar UI
      btn.innerHTML = originalText;
      btn.disabled = false;
    }
  }

  function triggerDownload(pdfUrl) {
    closeLeadModal();
    // Inicia la descarga
    const a = document.createElement('a');
    a.href = pdfUrl;
    a.download = pdfUrl.split('/').pop() || 'BajaTax-Recurso.pdf';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  }
</script>
"""

# Insert logic and modal at the bottom just before </body>
content = content.replace('</body>', '\n' + modal_html + '\n</body>')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated recursos.html to include the lead modal and replace direct downloads.")
