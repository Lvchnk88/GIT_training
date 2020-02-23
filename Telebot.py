import telebot
import pyowm

bot = telebot.TeleBot("850920576:AAEE8WVXnCnSsD3tU74HCJp7gJfynbuZdpw")
owm = pyowm.OWM('9cb0e81b8359598265f73dc892635802', language = "ru")


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Давай вводи свою страну или город: (ENG) 😒")

@bot.message_handler(commands=['info'])
def send_welcome(message):
	bot.send_message(message.chat.id, "-Пишем на ИНГЛИШЕ разборчиво😡 \n-Смотрим погоду😌 \n-Благодарим автора🤓 \n-Идем нахуй😆 ")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place( message.text )
    w = observation.get_weather()
    temp = w.get_temperature('celsius')

    #if observation == False:
        #restart_program()


    answer = "В  '" + message.text + "' сейчас " + w.get_detailed_status() + "." "\n"
    answer += "Температура воздуха: " + str(temp["temp"]) + " °C" "\n\n"
    answer += "Максимальная температура воздуха: " + str(temp["temp_max"]) + " °C" "\n"
    answer += "Миниимальная температура воздуха: " + str(temp["temp_min"]) + " °C" "\n"
    #answer += "Скорость ветра: " + str(speed['speed']) + " м/с" "\n"
    answer += "Влажность: " + str(w.get_humidity()) + " мм/рс" "\n\n"
    answer += "РЕКОМЕНДАЦИИ НА ДЕНЬ.""\n"

    if temp["temp"] <= 10:
        answer += "За окном пиздец, береги себя и одевайся теплее!!! 🥶 "
    elif (temp["temp"] > 15) and (temp["temp"] < 25):
        answer += "Погодка заебок не парься 😁"
    else:
        answer += "За бортом апокалипсис СИДИ ДОМА под кондером!!! 🥵 "

    bot.send_message(message.chat.id, answer)
    if observation == False:
        restart_program()

bot.polling( none_stop = True )




