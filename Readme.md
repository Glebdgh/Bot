Gleb, [12.02.21 23:56]
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
import telebot

owm = OWM('c87891ae5cab91c103c2d295135e25a0')
owm.supported_languages
mgr = owm.weather_manager()
bot = telebot.TeleBot("1661746602:AAHVuG46hW7zqevDbw22ld9MRgt3AyPNZI0")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    hum = w.humidity
    speed = w.wind()["speed"]
    deg = w.wind()["deg"]
    clouds = w.clouds

    answer = "В стране/городе "+ message.text + " сейчас " + w.detailed_status + "!" +"\n"
    if w.detailed_status == "пасмурно":
      answer += ("Ну,ты это,не сердчай!") + "\n"
    else:
      answer += ("")
    answer += "Температура здесь " + str(temp) + " C." "\n\n"
    answer += "Влажность здесь " + str(hum) + "%." + "\n\n"
    answer += "Скорость ветра " + str(speed) + " м/с." + "\n\n"
    answer += " " + str(deg) + "\n\n"
    answer += " " + str(clouds) + "" + "\n\n"


    if temp < 10:
      answer += "Жесть холодрыга на улице,так шо одевайся!"
    elif temp < 20:
      answer += "Потеплее конечно,но ты одевайся там!"
    else:
      answer += "Можешь идти загорать,погода персик "
 
    bot.send_message(message.chat.id,answer)

bot.polling (none_stop = True)