import requests, log, os, json, time

current_dir = os.path.dirname(__file__)
current_file = os.path.basename(__file__)

def telegram_bot_sendtext(bot_token, bot_message, chat_ids):
    """
    Use bot for send enssage to specific chat
    """

    # Updates: https://api.telegram.org/bot1853683882:AAH_4aToI5HY8DNwC4M0nCQmyuTnKmKjoLc/getUpdates
    responses = []

    for chat_id in chat_ids:
        bot_chatID = chat_id
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        
        log.info (f'Sendgin menssage to: {chat_id}', current_file)

        response_json = requests.get(send_text).text
        response_formated = json.loads(response_json)
        responses.append(response_formated)
    
    log.info(f'Telegram responses: {str(responses)}', current_file)
