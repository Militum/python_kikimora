
import constants
from commands import CommandBase
from discord import rename_channel
from discord import get_channel

class RenameCommand(CommandBase):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, member: dict, options: dict) -> None:
        if 'channel_name' not in options:
            raise Exception('パラメータ不足')

        super().validate(member, options)

    def execute(self, member: dict, options: dict, channel_id: str)->dict:

        new_channel_name = options.get('channel_name')

        # コマンドを実行したチャンネルは必ずある
        text_channel = get_channel.get_channel_by_id(channel_id)

        # テキストチャンネルと同じ名前のVCチャンネルを取得する(同名は複数hitしてしまう)
        target_channel_name = text_channel.get('name')
        voice_channels = get_channel.get_channels_by_name(
            target_channel_name,
            constants.GUILD_CHANNEL_TYPES["GUILD_VOICE"]
        )
        for voice_channel in voice_channels:
            rename_channel.execute(
                channel_id=voice_channel.get('id'),
                new_channel_name=new_channel_name
            )

        # todo: 荒らし防止のためチャンネル作成者のみ変更可能な仕様にする
        response = rename_channel.execute(channel_id=channel_id, new_channel_name=new_channel_name)

        user_name = member.get('user').get('username')
        return {
            "type": constants.RESPONSE_TYPES['MESSAGE_WITH_SOURCE'],
            "data": {
                "content": "{}がチャンネルの名前を<#{}>に変更しました".format(user_name, response.get('id'))
            }
        }
