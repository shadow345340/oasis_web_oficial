# config.py - Configuración centralizada

class Config:
    """Configuración base para el entorno de desarrollo y producción."""
    
    # --- 1. SEGURIDAD Y SESIÓN (OBLIGATORIO) ---
    # La clave que generaste para la sesión.
    SECRET_KEY = '698854dde8f9873df66f42337294a493d6c4624faeeac086281e9cf0d31eb8fe'
    
    # Contraseña para el panel de administración. ¡CAMBIA ESTO!
    ADMIN_PASSWORD = 'JESUS_VIVE_POR_SIEMPRE' 

    # --- 2. CONFIGURACIÓN DE CORREO ---
    # Tu correo de administrador (usado para enviar y recibir notificaciones).
    ADMIN_EMAIL = 'mathiascapote148@gmail.com'

    # Clave de aplicación de 16 caracteres de Google. ¡CAMBIA ESTO!
    MAIL_PASSWORD = 'eyic xihr nmgj gyan' 
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ADMIN_EMAIL
    MAIL_DEFAULT_SENDER = ADMIN_EMAIL
