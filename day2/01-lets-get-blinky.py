from machine import Pin
import time
onboardLED = Pin(25, Pin.OUT)

for i in range(10):
#     These do the same thing
    onboardLED.value(1)
    time.sleep(0.5)
    onboardLED.value(0)
    time.sleep(0.5)


#     onboardLED.high()
    # onboardLED.value(1)
#     onboardLED.low()
    # onboardLED.value(0)