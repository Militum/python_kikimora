import constants
import headers

import requests

# チャンネルIDからチャンネルを取得
def get_channel_by_id(channel_id: int)-> dict:
    endpoint='{}/channels/{}'.format(
        constants.DISCORD_ENDPOINT,
        channel_id
    )

    # channel 取得
    response = requests.get(url=endpoint, headers=headers.HEADERS)
    response.raise_for_status()

    return response.json()

# チャンネル名からチャンネルを取得
# 冗長なので可能な限りIDから取得すること
def get_channels_by_name(channel_name: str, channel_type: int)-> list:
    endpoint='{}/guilds/{}/channels'.format(
        constants.DISCORD_ENDPOINT,
        constants.COMMAND_GUILD_ID
    )

    # channel list 取得
    response = requests.get(url=endpoint, headers=headers.HEADERS)
    response.raise_for_status()

    channels = filter(
        lambda item: item['type'] == channel_type and item['name'] == channel_name,
        response.json()
    )

    return list(channels)
