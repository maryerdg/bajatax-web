import urllib.request
import json
import base64

api_key = '5d84d84bf7ac96ea6f7e9c0e01f8923a-us11'

template_html = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=0">
  <title>BajaTax - Boletín</title>
</head>
<body style="margin:0; padding:0; background-color:#f4f7fa; font-family: 'Helvetica Neue', Arial, sans-serif;">

<!-- Wrapper -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f7fa;">
  <tr>
    <td align="center" style="padding: 30px 15px;">
      
      <!-- Email Container -->
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:12px; overflow:hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
        
        <!-- ============ HEADER / LOGO ============ -->
        <tr>
          <td align="center" style="background-color:#002b55; padding: 28px 40px;">
            <img src="https://bajatax-web.vercel.app/assets/bajatax-logo-blanco.png" alt="Baja Tax" width="180" style="display:block; max-width:180px; height:auto;">
          </td>
        </tr>
        
        <!-- ============ ETIQUETA DE CATEGORÍA ============ -->
        <tr>
          <td align="center" style="padding: 30px 40px 0 40px;">
            <table role="presentation" cellpadding="0" cellspacing="0">
              <tr>
                <td style="background-color:#e8f5e9; color:#2e7d32; font-size:11px; font-weight:bold; text-transform:uppercase; letter-spacing:2px; padding:6px 16px; border-radius:20px;">
                  mc:edit="categoria"
                  📋 Boletín Fiscal
                </td>
              </tr>
            </table>
          </td>
        </tr>
        
        <!-- ============ TÍTULO PRINCIPAL ============ -->
        <tr>
          <td align="center" style="padding: 24px 40px 10px 40px;">
            <h1 mc:edit="titulo" style="margin:0; color:#002b55; font-size:26px; font-weight:800; line-height:1.3;">
              Aquí va el título de tu boletín
            </h1>
          </td>
        </tr>
        
        <!-- ============ SUBTÍTULO / FECHA ============ -->
        <tr>
          <td align="center" style="padding: 0 40px 20px 40px;">
            <p mc:edit="subtitulo" style="margin:0; color:#5f6b78; font-size:14px;">
              Abril 2026 · Información fiscal relevante para tu negocio
            </p>
          </td>
        </tr>
        
        <!-- ============ LÍNEA DIVISORA ============ -->
        <tr>
          <td style="padding: 0 40px;">
            <hr style="border:none; border-top:2px solid #f4f7fa; margin:0;">
          </td>
        </tr>
        
        <!-- ============ CONTENIDO PRINCIPAL ============ -->
        <tr>
          <td style="padding: 28px 40px;">
            <p mc:edit="intro" style="margin:0 0 16px; color:#333333; font-size:15px; line-height:1.7;">
              Estimado(a) <strong>*|FNAME|*</strong>,
            </p>
            <p mc:edit="cuerpo1" style="margin:0 0 16px; color:#333333; font-size:15px; line-height:1.7;">
              Aquí puedes escribir el contenido principal de tu boletín. Te recomendamos mantener los párrafos cortos y directos para que tus clientes capten la información clave de inmediato.
            </p>
            <p mc:edit="cuerpo2" style="margin:0 0 16px; color:#333333; font-size:15px; line-height:1.7;">
              Puedes agregar más párrafos según necesites, incluir datos importantes sobre reformas fiscales, recordatorios de fechas límite o cualquier actualización relevante para sus obligaciones tributarias.
            </p>
          </td>
        </tr>
        
        <!-- ============ CUADRO DESTACADO ============ -->
        <tr>
          <td style="padding: 0 40px 28px 40px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
              <tr>
                <td mc:edit="destacado" style="background-color:#f0f7ff; border-left:4px solid #005c94; padding:20px 24px; border-radius:0 8px 8px 0;">
                  <p style="margin:0 0 4px; color:#005c94; font-size:13px; font-weight:bold; text-transform:uppercase; letter-spacing:1px;">
                    💡 Dato Importante
                  </p>
                  <p style="margin:0; color:#333; font-size:14px; line-height:1.6;">
                    Aquí puedes resaltar un punto clave, una fecha límite o un consejo fiscal que no quieres que se pierda entre el texto.
                  </p>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        
        <!-- ============ BOTÓN CTA ============ -->
        <tr>
          <td align="center" style="padding: 0 40px 32px 40px;">
            <table role="presentation" cellpadding="0" cellspacing="0">
              <tr>
                <td align="center" style="background-color:#4caf60; border-radius:8px;">
                  <a mc:edit="boton_link" href="https://bajatax.mx/contacto" target="_blank" style="display:inline-block; padding:16px 40px; color:#ffffff; font-size:15px; font-weight:bold; text-decoration:none; letter-spacing:0.5px;">
                    mc:edit="boton_texto"
                    Agenda tu Asesoría Gratuita →
                  </a>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        
        <!-- ============ LÍNEA DIVISORA ============ -->
        <tr>
          <td style="padding: 0 40px;">
            <hr style="border:none; border-top:2px solid #f4f7fa; margin:0;">
          </td>
        </tr>
        
        <!-- ============ FOOTER ============ -->
        <tr>
          <td style="padding: 28px 40px; background-color:#fafbfc;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
              <tr>
                <td align="center">
                  <img src="https://bajatax-web.vercel.app/assets/bajatax-logo-azul.png" alt="Baja Tax" width="120" style="display:block; max-width:120px; height:auto; margin-bottom:16px;">
                  <p style="margin:0 0 6px; color:#5f6b78; font-size:12px; line-height:1.5;">
                    Baja Tax · Asesoría Contable y Fiscal
                  </p>
                  <p style="margin:0 0 6px; color:#8a99a8; font-size:11px; line-height:1.5;">
                    Av. De Los Insurgentes, Tijuana, B.C., México
                  </p>
                  <p style="margin:0 0 12px; color:#8a99a8; font-size:11px;">
                    📞 (664) 733-8483 · 🌐 bajatax.mx
                  </p>
                  
                  <!-- Redes Sociales -->
                  <p style="margin:0 0 16px;">
                    <a href="https://www.instagram.com/bajatax" style="color:#005c94; text-decoration:none; font-size:12px; margin:0 8px;">Instagram</a>
                    <span style="color:#ddd;">|</span>
                    <a href="https://wa.me/526647338483" style="color:#005c94; text-decoration:none; font-size:12px; margin:0 8px;">WhatsApp</a>
                    <span style="color:#ddd;">|</span>
                    <a href="https://bajatax.mx" style="color:#005c94; text-decoration:none; font-size:12px; margin:0 8px;">Sitio Web</a>
                  </p>
                  
                  <hr style="border:none; border-top:1px solid #e8ecf0; margin:0 0 16px;">
                  
                  <p style="margin:0; color:#aab4be; font-size:10px; line-height:1.5;">
                    Recibes este correo porque te suscribiste en bajatax.mx<br>
                    <a href="*|UNSUB|*" style="color:#8a99a8;">Cancelar suscripción</a> · <a href="*|UPDATE_PROFILE|*" style="color:#8a99a8;">Actualizar preferencias</a>
                  </p>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        
      </table>
      <!-- /Email Container -->
      
    </td>
  </tr>
</table>
<!-- /Wrapper -->

</body>
</html>
"""

url = 'https://us11.api.mailchimp.com/3.0/templates'

data = json.dumps({
    'name': 'Plantilla Oficial BajaTax',
    'html': template_html
}).encode('utf-8')

req = urllib.request.Request(url, data=data, method='POST')
base64str = base64.b64encode(f'anystring:{api_key}'.encode('utf-8')).decode('utf-8')
req.add_header('Authorization', f'Basic {base64str}')
req.add_header('Content-Type', 'application/json')

try:
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))
        print(f"Template created! ID: {result.get('id')}, Name: {result.get('name')}")
except urllib.error.HTTPError as e:
    print(f'API Error: {e.code}')
    print(f'Response: {e.read().decode("utf-8")}')
