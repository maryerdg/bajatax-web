import os
import re
import urllib.parse

files = [
    "index.html",
    "nosotros.html",
    "servicios.html",
    "persona-fisica.html",
    "empresas.html",
    "contacto.html",
    "recursos.html",
    "privacidad.html",
    "terminos.html"
]

phone_pattern = r'521?6647338483' # Matches 526647338483 or 5216647338483
new_msg = "Hola, vi su página de BajaTax y me gustaría recibir más información sobre sus servicios"
encoded_msg = urllib.parse.quote(new_msg)
new_url = f"https://wa.me/526647338483?text={encoded_msg}"

protected_phrases = [
    "asesoría sobre impuestos",
    "asesoría sobre contabilidad",
    "asesoría sobre nómina",
    "asesoría fiscal y legal",
    "asesoría sobre facturación"
]

def is_protected(url):
    decoded = urllib.parse.unquote(url)
    for phrase in protected_phrases:
        if phrase in decoded:
            return True
    return False

for filename in files:
    if not os.path.exists(filename):
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to find any wa.me or api.whatsapp link to the phone number
    # This covers: https://wa.me/NUMBER, https://api.whatsapp.com/send?phone=NUMBER, etc.
    wa_regex = re.compile(r'https?://(?:wa\.me|api\.whatsapp\.com/send)[^"\'\s>]*' + phone_pattern + r'[^"\'\s>]*', re.IGNORECASE)
    
    def replace_link(match):
        url = match.group(0)
        if is_protected(url):
            return url # Keep protected links
        return new_url
    
    new_content = wa_regex.sub(replace_link, content)
    
    if content != new_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes needed for {filename}")
