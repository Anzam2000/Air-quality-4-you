 # Air-quality-4-you
Телеграм бот для отслежевания качества воздуха в вашем городе. 
# Суть проекта: 
Телеграм бот который:
 ✅ Отправляет текущий индекс качества воздуха (AQI).
 
 ✅ Уведомляет о критических уровнях загрязнения.
 
 ✅ Предоставляет рекомендации (например, носить маску, закрывать окна).
# Цель проекта:
Разработка телеграм бота с помощью библиотеки telebot для отслеживания качества воздуха с помощью OpenWeatherMap	
# Актуальность:
 ✅ Загрязнение воздуха  - распрастраненная проблема для крупных городов(Москва, Новосибирск, СПБ).
 
 ✅ Люди с астмой, аллергией, сердечно-сосудистыми заболеваниями нуждаются в актуальных данных.
# Задачи:
🔹 Настроить парсинг данных из OpenWeatherMap.

🔹 Реализовать бота на Python с помощью telebot

🔹 Добавить геолокацию (автоматическое определение города).

🔹 Разработать систему уведомлений.

🔹 Сделать визуализацию данных (графики, цветовые индикаторы).

🔹 Запустить бота на сервере.

🔹 Разработка админки на tkinter.
# Целевая аудитория
    Жители крупных городов (Москва, СПб, Новосибирск, др.).
    
    Люди с заболеваниями дыхательной системы (астма, аллергия).
# Схема проекта
![Air-quality-4-you drawio(1)](https://github.com/user-attachments/assets/37e52eb1-aaf3-432b-9d51-911b37557598)


# Как запустить проект на своем компьютере?
1. Скачивание PyCharm

    Перейдите на официальный сайт JetBrains: https://www.jetbrains.com/pycharm/
   Выберите версию:

    Community Edition (бесплатная, с базовыми функциями для Python)

    Professional Edition (платная, с расширенными возможностями, включая поддержку Django, Flask, научных инструментов и др.)
   Нажмите Download и дождитесь загрузки установочного файла.
2. Установка

    Запустите скачанный .exe файл.

    Следуйте инструкциям мастера установки.

    На этапе выбора компонентов можно оставить галочки:

        Create Desktop Shortcut (создать ярлык на рабочем столе)

        Add "Open Folder as Project" (добавить в контекстное меню проводника)

        Add launchers dir to the PATH (добавить в PATH для запуска из командной строки)

    Нажмите Install и дождитесь завершения.

    После установки можно запустить PyCharm.
3. Создание проекта
   Создайте в новом проекте файлы bot.py, controllers.py, models.py, views.py, config.py
4. Вставьте код с репозитория в файлы в вашем компьтеры
5. config.py
6. 
   Я не добавил файл config.py так как в нем ключи для OpenWeather и телеграмм бота
   
   BOT_TOKEN = ""
   
   WEATHER_API_KEY = ""
   
   Скоприруйте эти 2 строчки в config.py и вставьте в ковычки ваш токен и ключ

8. Проект готов к запуску!
# Так же у проекта есть основной бот
@Air_quality_4_you_bot
