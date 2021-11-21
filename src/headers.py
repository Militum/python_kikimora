import constants

HEADERS = {
    "User-Agent": "discord-slash-commands-kikimora",
    "Content-Type": "application/json",
    "Authorization": 'Bot {}'.format(constants.DISCORD_TOKEN) # Botを入れないとBotとして認証されない
}
