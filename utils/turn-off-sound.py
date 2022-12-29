# Imports
from machine import Pin, PWM, ADC
import time

# Set up the Buzzer and Potentiometer
potentiometer = ADC(Pin(27))
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

reading = 0 # Create a variable called 'reading' and set it to 0
    
reading = potentiometer.read_u16() # Read the potentiometer value and store it in our 'reading' variable
    
buzzer.freq(500) # Frequency to 500
buzzer.duty_u16(0) # Use the reading variable as the duty