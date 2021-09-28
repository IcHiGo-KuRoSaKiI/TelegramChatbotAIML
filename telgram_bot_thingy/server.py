from bot import telegram_chatbot

bot = telegram_chatbot("config.cfg")


def make_reply(msg):
    reply = bot.getResponseFromBot(msg)
    if (reply == None):
        return "this is it"
    else:
        return reply



def userName(name1, name2 = ""):
    n1 = bot.getUserName(name1, name2)
    return n1


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
                from_ = item["message"]["from"]["id"]
                UsrFirstName = item["message"]["from"]["first_name"]
                UsrLastName = item["message"]["from"]["last_name"]
                reply = make_reply(message)
                if ( UsrLastName):
                    userName(UsrFirstName, UsrLastName)
                else :
                    print("Last name not found!!")
                    userName(UsrFirstName)
                reply = make_reply(message)
                bot.send_message(reply, from_)
            except:
                message = None
                print ( "Failed ")

if __name__ == '__main__':
    main()
