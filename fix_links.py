import re

with open('persona-fisica.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('href="/" style="">Inicio</a>', 'href="index.html" style="">Inicio</a>')
text = text.replace('href="/" style="">Nosotros</a>', 'href="nosotros.html" style="">Nosotros</a>')
text = text.replace('href="/" style="">Servicios</a>', 'href="servicios.html" style="">Servicios</a>')
text = text.replace('href="/" style="">Contacto</a>', 'href="contacto.html" style="">Contacto</a>')
text = text.replace('href="/" style="">Privacidad</a>', 'href="privacidad.html" style="">Privacidad</a>')
text = text.replace('href="/" style="">Términos</a>', 'href="terminos.html" style="">Términos</a>')

with open('persona-fisica.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Persona fisica footer links fixed")
