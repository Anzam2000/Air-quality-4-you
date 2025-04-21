from models import *
from views import AirQualityView
import time
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

class AirQualityController:
    def __init__(self, bot, api_key):
        self.db = DataBase()
        self.bot = bot
        self.model = AirQualityModel(api_key)
        self.view = AirQualityView()
        self.setup_handlers()

    def setup_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            self.view.send_welcome(message, self.bot)

        @self.bot.message_handler(content_types=['text'])
        def handle_location(message):
            if message.text == "Отправляй качество воздуха только сейчас":
                self.view.send(message, self.bot)

                @self.bot.message_handler(content_types=['location'])
                def location(message):
                    if message.location:
                        lat = message.location.latitude
                        lon = message.location.longitude
                        air_quality_data = self.model.get_air_quality(lat, lon)
                        aqi = air_quality_data["list"][0]["main"]["aqi"]
                        self.view.send_air_quality_data(
                            message,
                            self.bot,
                            air_quality_data,
                            self.model.interpret_aqi
                        )

                        self.db.insert_user(message.from_user.id, message.from_user.username, aqi)

                        df = self.db.get_all_data()
                        df['registration_date'] = pd.to_datetime(df['registration_date'], format='%m-%d %H:%M')
                        df['aqi_levels'] = pd.to_numeric(df['aqi_levels'])
                        df['label'] = df['registration_date'].dt.strftime('%m-%d %H:%M')

                        plt.figure(figsize=(10, 5))
                        plt.bar(df['label'], df['aqi_levels'], color='skyblue')
                        plt.title('AQI уровни по дате и времени')
                        plt.xlabel('Дата и время (MM-DD HH:MM)')
                        plt.ylabel('AQI уровень')
                        plt.xticks(rotation=45)
                        plt.grid(axis='y')
                        plt.tight_layout()

                        image_path = f"aqi_chart_{message.from_user.username}.png"
                        plt.savefig(image_path)
                        plt.close()

                        with open(image_path, 'rb') as photo:
                            self.bot.send_photo(message.chat.id, photo, caption="Ваш график AQI 📈")
                        print("Гео")

            if message.text == "Отправляй качество воздуха раз в день":
                self.view.send_day(message, self.bot)

                @self.bot.message_handler(content_types=['location'])
                def location_day(message):
                    while True:
                        if message.location:
                            lat = message.location.latitude
                            lon = message.location.longitude
                            air_quality_data = self.model.get_air_quality(lat, lon)
                            aqi = air_quality_data["list"][0]["main"]["aqi"]
                            self.view.send_air_quality_data(
                                message,
                                self.bot,
                                air_quality_data,
                                self.model.interpret_aqi
                            )

                            self.db.insert_user(message.from_user.id, message.from_user.username, aqi)

                            df = self.db.get_all_data()
                            df['registration_date'] = pd.to_datetime(df['registration_date'], format='%m-%d %H:%M')
                            df['aqi_levels'] = pd.to_numeric(df['aqi_levels'])
                            df['label'] = df['registration_date'].dt.strftime('%m-%d %H:%M')

                            plt.figure(figsize=(12, 5))
                            plt.bar(df['label'], df['aqi_levels'], color='skyblue')
                            plt.title('AQI уровни по дате и времени')
                            plt.xlabel('Дата и время (MM-DD HH:MM)')
                            plt.ylabel('AQI уровень')
                            plt.xticks(rotation=45)
                            plt.grid(axis='y')
                            plt.tight_layout()

                            image_path = f"aqi_chart_{message.from_user.username}.png"
                            plt.savefig(image_path)
                            plt.close()

                            with open(image_path, 'rb') as photo:
                                self.bot.send_photo(message.chat.id, photo, caption="Ваш график AQI 📈")

                            time.sleep(86400)
                            print("Гео 5")
