# import time
from machine import Pin
from neopixel import NeoPixel

strip = NeoPixel(Pin(28), 15)

strip.write()