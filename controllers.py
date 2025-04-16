from telebot import types
from models import AirQualityModel
from views import AirQualityView

class AirQualityController:
    def __init__(self, bot, api_key):
        self.bot = bot
        self.model = AirQualityModel(api_key)
        self.view = AirQualityView()
        self.setup_handlers()

    def setup_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            self.view.send_welcome(message, self.bot)

        @self.bot.message_handler(content_types=['location'])
        def handle_location(message):
            if message.location:
                lat = message.location.latitude
                lon = message.location.longitude
                air_quality_data = self.model.get_air_quality(lat, lon)
                self.view.send_air_quality_data(
                    message,
                    self.bot,
                    air_quality_data,
                    self.model.interpret_aqi
                )
