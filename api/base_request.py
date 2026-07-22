from flask import current_app
import requests

def base_request(url, method, headers=None, data=None):
    if headers is None:
        headers = {}
    with current_app.app_context():
        current_app.logger.debug(f"Calling {url}")
    try:
        response = requests.request(
            method, f'{url}', headers=headers , json=data)
        return response
    except Exception as ex:
        with current_app.app_context():
            current_app.logger.error(ex)
        return False