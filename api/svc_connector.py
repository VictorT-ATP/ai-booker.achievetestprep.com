from flask import current_app
import requests
from .constants import AI_BOOKER_API_URL, AI_BOOKER_API_SECRET

def __request(method, endpoint, data=None):
    with current_app.app_context():
        current_app.logger.debug(f"Calling {AI_BOOKER_API_URL}{endpoint}")
    try:
        headers = {"X-Webhook-Secret": AI_BOOKER_API_SECRET }
        response = requests.request(
            method, f'{AI_BOOKER_API_URL}{endpoint}', headers=headers , json=data)
        return response
    except Exception as ex:
        with current_app.app_context():
            current_app.logger.error(ex)

        return False

def get_status_details(agent_id=''):
    response = __request("GET", f'/status-details/{agent_id}')
    print(response)
    return response