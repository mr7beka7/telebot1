# import telebot #pip install telebot
# from time import sleep 

# TOKEN = '7240432620:AAE-MkV2v287w7tGvSaNJN5DVhtnxHFBxjw'

# bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет я бот.Чем вам могу помочь')

# @bot.message_handler(content_types=['text'])
# def text(message):
#    if message.text == 'Привет':
#         bot.send_message(message.from_user.id, 'Привет')
#     elif message.text == 'Как дела?':
#         sleep(2)
#         bot.send_message(message.from_user.id, 'Нормально')
#     elif message.text == 'Что делаешь?':
#         sleep(2)
#         bot.send_message(message.from_user.id, 'На данный момент с тобой разговариваю')
#     elif message.text == 'Ты на основе ИИ ?':
#         sleep(2)
#         bot.send_message(message.from_user.id, 'Нет, но скоро!') 
#     elif message.text == 'Что ты умеешь ?':
#         sleep(2)
#         bot.send_message(message.from_user.id, 'Умею добавлять 2 к 2 ') 
#     elif message.text == 'И сколько будет ?':
#         sleep(2)
#         bot.send_message(message.from_user.id, 'Посчитай сам')
#     elif message.text == 'Пока':
#         sleep(2)
#         bot.send_message(message.from_user.id, 'Если будут вопросы обращайся !')
#     else: 
#         bot.send_message(message.from_user.id, 'О чем ты?')

# bot.infinity_polling()