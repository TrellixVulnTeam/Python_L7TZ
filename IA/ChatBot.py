from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('DSV')
convI = ['oi','ola','ola, bom dia','bom dia','Bom dia, como vai ?','Estou bem']
convT = ['vamos trabalhar','sim, esta na hora', 'entao vamos','ok']

bot.set_trainer(ListTrainer)
bot.train(convI)
bot.train(convT)

while True :
    quest = raw_input ('Voce : ')
    response = bot.get_response(quest)
    if float(response.confidence)> 0.5:
        print ('Bot : ' , response)
    else:
        print ('Bot : nao entendi')