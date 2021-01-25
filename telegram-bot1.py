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

