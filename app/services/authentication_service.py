from app.utils.token_utils import fetch_token
from app.utils.logger import log_info, log_error, log_warning

def get_current_token():
    try:
        token = fetch_token()
        
        if not token:
            log_warning("Se obtuvo un token vacío o nulo.")
            raise ValueError("Token inválido obtenido.")
        
        log_info("Token obtenido con éxito.")
        return token
    
    except ValueError as e:
        log_error(f"Error al procesar el token: {str(e)}")
        raise e
    except Exception as e:
        log_error(f"Error inesperado al obtener el token: {str(e)}")
        raise e
