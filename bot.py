import telebot
from config import BOT_TOKEN, WEATHER_API_KEY
from controllers import AirQualityController

bot = telebot.TeleBot(BOT_TOKEN)
controller = AirQualityController(bot, WEATHER_API_KEY)

if __name__ == "__main__":
    bot.polling()
