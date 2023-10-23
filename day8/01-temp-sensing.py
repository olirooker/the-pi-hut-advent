# Imports
import onewire, ds18x20, time
from machine import Pin
 
# Set the data pin for the sensor
SensorPin = Pin(26, Pin.IN)
 
# Tell MicroPython we're using a DS18B20 sensor, and which pin it's on
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))
 
# Look for DS18B20 sensors (each contains a unique rom code)
roms = sensor.scan()

while True: # Run forever
    sensor.convert_temp() # Convert the sensor units to centigrade
    time.sleep(2) # Wait 2 seconds (you must wait at least 1 second before taking a reading)
 
    for rom in roms: # For each sensor found (just 1 in our case)
        # print((sensor.read_temp(rom)),"°C")
        print(f"{sensor.read_temp(rom)}°C")
        time.sleep(5)
