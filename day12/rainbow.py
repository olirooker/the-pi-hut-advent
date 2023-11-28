import time
from machine import Pin
from neopixel import NeoPixel

PIN = 28
NUM_LEDS = 15

strip = NeoPixel(Pin(28), 15)

def wheel(pos):
    # Generate rainbow colors across 0-255 positions.
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(NUM_LEDS):
            rc_index = (i * 256 // NUM_LEDS) + j
            strip[i] = wheel(rc_index & 255)
        strip.write()
        time.sleep(wait)

while True:
    rainbow_cycle(0.001)  # Rainbow cycle with 1ms delay per step
