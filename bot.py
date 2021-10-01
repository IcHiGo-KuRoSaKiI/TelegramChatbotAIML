import requests
import json
import configparser as cfg
import aiml
import os
import logging
logging.basicConfig(filename='info.log',level=logging.INFO)
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
            print("Parsing aiml files")
            self.k.bootstrap(learnFiles="startup.xml", commands="LOAD AIML B")
            print("Saving brain file: " + BRAIN_FILE)
            self.k.saveBrain(BRAIN_FILE)
        #only for testing purposes (or in life or death situations)
        #self.k = aiml.Kernel()
        #self.k.learn("startup.xml")
        # self.k.learn("std-startup.xml")
        #self.k.respond("LOAD AIML B")

    def getUserName(self,Fname, Lname):
        print("Username", Fname, Lname)
        logging.info("Username : "+Fname +" " +Lname)

        
#dikat hai yha - no match found for the input arg main hard code bhi kr du tb bhi ni
    def getResponseFromBot(self, lala):
        try:
            logging.info("User message: " + lala)
            print("User Input =", lala)
            response = str(self.k.respond(lala))
        except TypeError:
            logging.info("type error ")	
            response = "null response"	

        try:
            logging.info("IchiBot's response: " + response)
        except TypeError:
            print("no response due to type error")
        # print("the hard response", self.k.respond('Hello'))
        if response:
            return response
        else:
            x="Can you please rephrase that?"
            return x
    

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        print(chat_id,msg)
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
