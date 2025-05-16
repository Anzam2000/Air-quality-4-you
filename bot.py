import telebot
from config import BOT_TOKEN, WEATHER_API_KEY
from controllers import AirQualityController

bot = telebot.TeleBot(BOT_TOKEN)
controller = AirQualityController(bot, WEATHER_API_KEY)


def start_bot():
    bot.polling()
def stop_bot():
    bot.stop_polling()
