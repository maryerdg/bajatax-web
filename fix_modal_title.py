import os

html_file = 'recursos.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Make the title dynamic
old_title = '<h3 class="font-headline font-bold text-2xl text-primary mb-2">Desbloquea tu Documento</h3>'
new_title = '<h3 id="modalDynamicTitle" class="font-headline font-bold text-2xl text-primary mb-2">Desbloquea tu Documento</h3>'

if old_title in content:
    content = content.replace(old_title, new_title)

# Update openLeadModal to change title based on recursoName
old_js = """  function openLeadModal(pdfUrl, recursoName) {"""
new_js = """  function openLeadModal(pdfUrl, recursoName) {
    // Convertir nombre técnico a nombre amigable para el título
    let niceName = recursoName.replace('Recurso__', '').replace('.pdf', '').replace(/_/g, ' ').replace(/-/g, ' ');
    if (niceName.toLowerCase() === 'boletin laboral 2026') { niceName = 'Boletín Laboral'; } 
    niceName = niceName.charAt(0).toUpperCase() + niceName.slice(1);
    
    var titleEl = document.getElementById('modalDynamicTitle');
    if (titleEl) {
        titleEl.innerText = "Descargar " + niceName;
    }
"""

if old_js in content:
    content = content.replace(old_js, new_js)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated dynamic title.")
