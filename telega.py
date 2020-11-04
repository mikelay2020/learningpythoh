# -*- coding: utf-8 -*-
# Подключаем модуль случайных чисел 
import random

 
# Подключаем модуль для Телеграма

import telebot

# Указываем токен

bot = telebot.TeleBot('1285449136:AAGG_6z7yYlh5TSLRBJnmk7i6fSTu1nOnyc')

 
# Импортируем типы из модуля, чтобы создавать кнопки

from telebot import types

# Метод, который получает сообщения и обрабатывает их

@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    # Если написали «тест»

    if message.text == "test" or message.text == "Test" or message.text == "Тест" or message.text == "тест" :

        # Пишем приветствие

        bot.send_message(message.from_user.id, "Привет, Зануда.")

        # Готовим кнопки

        keyboard = types.InlineKeyboardMarkup()

        # По очереди готовим текст и обработчик 

        key_linux = types.InlineKeyboardButton(text='linux', callback_data='knopka1')
        # И добавляем кнопку на экран

        keyboard.add(key_linux)

        key_mysql = types.InlineKeyboardButton(text='MySQL', callback_data='knopka2')

        keyboard.add(key_mysql)

        key_git = types.InlineKeyboardButton(text='GitHub', callback_data='knopka3')

        keyboard.add(key_git)



        # Показываем все кнопки сразу и пишем сообщение о выборе

        bot.send_message(message.from_user.id, text='Выбери тест', reply_markup=keyboard)

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "напиши тест")

    else:

        bot.send_message(message.from_user.id, "Мая - твоя не понимать. Напиши 'тест'")

 
# Обработчик нажатий на кнопки

@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call):

    # Если нажали на одну из 3 кнопок — выводим Test

	if call.data == "knopka1":
		msg = "Linux рулит"
		bot.send_message(call.message.chat.id, msg)

	if call.data == "knopka2":
		msg = "мускуль рулит"
		bot.send_message(call.message.chat.id, msg)
	
	if call.data == "knopka3":
		msg = "Git рулит"
		bot.send_message(call.message.chat.id, msg)
 








# Запускаем постоянный опрос бота в Телеграме

bot.polling(none_stop=True, interval=0)
