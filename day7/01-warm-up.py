# Give the sensor time to baseline surroundings

# Imports
from machine import Pin
import time
 
# Set up PIR pin with pull down
pir = Pin(26, Pin.IN, Pin.PULL_DOWN)
print("Warming up...")
time.sleep(10) # Delay to allow the sensor to settle
print("Sensor ready!")

while True: # Run forever
    time.sleep(0.01) # Delay to stop unnecessary program speed
    
    if pir.value() == 1: # If PIR detects movement
        print("I SEE YOU!")
        time.sleep(5) # Wait 5 seconds before looking for more movement
        print("Sensor active") # Let us know that the sensor is active
