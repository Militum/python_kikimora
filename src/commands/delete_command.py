
import constants
from commands import CommandBase
from discord import delete_channel, get_channel

class DeleteCommand(CommandBase):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, member: dict, options: dict) -> None:
        super().validate(member, options)

    def execute(self, member: dict, options: dict, channel_id: str)->dict:
        # コマンドを実行したチャンネルは必ずある
        text_channel = get_channel.get_channel_by_id(channel_id)

        # テキストチャンネルと同じ名前のVCチャンネルを取得して連動して削除する
        target_channel_name = text_channel.get('name')
        voice_channels = get_channel.get_channels_by_name(
            target_channel_name,
            constants.GUILD_CHANNEL_TYPES["GUILD_VOICE"]
        )
        for voice_channel in voice_channels:
            delete_channel.execute(
                channel_id=voice_channel.get('id')
            )

        delete_channel.execute(channel_id=channel_id)

        return {
            "type": constants.RESPONSE_TYPES['MESSAGE_NO_SOURCE'],
            "data": {
                "tts": False,
                "content": 'Delete Channel.',
                "embeds": [],
                "allowed_mentions": []
            }
        }
