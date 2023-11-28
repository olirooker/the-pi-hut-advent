import time
from machine import Pin
from neopixel import NeoPixel

strip = NeoPixel(Pin(28), 15)

pink = 255,20,147

strip.fill((pink))

strip.write()