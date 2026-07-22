from elevenlabs.client import ElevenLabs
from .constants import ELEVENLABS_APIKEY

def get_agents():
    elevenlabs = ElevenLabs(api_key=ELEVENLABS_APIKEY)
    agents_list = elevenlabs.conversational_ai.agents.list()
    agents = []
    for agent in agents_list.agents:
        agents.append({'id': agent.agent_id, 'name': agent.name})
    return agents