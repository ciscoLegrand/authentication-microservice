from flask import jsonify, make_response
from app.utils.logger import log_info, log_error
from app.utils.token_utils import fetch_token

def get_token():
    try:
        token = fetch_token()
        if not token:
            log_error("🤦 El token obtenido es nulo o vacío.")
            return None
        log_info("✅ get_token auth_controller -> Token obtenido con éxito.")
        return token
    except Exception as e:
        log_error(f"❌ Error inesperado auth_controller al obtener el token: {str(e)}")
        return None
