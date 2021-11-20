import os

# dummy response
PING_PONG = {"type": 1}

# response types
RESPONSE_TYPES =  { 
                    "PONG": 1, 
                    "ACK_NO_SOURCE": 2, 
                    "MESSAGE_NO_SOURCE": 3, 
                    "MESSAGE_WITH_SOURCE": 4, 
                    "ACK_WITH_SOURCE": 5
                  }

# discord end point
DISCORD_ENDPOINT = "https://discord.com/api/v9"

# discord public key
PUBLIC_KEY = os.getenv('DISCORD_PUBLIC_KEY')

# discord bot token
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')    

# discord application id
APPLICATION_ID = os.getenv('APPLICATION_ID')

# discord guild id
COMMAND_GUILD_ID = os.getenv('COMMAND_GUILD_ID')
