import constants
import headers

import requests

def execute(channel_name: str, category_id: int, channel_type: int)-> dict:
    endpoint='{}/guilds/{}/channels'.format(
        constants.DISCORD_ENDPOINT,
        constants.COMMAND_GUILD_ID
    )
    payload = {
        "name": channel_name,
        "type": channel_type,
        "parent_id": category_id
    }

    # channel 作成
    response = requests.post(url=endpoint, headers=headers.HEADERS, json=payload)
    response.raise_for_status()

    return response.json()
