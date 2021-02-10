from bot import telegram_chatbot

bot = telegram_chatbot("config.cfg")


def make_reply(msg):
    reply = bot.getResponseFromBot(msg)
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    try:
        updates = updates["result"]
    except KeyError:
        print(KeyError)
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
