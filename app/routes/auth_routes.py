from flask import Blueprint, jsonify, make_response
from app.controllers.auth_controller import get_token
from app.utils.logger import log_info, log_error
import requests

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/get_token', methods=['GET'])
def token_route():
    try:
        token = get_token()
        if not token:
            return jsonify(error="Token inválido obtenido."), 500
        log_info("✅ Token obtenido y enviado con éxito.")
        return jsonify(token=token), 200
    except requests.RequestException as re:
        error_detail = ""
        if hasattr(re, 'response') and re.response:
            error_detail = f" Response Status: {re.response.status_code}, Response Text: {re.response.text}."
        log_error(f"❌ Error relacionado con 'requests' al obtener el token: {str(re)}." + error_detail)
        return jsonify(error="Error al comunicarse con el servicio externo."), 500
    except Exception as e:
        log_error(f"❌ Error inesperado al obtener el token: {str(e)}")
        return jsonify(error="Error interno del servidor."), 500
