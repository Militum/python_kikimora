
import constants
from commands import CommandBase
from discord import rename_channel, get_channel

class CloseCommand(CommandBase):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, member: dict, options: dict) -> None:
        super().validate(member, options)

    def execute(self, member: dict, options: dict, channel_id: str)->dict:
        # コマンドを実行したチャンネルは必ずある
        text_channel = get_channel.get_channel_by_id(channel_id)

        target_channel_name = text_channel.get('name')

        if target_channel_name.startswith('〆'):
            return {
                "type": constants.RESPONSE_TYPES['MESSAGE_WITH_SOURCE'],
                "data": {
                    "content": "既に募集を締め切っています"
                }
            }

        rename_channel.execute(channel_id=channel_id, new_channel_name='〆{}'.format(target_channel_name))

        user_name = member.get('user').get('username')
        return {
            "type": constants.RESPONSE_TYPES['MESSAGE_WITH_SOURCE'],
            "data": {
                "content": "{}が募集を締め切りました".format(user_name)
            }
        }
