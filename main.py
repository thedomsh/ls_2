import requests
import sqlite3
from datetime import datetime
from pprint import pprint

API = 'ccdd17f96d6dd55e8a75e51f425e8112'

parameters = {
    'appid': API,
    'units': 'metric',
    'lang': 'ru'
}

while True:
    city = input('Введите город, в котором хотите узнать погоду: ')
    if city.lower() == 'stop':
        break
    parameters['q'] = city
    try:
        data = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameters).json()
        temp = data['main']['temp']
        wind_speed = data['wind']['speed']
        timezone = data['timezone']
        description = data['weather'][0]['description']
        sunrise = datetime.utcfromtimestamp(data['sys']['sunrise'] + timezone).strftime('%Y-%m-%d %H:%M:%S')
        sunset = datetime.utcfromtimestamp(data['sys']['sunset'] + timezone).strftime('%Y-%m-%d %H:%M:%S')

        print(f'''В городе {city} сейчаc {description}
Температура: {temp} ℃
Скорость ветра: {wind_speed} м/c
Рассвет: {sunrise}
Закат: {sunset}''')

        database = sqlite3.connect('ls2.db')
        cursor = database.cursor()

        cursor.execute('''
        INSERT INTO weather(city, temp, wind, description, sunrise, sunset)
        VALUES (?,?,?,?,?,?)
        ''', (city, temp, wind_speed, description, sunrise, sunset))

        database.commit()
        database.close()

    except Exception as e:
        print(e)
        print('Вы ввели не корректный город. Попробуйте снова.')

