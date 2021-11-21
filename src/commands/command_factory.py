from commands import CommandBase

from commands import RecruitCommand
from commands import RoomCommand
from commands import CampaignCommand
from commands import RenameCommand
from commands import CloseCommand
from commands import DeleteCommand
from commands import HelpCommand

#from commands import InitializeCommand
#from commands import RegisterCommand

def create(command_name: str)->CommandBase:
    
    if command_name == 'recruit':
        return RecruitCommand()
    elif command_name == 'room':
        return RoomCommand()
    elif command_name == 'campaign':
        return CampaignCommand()
    elif command_name == 'rename':
        return RenameCommand()
    elif command_name == 'close':
        return CloseCommand()
    elif command_name == 'delete':
        return DeleteCommand()
    elif command_name == 'help':
        return HelpCommand()

    # todo 適合しなかった場合はHelpにするかエラーとするか決定する
    return HelpCommand()
