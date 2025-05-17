import telebot
from config import BOT_TOKEN, WEATHER_API_KEY
from controllers import AirQualityController

bot = telebot.TeleBot(BOT_TOKEN)
controller = None

def start_bot(tk_controller=None):
    global controller
    controller = AirQualityController(bot, WEATHER_API_KEY, tk_controller)
    bot.polling()

def stop_bot():
    bot.stop_polling()
