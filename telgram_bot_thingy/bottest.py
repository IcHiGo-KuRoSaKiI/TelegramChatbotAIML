import aiml
# from bot import telegram_chatbot
# bot = telegram_chatbot("config.cfg")
#
# def make_reply(msg):
#     reply = bot.getResponseFromBot(msg)
#     return reply
import os
# Ye basic test hai to test that aiml works


# class chatbot():
#
#     def __init__(self):
#         self.k = aiml.Kernel()
#         self.k.learn("std-startup.xml")
#         x = self.k.respond("LOAD AIML B")
#         print("self " ,self.k.respond("Hello"))

# bot=chatbot()
k = aiml.Kernel()
k.learn("std-startup.xml")
k.respond("LOAD AIML B")
x= k.respond("Hello")
print("x =",x)
while True:
    print (k.respond(input(('WHAT ARE YOU'))))
