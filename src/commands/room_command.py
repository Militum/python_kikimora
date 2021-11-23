
import constants
from commands import CommandBase
from discord import create_channnel

class RoomCommand(CommandBase):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, member: dict, options: dict) -> None:
        if 'user' not in member:
            raise Exception('パラメータ不足')

        if 'username' not in member.get('user'):
            raise Exception('パラメータ不足')

        if 'channel_name' not in options:
            raise Exception('パラメータ不足')

        if 'is_oneoff' not in options:
            raise Exception('パラメータ不足')

        super().validate(member, options)

    def execute(self, member: dict, options: dict, channel_id: str)->dict:
        channel_name = options.get('channel_name')
        is_oneoff_session = options.get('is_oneoff')
        is_voice_session = options.get('is_voice_session', True)

        # 入力値を元にチャンネルを作成
        response = create_channnel.execute(
            channel_name,
            constants.SESSION_TEXT_CATEGORY_ID if is_oneoff_session == False else constants.CAMPAIGN_TEXT_CATEGORY_ID,
            constants.GUILD_CHANNEL_TYPES["GUILD_TEXT"]
        )

        # テキストセッションであればVCチャンネルはいらないので最初から作らない
        if is_voice_session == True:
            create_channnel.execute(
                channel_name,
                constants.SESSION_VC_CATEGORY_ID if is_oneoff_session == False else constants.CAMPAIGN_VC_CATEGORY_ID,
                constants.GUILD_CHANNEL_TYPES["GUILD_VOICE"]
            )

        user_name = member.get('user').get('username')
        return {
            "type": constants.RESPONSE_TYPES['MESSAGE_WITH_SOURCE'],
            "data": {
                "content": "{}が<#{}>のセッションルームを作りました。良い卓を！".format(user_name, response.get('id'))
            }
        }
