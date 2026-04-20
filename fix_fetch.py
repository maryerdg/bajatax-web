import os

html_file = 'recursos.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace FormData with URLSearchParams
old_form_data = """      const formData = new FormData();
      formData.append('nombre', name);
      formData.append('telefono', phone);
      formData.append('recurso', recurso);
      
      // Enviamos con fetch a modo no-cors o con cors manejado
      await fetch(GOOGLE_SCRIPT_URL, {
        method: 'POST',
        body: formData,
        mode: 'no-cors' // Usamos no-cors porque google script manda redirect
      });"""

new_form_data = """      // Convertir a x-www-form-urlencoded para mejor compatibilidad con Apps Script
      const params = new URLSearchParams();
      params.append('nombre', name);
      params.append('telefono', phone);
      params.append('recurso', recurso);
      
      await fetch(GOOGLE_SCRIPT_URL, {
        method: 'POST',
        body: params,
        mode: 'no-cors'
      });"""

if old_form_data in content:
    content = content.replace(old_form_data, new_form_data)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated form data handler.")
else:
    print("Could not find the old block.")
