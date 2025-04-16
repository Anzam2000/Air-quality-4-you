import requests
class AirQualityModel:
    def __init__(self, api_key):
        self.api_key = api_key
    def get_air_quality(self, lat, lon):
        base_url = "http://api.openweathermap.org/data/2.5/air_pollution"
        params = {
                 "lat": lat,
                 "lon": lon,
                 "appid": self.api_key
             }
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    def interpret_aqi(self, aqi):
        aqi_levels = {
            1: "Хороший",
            2: "Удовлетворительный",
            3: "Умеренный",
            4: "Плохой",
            5: "Очень плохой"
         }
        return aqi_levels.get(aqi, "Неизвестный уровень")
