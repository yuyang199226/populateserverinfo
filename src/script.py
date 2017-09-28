from lib.config import settings
from src.plugins import handle_plugin
from src.client import AgentClient,SshSaltstackClient

def start():
    if settings.MODE == 'ssh' or settings.MODE == 'saltstack':
        SshSaltstackClient().excute()
    elif settings.MODE == 'agent':
        AgentClient().excute()

    else:
        raise Exception('仅仅支持agent/ssh/saltstack')