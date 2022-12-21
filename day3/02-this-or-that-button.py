# Imports
from machine import Pin
import time

# Set up our button names and GPIO pin numbers
# Also set pins as inputs and use pull downs
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)

# Set up our LED names and GPIO pin numbers
green = Pin(20, Pin.OUT)

while True: # Loop forever
    
    time.sleep(0.2) # Short Delay
        
    if button1.value() == 1 or button2.value() == 1: # If button 1 OR button 2 is pressed
        
        print("Button 1 or 2 pressed")
        
        green.value(1) # green LED on
        time.sleep(2)
        green.value(0) # green LED off
