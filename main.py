import json
import os

import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from telebot.types import Message
from Dodo import BOT_ID

telbot = telebot.TeleBot(BOT_ID)

info = {}
info2 = {}


@telbot.message_handler(commands=["start"])
def soobsh(message: Message):
    print(message)

    print(info)
    knopki = ReplyKeyboardMarkup(resize_keyboard=True)
    knopk = KeyboardButton(text="ka", request_location=True)
    knopki.add(knopk)
    # telbot.send_message(message.from_user.id,"вас выследили",reply_markup=knopki)
    telbot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEMM81mU1B_M45YswKX4Lt-5PM9uaktQAACAQADwDZPExguczCrPy1RNQQ")


@telbot.message_handler(commands=["add"])
def soobs(message: Message):
    info[message.from_user.id] = {"task":"","legality":""}
    print(info)
    telbot.send_message(message.from_user.id, "Что хотите сделать?")
    telbot.register_next_step_handler(message, otvetka)


def otvetka(message):
    info[message.from_user.id]["task"]=message.text
    print(info)

    telbot.send_message(message.from_user.id, "Это легально?")
    telbot.register_next_step_handler(message, otvetka2)


def otvetka2(message):
    telbot.send_message(message.from_user.id, "Я спать")
    info[message.from_user.id]["legality"] = message.text
    print(info)
    if os.path.exists(f"{message.from_user.id}.json"):
        pass
    else:


        with open (f"{message.from_user.id}.json","a+",encoding="UTF-8") as f:
                json.dump([info[message.from_user.id]],f,ensure_ascii=False)



telbot.polling()

"""
Узнать что такое срезы в пайтоне (старт, стоп, степ)

И как отобразить все буквы через одну в этой переменной:
x = "Tima, privet. Eto test stro4ka. Попробуй с помощью срезов достать только каждый второй символ"

"""
