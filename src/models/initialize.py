import constants
from models import execute_command

def execute(member:dict):
    execute_command.execute(member, {'name': 'register'})
