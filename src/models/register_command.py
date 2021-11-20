import constants
import requests

def initial_command()->dict:
    return [
        {
            "name": "recruit",
            "description": "募集チャンネルを作成します",
            "options": [
                {
                    "type": constants.COMMAND_OPTION_TYPES["STRING"],
                    "name": "channel_name",
                    "description": "チャンネル名",
                    "required": True             
                },
            ]
        },
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
            ]
        },
        {
            "name": "campaign",
            "description": "キャンペーン用のセッションルームを作成します",
            "options": [
                {
                    "type": constants.COMMAND_OPTION_TYPES["STRING"],
                    "name": "channel_name",
                    "description": "チャンネル名",
                    "required": True             
                },
            ]
        },
        {
            "name": "rename",
            "description": "チャンネル名の変更を行います",
            "options": [
                {
                    "type": constants.COMMAND_OPTION_TYPES["STRING"],
                    "name": "channel_name",
                    "description": "変更後のチャンネル名",
                    "required": True             
                },
            ]
        },
        {
            "name": "close",
            "description": "セッションの募集を締め切ります",
            "options": [
            ]
        },
        {
            "name": "delete",
            "description": "セッションルームを削除します",
            "options": [
            ]
        },
        {
            "name": "help",
            "description": "kikimoraで出来ることを表示します",
            "options": [
            ]
        }
    ]

def execute():
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

    commands = initial_command()
    for c in commands:
        response = requests.post(url=endpoint, headers=headers, json=c)
        response.raise_for_status()

    return constants.PING_PONG
