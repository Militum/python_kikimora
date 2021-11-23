import constants
import headers

import requests

def execute(channel_id: int, new_channel_name: str)-> dict:
    endpoint='{}/channels/{}'.format(
        constants.DISCORD_ENDPOINT,
        channel_id
    )
    payload = {
        "name": new_channel_name,
    }

    # channel リネーム
    response = requests.patch(url=endpoint, headers=headers.HEADERS, json=payload)
    response.raise_for_status()

    return response.json()
