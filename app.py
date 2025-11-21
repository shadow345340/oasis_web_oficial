from flask import Flask, render_template, request, jsonify, redirect, url_for, session, make_response
import os
from datetime import datetime
from flask_mail import Mail, Message
from config import Config # Importamos el archivo de configuración

app = Flask(__name__)

# --- CARGAR CONFIGURACIÓN DESDE config.py ---
app.config.from_object(Config)

# Cargar las variables de la clase Config a variables locales para uso en funciones
ADMIN_PASSWORD = app.config['ADMIN_PASSWORD']
ADMIN_EMAIL = app.config['ADMIN_EMAIL']
# --------------------------------------------

mail = Mail(app)

# --- FUNCIÓN DE NOTIFICACIÓN AUTOMÁTICA ---
def enviar_notificacion_admin(nombre, correo, asunto, mensaje):
    """Envía un correo a ADMIN_EMAIL para notificar sobre un nuevo mensaje."""
    try:
        html_body = f"""
        <html>
        <body>
            <h3>¡Nuevo Mensaje de Contacto en Oasis Web!</h3>
            <p><strong>De:</strong> {nombre} ({correo})</p>
            <p><strong>Asunto:</strong> {asunto}</p>
            <hr>
            <p><strong>Mensaje:</strong></p>
            <p style="white-space: pre-wrap; background-color: #f4f4f9; padding: 10px; border: 1px solid #ddd;">{mensaje}</p>
            <p><strong>Fecha/Hora:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
            <hr>
            <p>Puedes responder a este correo directamente desde tu bandeja de entrada.</p>
        </body>
        </html>
        """

        msg = Message(
            subject=f"[OASIS WEB] Nuevo mensaje: {asunto}",
            recipients=[ADMIN_EMAIL], # Te lo envías a ti mismo
            html=html_body,
            sender=ADMIN_EMAIL
        )
        mail.send(msg)
        return True
    except Exception as e:
        # Esto es importante: si falla el correo, lo registramos pero no rompemos la web.
        print(f"ADVERTENCIA: Fallo al enviar correo de notificación al administrador: {e}")
        return False


# --- RUTAS DEL SITIO WEB ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acerca-de')
def acerca_de():
    return render_template('acerca_de.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        try:
            nombre = request.form.get('nombre')
            correo = request.form.get('correo')
            asunto = request.form.get('asunto')
            mensaje = request.form.get('mensaje')
            
            # 1. Guardar en el archivo (como copia de seguridad)
            if not os.path.exists('mensajes'):
                os.makedirs('mensajes')
            
            ruta_archivo = os.path.join('mensajes', 'mensajes.txt')
            
            with open(ruta_archivo, 'a', encoding='utf-8') as archivo:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                archivo.write(f"--- Nuevo Mensaje ({timestamp}) ---\n")
                archivo.write(f"Nombre: {nombre}\n")
                archivo.write(f"Correo: {correo}\n")
                archivo.write(f"Asunto: {asunto}\n")
                archivo.write(f"Mensaje: {mensaje}\n")
                archivo.write("-------------------------------------\n\n")

            # 2. Enviar notificación al administrador
            notificacion_enviada = enviar_notificacion_admin(nombre, correo, asunto, mensaje)

            if notificacion_enviada:
                respuesta = '¡Mensaje enviado con éxito! Te contactaremos pronto.'
            else:
                respuesta = 'Mensaje guardado. (Advertencia: Fallo la notificación por correo.)'

            return jsonify({'success': True, 'message': respuesta})

        except Exception as e:
            print(f"ERROR CRÍTICO al procesar el formulario de contacto: {e}")
            return jsonify({'success': False, 'message': 'Hubo un error interno al procesar tu solicitud.'}), 500
            
    return render_template('contacto.html')

# --- RUTAS DEL PANEL DE ADMINISTRACIÓN ---
# ... (las rutas de login y admin_panel son las mismas, ya que ahora respondes por Gmail)

@app.route('/gestion_interna_oas', methods=['GET', 'POST'], endpoint='admin_login')
def admin_login_route():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('admin_panel'), code=302)
        else:
            return render_template('admin_login.html', error='Contraseña incorrecta')
    
    response = make_response(render_template('admin_login.html'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/admin/ver-mensajes', endpoint='admin_panel')
def admin_panel_route():
    if not session.get('logged_in'):
        return redirect(url_for('admin_login'))
    
    # Lee los mensajes
    ruta_archivo = os.path.join('mensajes', 'mensajes.txt')
    mensajes = "No hay mensajes guardados aún. Ahora recibirás los mensajes directamente en tu Gmail."
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            mensajes = archivo.read()
            
    return render_template('admin_panel.html', mensajes=mensajes)

# La ruta de enviar_respuesta ya NO es necesaria porque respondes directamente desde Gmail.
# Simplemente se mantiene el admin_panel para ver la copia de seguridad.

if __name__ == '__main__':
    app.run(debug=True)
