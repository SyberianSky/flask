#! /usr/bin/env python
# -*- coding: utf-8 -*-

import config
import telebot
import hello
import random
import re


bot = telebot.TeleBot(config.token)

#@bot.message_handler(content_types=["text"])
buzz = ('Максим гей', 'Лютик, блять', 'Никак вы блять не научитесь', 'Ламберт, Ламберт - хер моржовый. Ламберт, Ламберт - вредный хуй',
'Холера', 'Зараза', 'Ну и ветер', 'Разойдись свинопасы или Господин Ведьмак, вам таких пиздюлей отвесит, вовек не забудете! Где тут дрын, какой-нибудь?!',
'А чем тебе болота не нравятся? Я тут всю жизнь живу и всем советую', 'Когда в битве он потерял обе ноги, он сказал, что так даже лучше - больше не будут болеть',
'Геральт, ты... Как бы это помягче сказать... Пиздишь',
'Сам ты, сука, Питер Динклейдж',
'Ты и тут бывал, и там. Вот ты мне скажи, у них там в Новиграде правда такая мода, что б манду брить?')



adjectives = ('','')
adverbs = ('','')
verbs = ('','')


def sample(l, n = 1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result

def generate_p():
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([sample(adjectives), buzz_terms[0], sample (adverbs),
        sample(verbs)])
    return phrase.title()

#if __name__ == "__main__":
#    print(generate_p())

@bot.send_message(message.chat.id, 'sdsdsd, {}'print(generate_p) )
    
   

if  __name__  ==  '__main__':
     bot.infinity_polling()
