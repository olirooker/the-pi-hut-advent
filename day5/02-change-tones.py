# Imports
from machine import Pin, PWM
import time

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

# Set PWM duty - volume
buzzer.duty_u16(3000)

# Set PWM frequency to 1000 for one second
buzzer.freq(1000)
time.sleep(1)

# Set PWM frequency to 500 for one second
buzzer.freq(500)
time.sleep(1)

# Buzzer off
buzzer.duty_u16(0)