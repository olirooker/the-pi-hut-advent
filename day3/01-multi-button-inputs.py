# Imports
from machine import Pin
import time

# Set up our button names and GPIO pin numbers
# Also set pins as inputs and use pull downs
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

while True: # Loop forever
    
    time.sleep(0.2) # Short Delay
        
    if button1.value() == 1 and button2.value() == 1: # If button 1 and 2 are pressed at the same
        
        print("Buttons 1 and 2 pressed")
        green.value(1) # green LED on
        
    elif button1.value() == 1: # If button 1 is pressed
        
        print("Button 1 pressed")
        amber.value(1) # amber LED on
        
    else: # If no buttons are being pressed
        
        red.value(1) # red LED on
        amber.value(0) # amber LED off
        green.value(0) # green LED off
