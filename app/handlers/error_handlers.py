from flask import jsonify
from app.utils.logger import log_warning, log_error

def handle_401_error(error):
    log_warning("Intento de acceso no autorizado detectado.")
    return jsonify(error="Unauthorized: Acceso no autorizado. Por favor, verifica tus credenciales."), 401

def handle_403_error(error):
    log_warning("Intento de acceso a un recurso prohibido detectado.")
    return jsonify(error="Forbidden: No tienes permiso para acceder a este recurso."), 403

def handle_404_error(error):
    log_warning("Se solicitó un recurso no encontrado.")
    return jsonify(error="Not Found: El recurso solicitado no existe."), 404

def handle_500_error(error):
    log_error("Se produjo un error interno del servidor.")
    return jsonify(error="Internal Server Error: Se produjo un error mientras se procesaba tu solicitud. Nuestro equipo ha sido notificado."), 500
