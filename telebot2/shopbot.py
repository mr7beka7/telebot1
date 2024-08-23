import telebot #pip install telebot
from time import sleep 

# TOKEN = '7388810468:AAGvy3bGVYlpTTaUzTE9dK62ZjnvaVZ7op8'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет я бот.Чем вам могу помочь')

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Я хочу купить обувь ? ':
        bot.send_message(message.from_user.id, 'У нас есть качественные Li-Ning-ги.')
    elif message.text == 'Я хотел купить другие бренды':
        sleep(2)
        bot.send_message(message.from_user.id, 'Этот купишь и все !!!')
    elif message.text == 'а какие есть':
        sleep(2)
        bot.send_message(message.from_user.id, '')
    elif message.text == 'еще':
        sleep(2)
        bot.send_message(message.from_user.id, ').jpeg') 
    elif message.text == 'а еше':
        sleep(2)
        bot.send_message(message.from_user.id, 'jpeg') 
    elif message.text == 'И сколько будет последний?':
        sleep(2)
        bot.send_message(message.from_user.id, '3000 сом')
    elif message.text == 'Пока':
        sleep(2)
        bot.send_message(message.from_user.id, 'Покупай!')
    else: 
        bot.send_message(message.from_user.id, 'О чем ты?')

bot.infinity_polling()