from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot = ChatBot('Charlie')
#bot = ChatBot(
#    'Charlie',
 #   storage_adapter='chatterbot.storage.SQLStorageAdapter',
  #  database_uri='sqlite:///database.sqlite3'
   # )
    
trainer = ListTrainer(bot)
trainer.train([
    'Olá?',
    'Olá, tudo bem?',
    'Vou bem, e você?',
])

while True:
    request = input('Usuário: ')
    response = bot.get_response(request)
    print('Bot: ', response)