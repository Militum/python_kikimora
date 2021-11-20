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
    print('registering commands: {}'.format(endpoint))

    # todo: 関数化
    commands = [
        {
            "name": "help",
            "description": "コマンド一覧を表示する",
            "options": [
            ]
        }
    ]
    for c in commands:
        response = requests.post(url=endpoint, headers=headers, json=c)
        response.raise_for_status()

    return constants.PING_PONG
