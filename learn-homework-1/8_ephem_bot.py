"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import settings
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def planet_list(update, context):

    planets = ('Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')

    message = update.message.text.split()
    planet = message[1].lower().capitalize()
    if planet in planets:
        date = datetime.datetime.now()
        planet_info = getattr(ephem, planet)(date)
        stars = ephem.constellation(planet_info)
        update.message.reply_text(stars[1])


def planet_help(update, context):
    if context != "":
       help= "Введите /planet ИмяПланеты,список планет: 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'"
       print(help)
    update.message.reply_text(help)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_list))
    dp.add_handler(CommandHandler("planet", planet_help))


    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
