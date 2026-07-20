from flask import current_app
import requests
from constants import AI_BOOKER_API_URL

def __request(method, endpoint, data=None):
    with current_app.app_context():
        current_app.logger.debug(f"Calling {AI_BOOKER_API_URL}{endpoint}")
    try:
        response = requests.request(
            method, f'{AI_BOOKER_API_URL}{endpoint}', json=data)
        return response
    except Exception as ex:
        print(ex)
        with current_app.app_context():
            current_app.logger.error(ex)

        return False

def get_telemetry():
    return __request("GET", f'/status-details/{agent_id}')