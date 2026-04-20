import os

html_file = 'recursos.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the fetch with explicit form-urlencoded without 'no-cors' 
# or with an iframe/form approach which is 100% reliable.
old_fetch = """      // Convertir a x-www-form-urlencoded para mejor compatibilidad con Apps Script
      const params = new URLSearchParams();
      params.append('nombre', name);
      params.append('telefono', phone);
      params.append('recurso', recurso);
      
      await fetch(GOOGLE_SCRIPT_URL, {
        method: 'POST',
        body: params,
        mode: 'no-cors'
      });"""

new_fetch = """      // Enviar datos vía form-urlencoded explícito a Apps Script
      const dataStr = 'nombre=' + encodeURIComponent(name) + '&telefono=' + encodeURIComponent(phone) + '&recurso=' + encodeURIComponent(recurso);
      
      await fetch(GOOGLE_SCRIPT_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: dataStr,
        mode: 'no-cors'
      });"""

if old_fetch in content:
    content = content.replace(old_fetch, new_fetch)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated fetch explicit headers.")
else:
    print("Could not find the fetch block.")
