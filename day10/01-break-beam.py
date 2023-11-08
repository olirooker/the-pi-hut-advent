from machine import Pin
import time

# Set up our beam pin
beam = Pin(26, Pin.IN, Pin.PULL_DOWN)

while True:
    time.sleep(0.1)
    if beam.value() == 0: # If the beam is broken
        print("Beam Broken!")
