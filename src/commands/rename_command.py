
import constants
from commands import CommandBase

class RenameCommand(CommandBase):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, options: dict) -> None:
        if 'channel_name' not in options:
            raise Exception('パラメータ不足')

        super().validate(options)

    def execute(self, options: dict)->dict:
        text = 'RenameCommand'

        return {
            "type": constants.RESPONSE_TYPES['MESSAGE_WITH_SOURCE'],
            "data": {
                "content": text
            }
        }
