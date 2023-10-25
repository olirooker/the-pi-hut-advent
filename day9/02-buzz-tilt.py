from machine import Pin, PWM
import time

# Set up tilt sensor pin
tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

# Set PWM frequency to 1000
buzzer.freq(1000)

while True:
    time.sleep(0.01)
    if tilt.value() == 0: # If sensor is LOW - other way in instructions
        print("***TILT DETECTED***")
        buzzer.duty_u16(10000) # Set duty (volume up)
        time.sleep(0.2)
        buzzer.duty_u16(0) # Duty to zero (volume off)
