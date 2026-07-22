from .base_request import *
from .constants import AI_BOOKER_API_URL, AI_BOOKER_API_SECRET

def __request(method, endpoint, data=None):
    headers = {"X-Webhook-Secret": AI_BOOKER_API_SECRET}
    return base_request(f'{AI_BOOKER_API_URL}{endpoint}', method, headers=headers, data=data)

def get_status_details(agent_id=''):
    response = __request("GET", f'/status-details/{agent_id}')
    print(response)
    return response.json()