# Won't work with Pico in box

from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C 
import os, time, math, json, http.client
import urequests

def load_dotenv(dotenv_path=".env"):
    with open(dotenv_path) as file:
        for line in file:
            if line.startswith('#') or not line.strip():
                continue
            key, value = line.strip().split('=', 1)
            os.environ[key] = value

load_dotenv()

OPEN_WEATHER_KEY = os.getenv('OPEN_WEATHER_KEY')

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
time.sleep(1)
display = SSD1306_I2C(128, 32, i2c)

def wind_direction(degrees):
    value = math.floor(degrees / 22.5 + 0.5)
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return directions[value % 16]

# def get_current_weather(city):
#     conn = http.client.HTTPConnection("api.openweathermap.org")
#     try:
#         conn.request("GET", f"/data/2.5/weather?units=metric&appid={OPEN_WEATHER_KEY}&q={city}")
#         response = conn.getresponse()

#         if response.status != 200:
#             return f"HTTP Error: {response.status} - {response.reason}"

#         weather_data = response.read()
#         return json.loads(weather_data.decode('utf-8'))
#     except Exception as e:
#         # Generic exception handling, can be specialized as needed
#         return f"An error occurred: {e}"
#     finally:
#         conn.close()

def get_current_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?units=metric&appid={OPEN_WEATHER_KEY}&q={city}"

    response = urequests.get(url)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to retrieve data, status code:", response.status_code)

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        response.close()


def format_weather_data(data):
    return {
        'city': data['name'],
        'description': data['weather'][0]['description'].title(),
        'temp': data['main']['temp'],
        'wind_speed': data['wind']['speed'],
        'wind_direction': wind_direction(int(data['wind']['deg']))
    }

weather = get_current_weather("Sheffield")
formatted_weather = format_weather_data(weather)

# print(formatted_weather)

while True:
    # Display first screen
    time.sleep(0.5)
    display.fill(0)
    display.text(f"The weather in {formatted_weather['city']} is:",0,0)
    display.text(f"{formatted_weather['description']}",0,0)
    display.text(f"{formatted_weather['temp']}°C",0,0)
    display.show()

    # Display second screen
    time.sleep(5)
    display.fill(0)
    display.text(f"The weather in {formatted_weather['city']} is:",0,0)
    display.text(f"{formatted_weather['wind_speed']} kph",0,0)
    display.text(f"Wind direction of {formatted_weather['wind_direction']}",0,0)
    display.show()
    time.sleep(4.5)