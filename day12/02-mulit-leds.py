import time
from machine import Pin
from neopixel import NeoPixel

strip = NeoPixel(Pin(28), 15)

for i in range(15):
    strip[i] = (255, 224, 189)

strip.write()
