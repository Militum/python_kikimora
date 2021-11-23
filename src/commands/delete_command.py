
import constants
from commands import CommandBase

class DeleteCommand(CommandBase):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, member: dict, options: dict) -> None:
        super().validate(member, options)

    def execute(self, member: dict, options: dict, channel_id: str)->dict:
        text = 'DeleteCommand'

        return {
            "type": constants.RESPONSE_TYPES['MESSAGE_WITH_SOURCE'],
            "data": {
                "content": text
            }
        }
