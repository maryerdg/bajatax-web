import urllib.request
import json
import base64

api_key = '5d84d84bf7ac96ea6f7e9c0e01f8923a-us11'
template_id = '10031084'

font_base = 'https://bajatax-web.vercel.app/assets/poppins'
poppins = "'Poppins', Arial, sans-serif"

template_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BajaTax</title>
<style>
@font-face {{
  font-family: 'Poppins';
  src: url('{font_base}/Poppins-Regular.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
}}
@font-face {{
  font-family: 'Poppins';
  src: url('{font_base}/Poppins-Medium.ttf') format('truetype');
  font-weight: 500;
  font-style: normal;
}}
@font-face {{
  font-family: 'Poppins';
  src: url('{font_base}/Poppins-SemiBold.ttf') format('truetype');
  font-weight: 600;
  font-style: normal;
}}
@font-face {{
  font-family: 'Poppins';
  src: url('{font_base}/Poppins-Bold.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
}}
@font-face {{
  font-family: 'Poppins';
  src: url('{font_base}/Poppins-ExtraBold.ttf') format('truetype');
  font-weight: 800;
  font-style: normal;
}}
</style>
</head>
<body style="margin:0; padding:0; background-color:#f4f7fa; font-family: {poppins};">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f7fa;">
<tr>
<td align="center" style="padding: 30px 15px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:12px; overflow:hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">

<tr>
<td align="center" style="background-color:#002b55; padding: 28px 40px;">
<img src="https://bajatax-web.vercel.app/assets/bajatax-logo-blanco.png" alt="Baja Tax" width="180" style="display:block; max-width:180px; height:auto;">
</td>
</tr>

<tr>
<td align="center" style="padding: 30px 40px 0 40px;">
<table role="presentation" cellpadding="0" cellspacing="0">
<tr>
<td mc:edit="categoria" style="background-color:#e8f5e9; color:#2e7d32; font-family: {poppins}; font-size:11px; font-weight:600; text-transform:uppercase; letter-spacing:2px; padding:6px 16px; border-radius:20px;">
Boletin Fiscal
</td>
</tr>
</table>
</td>
</tr>

<tr>
<td align="center" style="padding: 24px 40px 10px 40px;">
<h1 mc:edit="titulo" style="margin:0; color:#002b55; font-family: {poppins}; font-size:26px; font-weight:800; line-height:1.3;">
Aqui va el titulo de tu boletin
</h1>
</td>
</tr>

<tr>
<td align="center" style="padding: 0 40px 20px 40px;">
<p mc:edit="subtitulo" style="margin:0; color:#5f6b78; font-family: {poppins}; font-size:14px; font-weight:400;">
Abril 2026 - Informacion fiscal relevante para tu negocio
</p>
</td>
</tr>

<tr>
<td style="padding: 0 40px;">
<hr style="border:none; border-top:2px solid #f4f7fa; margin:0;">
</td>
</tr>

<tr>
<td style="padding: 28px 40px;">
<p mc:edit="intro" style="margin:0 0 16px; color:#333333; font-family: {poppins}; font-size:15px; font-weight:400; line-height:1.7;">
Estimado(a) <strong>*|FNAME|*</strong>,
</p>
<p mc:edit="cuerpo1" style="margin:0 0 16px; color:#333333; font-family: {poppins}; font-size:15px; font-weight:400; line-height:1.7;">
Aqui puedes escribir el contenido principal de tu boletin. Te recomendamos mantener los parrafos cortos y directos para que tus clientes capten la informacion clave de inmediato.
</p>
<p mc:edit="cuerpo2" style="margin:0 0 16px; color:#333333; font-family: {poppins}; font-size:15px; font-weight:400; line-height:1.7;">
Puedes agregar mas parrafos segun necesites, incluir datos importantes sobre reformas fiscales, recordatorios de fechas limite o cualquier actualizacion relevante para sus obligaciones tributarias.
</p>
</td>
</tr>

<tr>
<td style="padding: 0 40px 28px 40px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr>
<td mc:edit="destacado" style="background-color:#f0f7ff; border-left:4px solid #005c94; padding:20px 24px; border-radius:0 8px 8px 0;">
<p style="margin:0 0 4px; color:#005c94; font-family: {poppins}; font-size:13px; font-weight:700; text-transform:uppercase; letter-spacing:1px;">
Dato Importante
</p>
<p style="margin:0; color:#333; font-family: {poppins}; font-size:14px; font-weight:400; line-height:1.6;">
Aqui puedes resaltar un punto clave, una fecha limite o un consejo fiscal que no quieres que se pierda entre el texto.
</p>
</td>
</tr>
</table>
</td>
</tr>

<tr>
<td align="center" style="padding: 0 40px 32px 40px;">
<table role="presentation" cellpadding="0" cellspacing="0">
<tr>
<td align="center" style="background-color:#4caf60; border-radius:8px;">
<a mc:edit="boton" href="https://bajatax.mx/contacto" target="_blank" style="display:inline-block; padding:16px 40px; color:#ffffff; font-family: {poppins}; font-size:15px; font-weight:700; text-decoration:none; letter-spacing:0.5px;">
Agenda tu Asesoria Gratuita
</a>
</td>
</tr>
</table>
</td>
</tr>

<tr>
<td style="padding: 0 40px;">
<hr style="border:none; border-top:2px solid #f4f7fa; margin:0;">
</td>
</tr>

<tr>
<td style="padding: 28px 40px; background-color:#fafbfc;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr>
<td align="center">
<img src="https://bajatax-web.vercel.app/assets/bajatax-logo-azul.png" alt="Baja Tax" width="120" style="display:block; max-width:120px; height:auto; margin-bottom:16px;">
<p style="margin:0 0 6px; color:#5f6b78; font-family: {poppins}; font-size:12px; font-weight:500; line-height:1.5;">
Baja Tax - Asesoria Contable y Fiscal
</p>
<p style="margin:0 0 6px; color:#8a99a8; font-family: {poppins}; font-size:11px; font-weight:400; line-height:1.5;">
Av. De Los Insurgentes, Tijuana, B.C., Mexico
</p>
<p style="margin:0 0 12px; color:#8a99a8; font-family: {poppins}; font-size:11px; font-weight:400;">
Tel: (664) 733-8483 | bajatax.mx
</p>
<p style="margin:0 0 16px;">
<a href="https://www.instagram.com/bajatax" style="color:#005c94; font-family: {poppins}; text-decoration:none; font-size:12px; font-weight:500; margin:0 8px;">Instagram</a>
<span style="color:#ddd;">|</span>
<a href="https://wa.me/526647338483" style="color:#005c94; font-family: {poppins}; text-decoration:none; font-size:12px; font-weight:500; margin:0 8px;">WhatsApp</a>
<span style="color:#ddd;">|</span>
<a href="https://bajatax.mx" style="color:#005c94; font-family: {poppins}; text-decoration:none; font-size:12px; font-weight:500; margin:0 8px;">Sitio Web</a>
</p>
<hr style="border:none; border-top:1px solid #e8ecf0; margin:0 0 16px;">
<p style="margin:0; color:#aab4be; font-family: {poppins}; font-size:10px; font-weight:400; line-height:1.5;">
Recibes este correo porque te suscribiste en bajatax.mx<br>
<a href="*|UNSUB|*" style="color:#8a99a8;">Cancelar suscripcion</a> | <a href="*|UPDATE_PROFILE|*" style="color:#8a99a8;">Actualizar preferencias</a>
</p>
</td>
</tr>
</table>
</td>
</tr>

</table>
</td>
</tr>
</table>
</body>
</html>"""

url = f'https://us11.api.mailchimp.com/3.0/templates/{template_id}'

data = json.dumps({
    'name': 'Plantilla Oficial BajaTax',
    'html': template_html
}).encode('utf-8')

req = urllib.request.Request(url, data=data, method='PATCH')
base64str = base64.b64encode(f'anystring:{api_key}'.encode('utf-8')).decode('utf-8')
req.add_header('Authorization', f'Basic {base64str}')
req.add_header('Content-Type', 'application/json')

try:
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))
        print(f"Template updated! ID: {result.get('id')}, Name: {result.get('name')}")
except urllib.error.HTTPError as e:
    print(f'API Error: {e.code}')
    print(f'Response: {e.read().decode("utf-8")}')
