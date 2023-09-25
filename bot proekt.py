#from constant import token
import telebot
import requests
import json

from telebot import TeleBot

bot: TeleBot = telebot.TeleBot('6432568628:AAGPmUlXPfx340cZBvY2dZ-8jPpMDUe6gR4')
API = '2fa6513c89023a60b51908c40ea118cc'

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Приветствую тебя, какой город тебя интересует?')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = round(data["main"]["temp"])
        feels_like = round(data["main"]["feels_like"])
        temp_min = (data["main"]["temp_min"])
        temp_max = (data["main"]["temp_max"])
        bot.reply_to(message, f'Сейчас погода в городе {city.capitalize()} \n\n'
                          f'Текущая температура воздуха: {temp} °C \n'
                          f'Ощущается как: {feels_like} °C \n'
                          f'Минимальная температура: {temp_min}°C\n'
                          f'Максимальная температура: {temp_max}°C\n')
    else:
        bot.reply_to(message,f'Похоже ты не корректно указал город, попробуй еще раз')

bot.polling(none_stop=True)