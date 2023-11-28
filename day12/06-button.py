import time
from machine import Pin
from neopixel import NeoPixel

button = Pin(15, Pin.IN, Pin.PULL_DOWN)

strip = NeoPixel(Pin(28), 15)

red = 255,0,0
green = 0,255,0
blue= 0,0,255

colours = [red, green, blue]

myindex = 0

indexlength = len(colours) -1

while True:
    time.sleep(0.4)
    
    if button() == 1: # If button pressed
        
        # If the index variable is less than or equal to the lengh of the index
        if myindex < indexlength:
            
            # Add +1 to the index variable
            myindex = myindex + 1
        
        # If the index variable is over the index length
        else:
            # Set index variable back to 0 (the first item in our list)
            myindex = 0
        
        # Fill the strip with the current list index colour
        strip.fill((colours[myindex]))

        strip.write()
