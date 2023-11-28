import time
from machine import Pin, ADC
from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

# Set up the potentiometer on ADC pin 26
potentiometer = ADC(Pin(26))

hotPink = 255, 105, 180
gold = 255, 215, 0
deepSkyBlue = 0, 191, 255
limeGreen = 50, 205, 50
violet = 238, 130, 238
chocolate = 210, 105, 30
coral = 255, 127, 80
midnightBlue = 25, 25, 112
tomato = 255, 99, 71
royalBlue = 65, 105, 225
turquoise = 64, 224, 208
orchid = 218, 112, 214
sienna = 160, 82, 45
plum = 221, 160, 221
seaGreen = 46, 139, 87

colours = [hotPink, gold, deepSkyBlue, limeGreen, violet, chocolate, coral, midnightBlue, tomato, royalBlue, turquoise, orchid, sienna, plum, seaGreen]

while True:
    for j in colours:
        for i in range(15):       
            # Set the next LED in the range to light with a colour
            strip[i] = (j)
            
            # Read the potentiometer
            # Divide the reading to make it more usable as a time delay
            mydelay = potentiometer.read_u16() / 50000
            
            # Delay - the speed of the chaser
            time.sleep(mydelay)
            strip.write()
