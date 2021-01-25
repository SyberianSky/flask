#! /usr/bin/env python
# -*- coding: utf-8 -*-

import config
import telebot
import hello
import random
import re


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#	bot.reply_to(message, message.text)

   

if  __name__  ==  '__main__':
     bot.infinity_polling()
