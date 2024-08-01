import json
import os

import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from telebot.types import Message
from Dodo import BOT_ID

telbot = telebot.TeleBot(BOT_ID)

info = {}
info2 = {}


@telbot.message_handler(commands=["watch"])
def pokas(message: Message):
    with open(f"{message.from_user.id}.json", "r", encoding="UTF-8") as p:
        fal = json.load(p)
        if len(fal)==0:
            telbot.send_message(message.from_user.id, "Бро тебе надо тренироватся")
            return False


    result = ""
    for schet, x in enumerate(fal, start=1):
        result += f"{x['task']} {x['legality']} {schet}  \n"

    telbot.send_message(message.from_user.id, f"{result}")
    return  True


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
    info[message.from_user.id] = {"task": "", "legality": ""}
    print(info)
    telbot.send_message(message.from_user.id, "Что хотите сделать?")
    telbot.register_next_step_handler(message, otvetka)


def otvetka(message):
    info[message.from_user.id]["task"] = message.text
    print(info)

    telbot.send_message(message.from_user.id, "Это легально?")
    telbot.register_next_step_handler(message, otvetka2)


def otvetka2(message):
    telbot.send_message(message.from_user.id, "Я спать")
    info[message.from_user.id]["legality"] = message.text
    print(info)
    if os.path.exists(f"{message.from_user.id}.json"):
        with open(f"{message.from_user.id}.json", "r", encoding="UTF-8") as p:
            fal = json.load(p)
            fal.append(info[message.from_user.id])
        with open(f"{message.from_user.id}.json", "w+", encoding="UTF-8") as f:
            json.dump(fal, f, ensure_ascii=False)
    else:

        with open(f"{message.from_user.id}.json", "a+", encoding="UTF-8") as f:
            json.dump([info[message.from_user.id]], f, ensure_ascii=False)


@telbot.message_handler(commands=["del"])
def delete(message):
    proverka = pokas(message)
    if proverka:

        telbot.send_message(message.from_user.id, "Какое задание хотите удалить?")
        telbot.register_next_step_handler(message, delete2)


def delete2(message):
    telbot.send_message(message.from_user.id, "ок")
    if os.path.exists(f"{message.from_user.id}.json"):
        with open(f"{message.from_user.id}.json", "r+", encoding="UTF-8") as f:
            spisok = json.load(f)


            try:
                spisok.pop(int(message.text)-1)
            except IndexError:
                telbot.send_message(message.from_user.id, "Такого нет?")
                return

        with open(f"{message.from_user.id}.json", "w+", encoding="UTF-8") as f:
            json.dump(spisok,f,ensure_ascii=False)
    else:
        with open(f"{message.from_user.id}.json", "a+", encoding="UTF-8") as f:
            json.dump([info2[message.from_user.id]], f, ensure_ascii=False)
            info2.pop()


telbot.polling()

"""
Узнать что такое SQLite  в пайтоне
найти и скопировать код, который создаёт базу данных при помощи пайтона

Запросы:
- "что такое SQLite"
- "как создать таблицу SQLite в пайтоне"
найти видосик на ютубе с обучением "SQLite обучение на пайтоне", посмотреть хотя бы 10 мин. это оч поможет на занаятии 

"""
