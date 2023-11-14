# Imports
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# Set up I2C and the pins we're using for it
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

# Short delay to stop I2C falling over
time.sleep(1) 

# Define the display and size (128x32)
display = SSD1306_I2C(128, 32, i2c) 

counter = 0 # Start our counter at zero

while True: # Loop forever

    display.fill(0) # Clear the display
    
    print(counter) # Print the current count
    
    # Show the counter on the display
    # The display library expects strings only
    # Counter is a number (integer) so we convert it to text (a string) with 'str'
    display.text("The Endless",0,0)
    display.text("Counter!",0,12)
    display.text((str(counter)),0,24)

    # Update the display
    display.show()  
    
    # Short delay
    time.sleep(1)
    
    # Add 1 to our counter  
    counter += 1