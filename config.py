import os

class Config:
    """Configuración que lee las variables desde Render"""
    
    # 1. SEGURIDAD
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-secreta-por-defecto-123')
    
    # 2. PANEL DE ADMINISTRACIÓN
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')

    # 3. CORREO
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'mathiascapote148@gmail.com')
    
    # --- CONFIGURACIÓN DE CORREO CORREGIDA (SSL) ---
    # Usamos el puerto 465 con SSL para evitar el "Error de conexión/Timeout"
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465             # <--- CAMBIO IMPORTANTE: Puerto SSL
    MAIL_USE_TLS = False        # <--- Apagamos TLS
    MAIL_USE_SSL = True         # <--- Encendemos SSL (Más rápido y seguro)
    
    MAIL_USERNAME = ADMIN_EMAIL
    # Lee la contraseña de 16 caracteres de las variables de Render
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    MAIL_DEFAULT_SENDER = ADMIN_EMAIL
