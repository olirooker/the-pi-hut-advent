# Imports
from machine import Pin
import time

# Set up the LED pins
red = Pin(20, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)

red.value(0)
amber.value(0)
green.value(0)