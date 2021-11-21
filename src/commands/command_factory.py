from commands import InitializeCommand
from commands import HelpCommand
from commands import CommandBase

def create(command_name: str)->CommandBase:
    
    if command_name == 'administrator_role':
        return InitializeCommand()


    return HelpCommand()
