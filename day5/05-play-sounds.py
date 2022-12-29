# Imports
from machine import Pin, PWM
import time
from notes import *

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

# Create volume variable (Duty cycle)
volume = 10000

# Create our function with arguments
def playtone(note,vol,length,delay2):
    buzzer.duty_u16(vol)
    buzzer.freq(note)
    time.sleep(length)
    buzzer.duty_u16(0)
    time.sleep(delay2)

# Zelda's Lullaby
playtone(E5,volume,0.5,0.1)
playtone(G5,volume,0.5,0.1)
playtone(D5,volume,0.5,0.05)
playtone(C5,volume,0.2,0.05)
playtone(D5,volume,0.2,0.1)

playtone(E5,volume,0.5,0.1)
playtone(G5,volume,0.5,0.1)
playtone(D5,volume,0.5,0.05)
playtone(C5,volume,0.2,0.05)
playtone(D5,volume,0.2,0.1)

playtone(E5,volume,0.5,0.1)
playtone(G5,volume,0.5,0.1)
playtone(D6,volume,0.5,0.07)

playtone(E5,volume,0.5,0.1)
playtone(G5,volume,0.5,0.1)
playtone(F5,volume,0.2,0.05)
playtone(E5,volume,0.2,0.05)
playtone(D5,volume,0.5,0.05)


# # Never Going to Give You Up
# playtone(C,volume,0.1,0.1)
# playtone(D,volume,0.1,0.1)
# playtone(F,volume,0.1,0.1)
# playtone(D,volume,0.1,0.2)
# playtone(A2,volume,0.1,0.2)
# playtone(A2,volume,0.1,0.2)
# playtone(G,volume,0.1,0.5)
# 
# playtone(C,volume,0.1,0.1)
# playtone(D,volume,0.1,0.1)
# playtone(F,volume,0.1,0.1)
# playtone(D,volume,0.1,0.2)
# playtone(G,volume,0.1,0.2)
# playtone(G,volume,0.1,0.2)
# playtone(F,volume,0.1,0.05)
# playtone(E,volume,0.1,0.05)
# playtone(D,volume,0.1,0.5)
# 
# playtone(C,volume,0.1,0.1)
# playtone(D,volume,0.1,0.1)
# playtone(F,volume,0.1,0.1)
# playtone(D,volume,0.1,0.1)
# playtone(F,volume,0.1,0.3)
# playtone(G,volume,0.1,0.07)
# playtone(E,volume,0.1,0.07)
# playtone(D,volume,0.1,0.1)
# playtone(C,volume,0.1,0.4)
# playtone(C,volume,0.1,0.1)
# playtone(G,volume,0.1,0.2)
# playtone(F,volume,0.1,0.2)