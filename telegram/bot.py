import os
import sys
import json
import requests
from log import Log

def telegram_bot_sendtext(bot_token, bot_message, chat_ids):
    """
    Use bot for send enssage to specific chat
    """

    # Log instance
    logs = Log(os.path.basename(__file__))

    # Updates: https://api.telegram.org/bot{bot_token}/getUpdates

    responses = []

    for chat_id in chat_ids:
        bot_chatID = chat_id
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        
        logs.info (f'Sending menssage to: {chat_id}', print_text=True)

        response_json = requests.get(send_text).text
        response_formated = json.loads(response_json)
        responses.append(response_formated)
    
    logs.info(f'Telegram responses: {str(responses)}', print_text=False)
