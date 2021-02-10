import requests
import json
import configparser as cfg
import aiml
import os
class telegram_chatbot():

    def __init__(self,config):
        self.token = self.read_token_from_config_file(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)
        BRAIN_FILE = self.read_file_from_config_file(config)
        self.k = aiml.Kernel()
        if os.path.exists(self.read_file_from_config_file(config)):
            print("Loading from brain file: " + BRAIN_FILE)
            self.k.loadBrain(BRAIN_FILE)
        else:
            print("Parsing aiml files")#
            self.k.bootstrap(learnFiles="startup.xml", commands="LOAD AIML B")
            print("Saving brain file: " + BRAIN_FILE)
            self.k.saveBrain(BRAIN_FILE)

    def getResponseFromBot(self, message):
        global response
        response = self.k.respond(message)

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(url)

    def read_token_from_config_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')

    def read_file_from_config_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'file')