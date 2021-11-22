import constants
import requests
from commands import CommandBase

# todo 一回で6個以上のコマンドを実行しようとすると429エラーとなるので対応策を考える
class RegisterCommand(CommandBase):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, member: dict, options: dict) -> None:
        super().validate(member, options)

    def execute(self, member: dict, options: dict)->dict:

        add_commands = [
            # {
            #     "name": "recruit",
            #     "description": "募集チャンネルを作成します",
            #     "options": [
            #         {
            #             "type": constants.COMMAND_OPTION_TYPES["STRING"],
            #             "name": "channel_name",
            #             "description": "チャンネル名",
            #             "required": True             
            #         },
            #     ]
            # },
            {
                "name": "room",
                "description": "セッションルームを作成します",
                "options": [
                    {
                        "type": constants.COMMAND_OPTION_TYPES["STRING"],
                        "name": "channel_name",
                        "description": "チャンネル名",
                        "required": True             
                    },
                    {
                        "type": constants.COMMAND_OPTION_TYPES["BOOLEAN"],
                        "name": "is_oneoff",
                        "description": "ワンオフ(単発)のセッションを行うか(True=ワンオフ,False=キャンペーン)",
                        "required": True 
                    },
                    {
                        "type": constants.COMMAND_OPTION_TYPES["BOOLEAN"],
                        "name": "is_voice_session",
                        "description": "ボイスセッションを行うか",
                        "required": False    
                    },
                ]
            },
            # {
            #     "name": "rename",
            #     "description": "チャンネル名の変更を行います",
            #     "options": [
            #         {
            #             "type": constants.COMMAND_OPTION_TYPES["STRING"],
            #             "name": "channel_name",
            #             "description": "変更後のチャンネル名",
            #             "required": True             
            #         },
            #     ]
            # },
            # {
            #     "name": "close",
            #     "description": "セッションの募集を締め切ります",
            #     "options": [
            #     ]
            # },
            # {
            #     "name": "delete",
            #     "description": "セッションルームを削除します",
            #     "options": [
            #     ]
            # },
            # {
            #     "name": "help",
            #     "description": "kikimoraで出来ることを表示します",
            #     "options": [
            #     ]
            # }
        ]

        update_commands = [
        ]

        headers = {
            "User-Agent": "discord-slash-commands-helloworld",
            "Content-Type": "application/json",
            "Authorization": 'Bot {}'.format(constants.DISCORD_TOKEN) # Botを入れないとBotとして認証されない
        }
        endpoint='{}/applications/{}/guilds/{}/commands'.format(
            constants.DISCORD_ENDPOINT,
            constants.APPLICATION_ID,
            constants.COMMAND_GUILD_ID
        )
        # print('registering commands: {}'.format(endpoint))

        for c in add_commands:
            response = requests.post(url=endpoint, headers=headers, json=c)
            response.raise_for_status()

        for c in update_commands:
            response = requests.patch(url=endpoint, headers=headers, json=c)
            response.raise_for_status()

        initial_text = 'コマンド登録完了'
        return {
            "type": constants.RESPONSE_TYPES['MESSAGE_WITH_SOURCE'],
            "data": {
                "content": initial_text
            }
        }
