import os

class Config:
    """Configuración que lee las variables desde Render"""
    
    # 1. SEGURIDAD
    # Intenta leer la clave de Render, si no la encuentra, usa una por defecto (para pruebas)
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-secreta-por-defecto-123')
    
    # 2. PANEL DE ADMINISTRACIÓN
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')

    # 3. CORREO
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'mathiascapote148@gmail.com')
    
    # Aquí está la magia: Lee la contraseña de aplicación de las variables de Render
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ADMIN_EMAIL
    MAIL_DEFAULT_SENDER = ADMIN_EMAIL
