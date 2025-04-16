from telebot import types


class AirQualityView:
    @staticmethod
    def send_welcome(message, bot):
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        btn_location = types.KeyboardButton("Отправить местоположение 📍", request_location=True)
        markup.add(btn_location)
        bot.send_message(message.chat.id,
                         "Привет! Нажми кнопку ниже, чтобы поделиться своим местоположением.",
                         reply_markup=markup)

    @staticmethod
    def send_air_quality_data(message, bot, aqi_data, interpret_func):
        aqi = aqi_data["list"][0]["main"]["aqi"]
        components = aqi_data["list"][0]["components"]

        response = (
            f"Индекс качества воздуха (AQI): {aqi} - {interpret_func(aqi)}\n\n"
            "Концентрации загрязняющих веществ (μg/m³):\n"
            f"- CO (Угарный газ): {components['co']}\n"
            f"- NO₂ (Диоксид азота): {components['no2']}\n"
            f"- O₃ (Озон): {components['o3']}\n"
            f"- SO₂ (Диоксид серы): {components['so2']}\n"
            f"- PM2.5 (Твёрдые частицы <2.5μm): {components['pm2_5']}\n"
            f"- PM10 (Твёрдые частицы <10μm): {components['pm10']}\n"
            f"- NH₃ (Аммиак): {components['nh3']}"
        )

        bot.send_message(message.chat.id, response)
