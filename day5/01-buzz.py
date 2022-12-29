# Imports
from machine import Pin, PWM
import time

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

# Set PWM frequency to 1000
buzzer.freq(1000)

# Set PWM duty
buzzer.duty_u16(2000)

time.sleep(1) # Wait 1 second

# Duty to 0 to turn the buzzer off
buzzer.duty_u16(0)