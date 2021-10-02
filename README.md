<div align = "center">
<img src = "https://res.cloudinary.com/practicaldev/image/fetch/s--T__NDHd5--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/w0shqntyjc5vyfuyn5bg.png"  width="500" height="240" > 
<h2 >
 <a href = https://hacktoberfest.digitalocean.com > Hacktoberfest-2021 </a> contribution Repo for Beginners 
</h2>
</br>
</div>
<h2> TelegramChatbotAIML </h2> <br>
A simple telegram chatbot working on AIML and deployed @IcHiGo_bot

## What is a Chatbot?
Chatbots are intelligent digital assistants which may address customer’s basic and predictable queries. 
They offer numerous services via chatting and perform basic customer service operations. 
Chatbots work 24/7 and hence they provide assistance when offices are closed on holidays.
There are a variety of synonyms for chatbot, including “talkbot,” “bot,” “IM bot,” “interactive agent” or “artificial conversation entity”.

## What is  AIML?
AIML stands for computing language. it’s an XML dialect for creating tongue software agents. 

AIML contains a collection of rules which define the conversational capabilities of the chatbot. it’s used with a linguistic communication Understanding (NLU) processor which takes AIML rules to investigate and reply to the text queries asked via the chatbot. The more rules we add in AIML – the more intelligent the chatbot is.

- AIML based chatbots come under the rule-based chatbots category, however, some level of self-learning feature is feasible.
- AIML is that the language to make a brain for chatbots.
- NLU in chatbots process AIML and their chat behavior is controlled through AIML rules.
- One chatbot application can have multiple sets of AIML and might behave differently.
- The below flow diagram shows how AIML based chatbot can work with a range of input, which essentially represents the texts with identical meaning.

## How to contribute :
- Create a new aiml file in ```AddedFeatures``` folder 
- Deleting the brain.dump file so that it doesnt take into account the pretrained model and use your created aiml file as well.
- Run ```server.py``` in terminal to retrain the model.
- You can't really deploy it on your own , if you wish to then just add a ```config.cfg``` to the root directory and with the following parameters.
```
[creds]
token= YOUR_BOT_TOKEN
file=brain.dump
```
After all this you'll be good to go.
