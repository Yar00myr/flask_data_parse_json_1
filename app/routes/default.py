import requests
from flask import render_template
from os import getenv
from .. import app

api_key = getenv("api_key")


def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=' + api_key
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_data = {
            'temperature': round(data['main']['temp'] - 273.15, 1),
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return weather_data
    else:
        return None
    

@app.route('/')
def index():
    city = "Kyiv"
    weather = get_weather(city)
    return render_template('weather.html', weather=weather)