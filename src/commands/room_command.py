
import constants
from commands import CommandBase

class RoomCommand(CommandBase):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, member: dict, options: dict) -> None:
        if 'channel_name' not in options:
            raise Exception('パラメータ不足')

        super().validate(member, options)

    def execute(self, member: dict, options: dict)->dict:
        text = 'RoomCommand'

        return {
            "type": constants.RESPONSE_TYPES['MESSAGE_WITH_SOURCE'],
            "data": {
                "content": text
            }
        }
