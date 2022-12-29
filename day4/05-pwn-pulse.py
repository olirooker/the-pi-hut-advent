from machine import Pin, PWM
from time import sleep

green = PWM(Pin(18))
green.freq(1000)

amber = PWM(Pin(19))
amber.freq(1000)

red = PWM(Pin(20))
red.freq(1000)

while True:
    for duty in range(0,65535):
        green.duty_u16(duty)
        amber.duty_u16(duty)
        red.duty_u16(duty)
        sleep(0.0001)