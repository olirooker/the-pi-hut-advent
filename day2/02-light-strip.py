from machine import Pin
import time
import sys

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

for i in range(10):
    if i % 5 == 0:
        print(i)
    red.value(1)
    time.sleep(0.1)
    red.value(0)
    amber.value(1)
    time.sleep(0.1)
    amber.value(0)
    green.value(1)
    time.sleep(0.1)
    green.value(0)
#     and back
    time.sleep(0.1)
    amber.value(1)
    time.sleep(0.1)
    amber.value(0)