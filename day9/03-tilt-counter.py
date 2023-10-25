from machine import Pin
import time

# Set up tilt sensor pin
tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Set up a counter variable at zero
tiltcount = 0

# Create a state variable at zero
state = 0

while True: # Run forever
    time.sleep(0.1) # Short delay
    if state == 0 and tilt.value() == 0: # If state is 0 and our pin is LOW - other way in guide
         tiltcount = tiltcount + 1 # Add +1 to tiltcount
         state = 1 # Change state to 1
         print("tilts =",tiltcount) # Print our new tiltcount
            
    if state == 1 and tilt.value() == 0: # If state is 1 and our pin is LOW                            
        state = 0 # Change the state to 0
