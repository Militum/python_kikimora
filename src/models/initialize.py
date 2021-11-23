import constants
from models import execute_command

def execute(member: dict, channel_id: str):
    execute_command.execute(member, {'name': 'register'}, channel_id)
