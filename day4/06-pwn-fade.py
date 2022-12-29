from machine import Pin, PWM
from time import sleep

# Set up pins
green = PWM(Pin(18))
green.freq(1000)
amber = PWM(Pin(19))
amber.freq(1000)
red = PWM(Pin(20))
red.freq(1000)

# max brightness
maxWidth = 65535
# min brightness
minWidth = 3000

# how much to change the pulse-width by each step
step = round(maxWidth / 100)
currentWidth = minWidth

while True:
  green.duty_u16(currentWidth)
  amber.duty_u16(currentWidth)
  red.duty_u16(currentWidth)

# changes how fast the leds fade on and off
  sleep(0.01)

  currentWidth += step

# check currentWidth with max and min values and change direction of the step
  if currentWidth > maxWidth:
    currentWidth = maxWidth
    # flip the step to a negative number - to count down
    step *= -1
  elif currentWidth < minWidth:
    currentWidth = minWidth
    # flip the step to a positive number - to count up
    step *= -1