# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)
        
# Select the first pixel (pixel 0)
# Set the RGB colour (red)
strip[0] = (255,0,0)

# strip[0] = (255, 0, 0) #Pure Red
# strip[1] = (0, 255, 0) #Pure Green
# strip[2] = (0, 0, 255) #Pure Blue
# strip[3] = (255, 255, 0) #Yellow (Red + Green)
# strip[4] = (0, 255, 255) #Cyan (Green + Blue)
# strip[5] = (255, 0, 255) #Magenta (Red + Blue)
# strip[6] = (192, 192, 192) #Silver
# strip[7] = (128, 0, 0) #Maroon
# strip[8] = (128, 128, 0) #Olive
# strip[9] = (0, 128, 0) #Dark Green
# strip[10] = (128, 0, 128) #Purple
# strip[11] = (0, 128, 128) #Teal
# strip[12] = (0, 0, 128) #Navy
# strip[13] = (255, 165, 0) #Orange
# strip[14] = (255, 192, 203) #Pink

# Send the data to the strip
strip.write()