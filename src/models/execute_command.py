def execute(options:dict)->dict:
    return {
        "type": 4, # InteractionResponseType.ChannelMessageWithSource
        "data": {
            "content": 'sample text'
        }
    }
