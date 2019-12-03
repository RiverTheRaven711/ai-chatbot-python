# import modules to project
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

# define functions
bot = ChatBot('Bot')
trainer = ListTrainer(bot)

# setting up chatbot
for files in os.listdir('data/english/'):
    files_path = os.path.join('data/english/', files)
    data = open('data/english/' + files, 'r').readlines()
    trainer.train(data)

while True:
    message = input('You:')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print('ChatBot :', reply)
    if message.strip() == 'Bye':
        print('ChatBot : Bye')
        break
