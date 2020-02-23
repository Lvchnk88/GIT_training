import pyowm
from colorama import init
from colorama import Fore
owm = pyowm.OWM('9cb0e81b8359598265f73dc892635802',language = "ru")  # You MUST provide a valid API key
place = input(Fore.YELLOW + 'Введи свой страну или город: ')

observation = owm.weather_at_place(place)
w = observation.get_weather()
temp = w.get_temperature('celsius')
speed = w.get_wind()

print("В городе '" + place + "' сейчас " + w.get_detailed_status() + ".")
print("Температура воздуха- " + str(temp["temp"]) + " °C")
print("Максимальная температура воздуха- " + str(temp["temp_max"]) + " °C")
print("Миниимальная температура воздуха- " + str(temp["temp_min"]) + " °C")
print("Скорость ветра- " + str(speed["speed"]) + " м/с")
print("Влажность- " + str(w.get_humidity()) + " мм/рс")
print()
print("РЕКОМЕНДАЦИИ НА ДЕНЬ.")
if temp["temp"] <= 10:
    print(Fore.BLUE + "За окном пиздец, береги себя и одевайся теплее!!!")
elif (temp["temp"] > 10) and (temp["temp"] < 20):
    print(Fore.WHITE + "Погодка заебок не парься.")
else:
    print(Fore.RED + "За бортом апокалипсис СИДИ ДОМА под кондером!!!")

input()