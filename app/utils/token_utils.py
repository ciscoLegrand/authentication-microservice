import os
import requests
from base64 import b64encode
from app.utils.logger import log_info, log_error, log_warning

def fetch_token():
    BASE_URL = os.environ.get("BASE_URL")
    url = BASE_URL + "/oauth/token"
    EMAIL = os.environ.get("EMAIL")
    PASS = os.environ.get("PASSWORD")
    headers = { "Authorization": "Basic " + b64encode(f"{EMAIL}:{PASS}".encode("utf-8")).decode("utf-8") }

    data = { "grant_type": "password" }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()

        token = response.json().get("access_token")
        if token:
            log_info("✅ Token obtenido con éxito. -> " + token)
            return token
        else:
            log_warning("⚠️ El token no está presente en la respuesta. " + response.text)
            raise ValueError("El token no está presente en la respuesta.")
    except requests.RequestException as e:
        error_msg = f"🔴 [ERROR] Error al obtener el token: {str(e)}"
        if hasattr(e, 'response') and e.response:
            error_msg += f" | Response: {e.response.status_code} - {e.response.text}"
        log_error(error_msg)
        raise e
