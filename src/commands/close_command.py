
import constants
from commands import CommandBase

class CloseCommand(CommandBase):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, options: dict) -> None:
        super().validate(options)

    def execute(self, options: dict)->dict:
        text = 'CloseCommand'

        return {
            "type": constants.RESPONSE_TYPES['MESSAGE_WITH_SOURCE'],
            "data": {
                "content": text
            }
        }
