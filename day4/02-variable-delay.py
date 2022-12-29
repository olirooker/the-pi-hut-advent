# Imports
from machine import ADC, Pin
import time

# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# Set up the red LED pin
red = Pin(18, Pin.OUT)

# Create a variable called mydelay and start at 0
mydelay = 0

while True: # Loop forever
    # Update our variable with the reading divided by 65000
    mydelay = potentiometer.read_u16() / 65000
    
    # Red LED on for the variable delay period
    red.value(1)
    time.sleep(mydelay)
    
    # Red LED off for the variable delay period
    red.value(0)
    time.sleep(mydelay)