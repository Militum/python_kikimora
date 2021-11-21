import constants
from commands import CommandBase

class InitializeCommand(CommandBase):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, member: dict, options: dict) -> None:
        if 'administrator_role' not in options:
            raise Exception('パラメータ不足')

        super().validate(member, options)

    def execute(self, member: dict, options: dict)->dict:
        initial_text = 'hello kikimora'
        return {
            "type": constants.RESPONSE_TYPES['MESSAGE_WITH_SOURCE'],
            "data": {
                "content": initial_text
            }
        }
