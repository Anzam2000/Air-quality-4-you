import sqlite3 as sl
import pandas as pd
from datetime import datetime
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
class DataBase:
    def __init__(self, db_path='my_database.db'):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        connection = sl.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                registration_date TEXT,
                aqi_levels TEXT
            )
        ''')
        connection.commit()
        connection.close()

    def insert_user(self, username, aqi_level):
        current_date = datetime.now().strftime('%m-%d')
        connection = sl.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO Users (username, registration_date, aqi_levels)
            VALUES (?, ?, ?)
        ''', (username, current_date, str(aqi_level)))
        connection.commit()
        connection.close()

    def get_all_data(self):
        connection = sl.connect(self.db_path)
        df = pd.read_sql_query("SELECT username, registration_date, aqi_levels FROM Users", connection)
        connection.close()
        return df
