#! /usr/bin/env python
# -*- coding: utf-8 -*-

import config
import telebot
from engine import get_random_quote
#from engine import get_random_quote

bot = telebot.TeleBot(config.token)
#token = "1591933405:AAF1qRG8Oa-812x-91Pcrgh_QLI63dg--6k"


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    names = ['Лютик', 'лютик', 'Гервант', 'Геральт', 'геральт', 'гервант', 'мастер', ' Мастер', 'ведьмак', 'Ведьмак', 'приблуда', 'Приблуда', 'ветер', 'Ветер', 'холодно', 'Холодно' ]
    for name in names:
        if name in message.text.lower():
                    bot.send_message(message.chat.id, text=get_random_quote()) 
#@bot.message_handler(content_types=["text"])
#def repeat_all_messages2(message):
    names1 = ['Гвинт', 'гвинт', 'карты', 'картишки', 'Карты', 'Картишки', 'ХВЭНДЭ', 'хвэндэ', 'Хвэндэ', 'Гвинтец', 'гвинтец', 'Партия', 'Партию', 'партия', 'партию', 'партейку', 'Партейку', 'Партейка', 'партейка']
    for name in names1:
        if name in message.text.lower():
                    bot.send_message(message.chat.id, 'Кто то тут сказал ГВИНТ?')
#    names2 = ['два', 'Два', '2']
#    for name in names2:
#        if name in message.text.lower():
#                    bot.send_message(message.chat.id, 'Хера')
    names3 = ['Холера', 'холера']
    for name in names3:
        if name in message.text.lower():
                    bot.send_message(message.chat.id, 'Зараза')
    names4 = ['Зараза', 'зараза']
    for name in names4:
        if name in message.text.lower():
                    bot.send_message(message.chat.id, 'Холера')
#    names5 = ['Да', 'да']
#    for name in names5:
#        if name in message.text.lower():
#                    bot.send_message(message.chat.id, 'Пизда')

    if message.text.lower() == 'два':
        bot.send_message(message.chat.id, 'хера')
    if message.text.lower() == 'Два':
        bot.send_message(message.chat.id, 'хера')
    if message.text.lower() == '2':
        bot.send_message(message.chat.id, 'хера') 
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Пизда')
    if message.text.lower() == 'Да':
        bot.send_message(message.chat.id, 'Пизда')
        
        #ef main():
#       updater = Updater(token);
#       dp = updater.dispatcher

        # Define all the commands that the bot will receive
        #dp.add_handler(CommandHandler("start", start))
#       dp.add_handler(CommandHandler("quote", quote))
        # Start the bot
        #updater.start_polling()
       # print("================================")
       # print("========= Bot Running ==========")
       # print("================================")

       # updater.idle()


bot.polling()

