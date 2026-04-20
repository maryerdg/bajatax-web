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

phone = "526647338483"
global_msg = "Hola, vi su página de BajaTax y me gustaría recibir más información sobre sus servicios de asesoría."
encoded_global = urllib.parse.quote(global_msg)

specialized = {
    "servicios.html": [
        ("Impuestos", "Hola, visité la página web de BajaTax y me interesa recibir asesoría sobre impuestos"),
        ("Contabilidad", "Hola, visité la página web de BajaTax y me interesa recibir asesoría sobre contabilidad"),
        ("Nómina", "Hola, visité la página web de BajaTax y me interesa recibir asesoría sobre nómina"),
        ("Asesoría fiscal y legal", "Hola, visité la página web de BajaTax y me interesa recibir asesoría fiscal y legal"),
        ("Facturación", "Hola, visité la página web de BajaTax y me interesa recibir asesoría sobre facturación")
    ]
}

def update_file(filename):
    if not os.path.exists(filename):
        return
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update Floating Button (usually at the end, inside a fixed link)
    # We look for the link that has the fixed classes
    floating_pattern = re.compile(r'(<a [^>]*class="[^"]*fixed[^"]*right-8[^"]*"[^>]*href=")(https://wa\.me/526647338483[^"]*)(")', re.IGNORECASE)
    new_content = floating_pattern.sub(fr'\1https://wa.me/{phone}?text={encoded_global}\3', content)
    
    # Restore specialized if it's servicios.html
    if filename == "servicios.html":
        for title, msg in specialized[filename]:
            encoded_spec = urllib.parse.quote(msg)
            spec_url = f"https://wa.me/{phone}?text={encoded_spec}"
            
            # Find the anchor that follows the header with the title
            # This is tricky with regex, so we'll do a more direct search and replace for the specific blocks
            # We know the titles are unique.
            
            # Example: <h3>Title</h3> ... <a href="...">
            # We'll use a regex that matches the block and updates the href.
            block_pattern = re.compile(rf'(<h3[^>]*>{title}</h3>.*?<a [^>]*href=")(https://wa\.me/{phone}[^"]*)(")', re.DOTALL)
            new_content = block_pattern.sub(fr'\1{spec_url}\3', new_content)

    if content != new_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes for {filename}")

for f in files:
    update_file(f)
