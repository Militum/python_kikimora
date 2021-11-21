import constants
import requests

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
    command = {
        "name": "initialize_kikimora",
        "description": "kikimoraの初期化を行います",
        "options": [
            {
                "type": constants.COMMAND_OPTION_TYPES["ROLE"],
                "name": "administrator_role",
                "description": "kikimoraのバージョン管理を行う管理者ロールを設定してください",
                "required": True
            },
        ]
    }

    response = requests.post(url=endpoint, headers=headers, json=command)
    response.raise_for_status()
