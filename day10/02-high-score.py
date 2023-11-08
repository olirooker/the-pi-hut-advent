from machine import Pin, PWM
import time, sys

# Set up the Break Beam pin
beam = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13))

# Set buzzer PWM frequency to 1000
buzzer.freq(1000)

# Start with the buzzer volume off (duty 0)
buzzer.duty_u16(0)

# Create game variables
starttime = 0
timecheck = 0
scorecounter = 0
state = 0

print("Game starts after the beep!")

#Long beep to signal game start
buzzer.duty_u16(10000)
time.sleep(2)
buzzer.duty_u16(0)

print("GO!")
    
# Store our start time (seconds)
starttime = time.time()

while True: # Run this block until code stopped
    time.sleep(0.0001) # Very short delay
    # Take the current epoch time and minus the start time
    # This gives us the number of seconds since we started the game
    timecheck = time.time() - starttime
    if timecheck >= 30: # If 30 or more seconds have passed
        print("GAME OVER!")
        # Beep to signal game end
        buzzer.duty_u16(10000)
        time.sleep(0.2)
        buzzer.duty_u16(0)
        # Print the player's score
        print("YOUR SCORE:",scorecounter)
        # Exit the program
        sys.exit()
   
    elif state == 0 and beam.value() == 0: # If state is 0 AND our pin is LOW
         scorecounter = scorecounter + 1 # Add +1 to our score counter
         state = 1 # Change state to 1
         print("SCORE =",scorecounter) # Print our new score counter
         print("Time remaining:", (30 - timecheck)) # take our timecheck variable away from 30 - gives the remaining time
        
    elif state == 1 and beam.value() == 1: # If state is 1 AND our pin is HIGH
        state = 0 # Change the state to 0