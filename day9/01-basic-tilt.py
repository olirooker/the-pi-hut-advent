from machine import Pin
import time

tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)

while True:
    time.sleep(0.10) # Short delay
    if tilt.value() == 0: # If sensor is LOW - for some reason this was the other way around in the guide
        print("I tilted!")
    else:
        print('No tilt')