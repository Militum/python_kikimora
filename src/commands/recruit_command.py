
import constants
from commands import CommandBase
from discord import create_channnel
class RecruitCommand(CommandBase):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, member: dict, options: dict) -> None:
        if 'user' not in member:
            raise Exception('パラメータ不足')

        if 'username' not in member.get('user'):
            raise Exception('パラメータ不足')

        if 'channel_name' not in options:
            raise Exception('パラメータ不足')

        super().validate(member, options)

    def execute(self, member: dict, options: dict, channel_id: str)->dict:
        channel_name = options.get('channel_name')
        response = create_channnel.execute(
            channel_name,
            constants.RECRUIT_CATEGORY_ID,
            constants.GUILD_CHANNEL_TYPES["GUILD_TEXT"]
        )

        user_name = member.get('user').get('username')
        return {
            "type": constants.RESPONSE_TYPES['MESSAGE_WITH_SOURCE'],
            "data": {
                "content": "{}が<#{}>で募集を開始しました".format(user_name, response.get('id'))
            }
        }
