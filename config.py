import os

class Config:
    """Configuración que lee las variables desde Render"""
    
    # 1. SEGURIDAD
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-secreta-por-defecto-123')
    
    # 2. PANEL DE ADMINISTRACIÓN
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')

    # 3. CORREO
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'mathiascapote148@gmail.com')
    
    # --- CONFIGURACIÓN DE CORREO ESTÁNDAR (TLS - PUERTO 587) ---
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587             # Volvemos al 587
    MAIL_USE_TLS = True         # Encendemos TLS
    MAIL_USE_SSL = False        # Apagamos SSL
    
    MAIL_USERNAME = ADMIN_EMAIL
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ADMIN_EMAIL
    
    # DEBUG: Esto imprimirá en los logs si la contraseña fue leída correctamente
    if not MAIL_PASSWORD:
        print("⚠️ ADVERTENCIA: No se encontró la variable MAIL_PASSWORD en Render.")
    else:
        print("✅ ÉXITO: Se encontró una contraseña de correo configurada.")
