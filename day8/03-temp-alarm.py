import onewire, ds18x20, time
from machine import Pin, PWM

red = Pin(20, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13))

# Start PWM duty to 0% at program start
buzzer.duty_u16(0)
 
# Set the data pin for the sensor
SensorPin = Pin(26, Pin.IN)
 
# Tell MicroPython that we're using a DS18B20 sensor, and which pin it's on
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))

# Look for DS18B20 sensors (each contains a unique rom code)
roms = sensor.scan()

def alarm(): # Our alarm function 
    buzzer.duty_u16(10000) # Buzzer duty (volume) up

    for i in range(5):
        buzzer.freq(5000) # Higher pitch
        
        # LEDs ON
        red.value(1)
        amber.value(1)
        green.value(1)
        
        time.sleep(0.2)
        
        buzzer.freq(1000) # Lower pitch
        
        # LEDs OFF
        red.value(0)
        amber.value(0)
        green.value(0)        
        
        time.sleep(0.2)

    buzzer.duty_u16(0) # Buzzer duty (volume) off 

while True:
    time.sleep(5)
  
    for rom in roms: # For each sensor found (just 1 in our case)
        sensor.convert_temp() # Convert the sensor units to centigrade
        time.sleep(1) # Always wait 1 second after converting
    
        reading = sensor.read_temp(rom) # Take a temperature reading
        print(reading)

        if reading < 20:        
            alarm()
