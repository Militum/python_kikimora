import bootstrap

from nacl.signing import VerifyKey
import constants
from models import execute_command
from models import register_command

def verify_signature(event):
    raw_body = event.get("rawBody")
    auth_sig = event['params']['header'].get('x-signature-ed25519')
    auth_ts  = event['params']['header'].get('x-signature-timestamp')
    
    message = auth_ts.encode() + raw_body.encode()
    verify_key = VerifyKey(bytes.fromhex(constants.PUBLIC_KEY))
    verify_key.verify(message, bytes.fromhex(auth_sig)) # raises an error if unequal

def ping_pong(body):
    if body.get("type") == 1:
        return True
    return False

def is_application_command(body):
    if body.get("type") == 2:
        return True
    return False

def lambda_handler(event, context):
    # verify the signature
    try:
        verify_signature(event=event)
    except Exception as e:
        print(e)
        raise Exception(f"[UNAUTHORIZED] Invalid request signature: {e}")

    # check if message is a ping
    body = event.get('body-json')
    try:
        if ping_pong(body):
            return register_command.execute()
        elif is_application_command(body):
            return execute_command.execute(options=body['data'])
    except Exception as e:
        print(e)
        raise Exception(f"[UNAUTHORIZED] commands execution filed: {e}")

    # dummy return
    return {
            "type": constants.RESPONSE_TYPES['MESSAGE_NO_SOURCE'],
            "data": {
                "tts": False,
                "content": "BEEP BOOP",
                "embeds": [],
                "allowed_mentions": []
            }
        }
