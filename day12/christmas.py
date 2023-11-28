import time
from machine import Pin
from neopixel import NeoPixel
import random

# Initialize the Neopixel strip
strip = NeoPixel(Pin(28), 15)

# Define Christmas colors
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
colors = [red, green, white]

def fill(color):
    for i in range(len(strip)):
        strip[i] = color
    strip.write()

def twinkling_effect(cycles, speed=0.1):
    for _ in range(cycles):
        # Randomly pick a LED to twinkle
        led = random.randint(0, len(strip) - 1)
        original_color = strip[led]

        # Twinkle with white color
        strip[led] = white
        strip.write()
        time.sleep(speed)

        # Revert back to original color
        strip[led] = original_color
        strip.write()
        time.sleep(speed)

while True:
    for color in colors:
        fill(color)
        time.sleep(0.5)
        twinkling_effect(10, 0.05)
