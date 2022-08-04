import requests
import sqlite3
from datetime import datetime
from pprint import pprint

API = '7bb2a5eb-82fa-4102-9fc9-c8d5cea2a5a3'

parameters = {
    'appid': API,
    'units': 'metric',
    'lang': 'ru'
}
while True:
    city = input('Введите город Узбекистана: ')
    if city.lower() == 'stop':
        break
    parameters['q'] = city
    try:
        data = requests.get('https://yandex.uz/pogoda', params=parameters).json()
        temperature = data['temp']
        day_temperature = data['weather-table__daypart']['weather-table__temp']
        humidity = data['term__value']['humidity']
        wind_speed = data['term__value']['wind-speed']

    print(f'''В городе {city}
    Температура: {temperature} ℃
    Влажность: {humidity} %
    Скорость ветра: {wind_speed} м/с
    Температура днем: {day_temperature}''')

    database = sqlite3.connect('ls2.db')
    cursor = database.cursor()

    cursor.execute('''
            INSERT INTO weather(city, temperature, wind_speed, humidity, day_temp)
            VALUES (?,?,?,?,?,?)
            ''', (city, temperature, wind_speed, humidity, day_temperature))

    database.commit()
    database.close()

