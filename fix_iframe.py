import os
import re

html_file = 'recursos.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the form entirely
old_form_start = '    <form id="leadForm" class="space-y-4" onsubmit="handleLeadSubmit(event)">'
old_form_end = '    </form>'

new_form_block = """    <!-- Hidden Iframe to bypass CORS -->
    <iframe name="hidden_iframe" id="hidden_iframe" style="display:none;" onload="if(submitted) { completeLeadFlow(); }"></iframe>
    
    <form id="leadForm" action="https://script.google.com/macros/s/AKfycbw8UaAkf5hTxBt3uxlmm9R9yzXlCi2zLgQ4Ibq6-ijieyOv2DgOUhReCZiIEdg3iqDi3A/exec" method="POST" target="hidden_iframe" class="space-y-4" onsubmit="submitted=true; prepForm();">
      <input type="hidden" id="leadPdfUrl">
      <input type="hidden" id="leadRecurso" name="recurso">
      <input type="hidden" id="leadTelefonoCompleto" name="telefono">
      
      <div>
        <label class="block text-xs font-bold text-primary mb-1 uppercase tracking-wider">Nombre completo</label>
        <input type="text" id="leadName" name="nombre" required placeholder="Ej. Juan Pérez" class="w-full bg-surface text-on-surface border border-outline-variant/30 rounded-xl px-4 py-3 focus:outline-none focus:border-secondary focus:ring-1 focus:ring-secondary transition-colors">
      </div>
      
      <div>
        <label class="block text-xs font-bold text-primary mb-1 uppercase tracking-wider">Número de WhatsApp</label>
        <div class="flex">
          <select id="leadLada" class="outline-none appearance-none cursor-pointer pl-3 pr-2 lg:px-4 rounded-l-xl border border-r-0 border-outline-variant/30 bg-surface-container-low text-on-surface-variant text-sm font-bold focus:outline-none focus:border-secondary transition-colors">
            <option value="+52">🇲🇽 +52</option>
            <option value="+1">🇺🇸 +1</option>
            <option value="+57">🇨🇴 +57</option>
            <option value="+54">🇦🇷 +54</option>
            <option value="+56">🇨🇱 +56</option>
            <option value="+51">🇵🇪 +51</option>
          </select>
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
    </form>"""

# Using regex to replace the form
content = re.sub(r'    <form id="leadForm" class="space-y-4" onsubmit="handleLeadSubmit\(event\)">.*?    </form>', new_form_block, content, flags=re.DOTALL)


# Replace JS block completely
old_js_block = r'<script>\s*const GOOGLE_SCRIPT_URL.*?</script>'

new_js_block = """<script>
  let submitted = false;

  function openLeadModal(pdfUrl, recursoName) {
    document.getElementById('leadPdfUrl').value = pdfUrl;
    document.getElementById('leadRecurso').value = recursoName;
    document.getElementById('leadPhone').value = '';
    document.getElementById('leadName').value = '';
    submitted = false;
    
    document.getElementById('leadSubmitBtn').innerHTML = '<span class="material-symbols-outlined text-lg">download</span><span>Continuar y Descargar</span>';
    document.getElementById('leadSubmitBtn').disabled = false;
    
    const overlay = document.getElementById('leadModalOverlay');
    const box = document.getElementById('leadModalBox');
    
    overlay.classList.remove('hidden');
    overlay.classList.add('flex');
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
      overlay.classList.remove('flex');
      overlay.classList.add('hidden');
    }, 300);
  }

  function prepForm() {
    // Unir lada + telefono
    const lada = document.getElementById('leadLada').value;
    const phone = document.getElementById('leadPhone').value;
    document.getElementById('leadTelefonoCompleto').value = lada + " " + phone;
    
    // Cambiar boton UI
    const btn = document.getElementById('leadSubmitBtn');
    btn.innerHTML = '<span class="material-symbols-outlined animate-spin">sync</span><span>Procesando...</span>';
    
    // Timeout of 3 seconds fallback if iframe onload bugs out
    setTimeout(() => {
        if(submitted) {
           completeLeadFlow();
        }
    }, 3000);
  }

  function completeLeadFlow() {
    if(!submitted) return;
    const pdfUrl = document.getElementById('leadPdfUrl').value;
    closeLeadModal();
    
    const a = document.createElement('a');
    a.href = pdfUrl;
    a.download = pdfUrl.split('/').pop() || 'BajaTax-Recurso.pdf';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    
    submitted = false; // reset
  }
</script>"""

content = re.sub(r'<script>\s*const GOOGLE_SCRIPT_URL.*?</script>', new_js_block, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated fallback form mechanism.")
