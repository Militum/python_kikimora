import constants
import headers

import requests

def execute(channel_id: str)-> dict:
    endpoint='{}/channels/{}'.format(
        constants.DISCORD_ENDPOINT,
        channel_id
    )

    # channel 削除
    response = requests.delete(url=endpoint, headers=headers.HEADERS)
    response.raise_for_status()

    return response.json()
