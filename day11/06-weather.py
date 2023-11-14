from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
from dotenv import load_dotenv
import os, requests, time, math

load_dotenv()
OPEN_WEATHER_KEY = os.getenv('OPEN_WEATHER_KEY')
base_url="https://api.openweathermap.org/data/2.5"

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
time.sleep(1)
display = SSD1306_I2C(128, 32, i2c)

def wind_direction(degrees):
    value = math.floor(degrees / 22.5 + 0.5)
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return directions[value % 16]

def get_current_weather(city):
    weather_data = requests.get(f"{base_url}/weather?units=metric&appid={OPEN_WEATHER_KEY}&q={city}")
    return {
        'city': weather_data.json()['name'],
        'description': weather_data.json()['weather'][0]['description'],
        'temp': weather_data.json()['main']['temp'],
        'wind_speed': weather_data.json()['wind']['speed'],
        'wind_direction': wind_direction(int(weather_data.json()['wind']['deg'])),
    }

weather = get_current_weather("Sheffield")

while True:
    # Display first screen
    time.sleep(0.5)
    display.fill(0)
    display.text(f"The weather in {weather['city']} is:",0,0)
    display.text(f"{weather['description'].title()}",0,0)
    display.text(f"{weather['temp']}°C",0,0)
    display.show()

    # Display second screen
    time.sleep(5)
    display.fill(0)
    display.text(f"The weather in {weather['city']} is:",0,0)
    display.text(f"{weather['wind_speed']} kph",0,0)
    display.text(f"Wind direction of {weather['wind_direction']}",0,0)
    display.show()
    time.sleep(4.5)