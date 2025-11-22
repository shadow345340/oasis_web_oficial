import os

class Config:
    """Configuración que lee las variables desde Render"""
    
    # 1. SEGURIDAD
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-defecto')
    
    # 2. PANEL DE ADMINISTRACIÓN
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')

    # 3. CORREO
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'mathiascapote148@gmail.com')
  # --- CONFIGURACIÓN SSL (PUERTO 465) ---
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465             # Usamos 465
    MAIL_USE_TLS = False        # Apagamos TLS
    MAIL_USE_SSL = True         # Encendemos SSL
    
    MAIL_USERNAME = ADMIN_EMAIL
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ADMIN_EMAIL
    # DEBUG
    if not MAIL_PASSWORD:
        print("⚠️ ALERTA: No hay contraseña de correo.")
    else:
        print(f"✅ ÉXITO: Contraseña detectada (Longitud: {len(MAIL_PASSWORD)})")
