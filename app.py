# app.py

import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
# Flask-Mail ya no se usará, pero lo dejamos por si quieres activarlo después
from flask_mail import Mail, Message

# Importar configuración
from config import Config

# Inicializar Flask y configurar
app = Flask(__name__)
app.config.from_object(Config)

# Inicializar Flask-Mail (Mantenemos la inicialización por si la volvemos a usar)
mail = Mail(app)

# ----------------------------------------------------
# Nota: La función enviar_notificacion_admin ha sido eliminada
# ya que ahora usamos mailto: para evitar problemas de conexión.
# ----------------------------------------------------

# --- RUTAS PRINCIPALES ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

# ¡Ruta de Contacto Simplificada!
@app.route('/contacto', methods=['GET']) # Solo necesitamos GET
def contacto():
    return render_template('contacto.html')

# --- FUNCIÓN DE PRUEBA (Para ver logs y mensajes guardados) ---
@app.route('/test-messages')
def test_messages():
    try:
        with open('mensajes/mensajes.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        content = "El archivo de mensajes aún no existe."
    return f"<pre>{content}</pre>"


if __name__ == '__main__':
    # Esta línea es solo para desarrollo local, Render usa gunicorn
    app.run(debug=True)
