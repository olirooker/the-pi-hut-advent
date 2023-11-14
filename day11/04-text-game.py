# Imports
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# Set up the button
button = Pin(8, Pin.IN, Pin.PULL_DOWN)

# Set up I2C and the pins we're using for it
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

# Short delay to stop I2C falling over
time.sleep(1) 

# Define the display and size (128x32)
display = SSD1306_I2C(128, 32, i2c)

# Create variables
state = 0

while True: # Loop forever
    
    time.sleep(0.1) # Delay before changing marker
    
    if state == 0: # If state is 0
        
        display.fill(0) # Clear the display
        display.text("Naughty or Nice?",0,0) # Line 1
        display.text(">Naughty  Nice",0,24) # Line 3
        
        display.show() # Update the display
        
        state = 1 # State change
        
        if button.value() == 1: # If button clicked
            
            display.fill(0) # Clear the display
            display.text("Oh no!",0,0) # Line 1
            display.text(">Naughty  Nice",0,24) # Line 3

            display.show()  # Update the display
            
            time.sleep(2) # Delay

    elif state == 1: # If state is 1
        
        display.fill(0) # Clear the display
        display.text("Naughty or Nice?",0,0) # Line 1
        display.text(" Naughty >Nice",0,24) # Line 3
        
        display.show()  # Update the display
        
        state = 0 # State change
        
        if button.value() == 1: # If button clicked
            
            display.fill(0) # Clear the display
            display.text("Yay!",0,0) # Line 1
            display.text(" Naughty >Nice",0,24) # Line 3
            
            display.show()  # Update the display
            
            time.sleep(2) # Delay
