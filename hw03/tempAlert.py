#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import smbus
import subprocess

subprocess.call(['./setup.sh'])

def alert(channel):
    print('Alert')
    if (channel=='P9_41'):
        print('Temp1: ' + str(bus.read_byte_data(address1, 0)))
    elif (channel=='P9_42'):
        print('Temp2: ' + str(bus.read_byte_data(address2, 0)))
        
# Define alert pins
Alert1 = 'P9_41'
Alert2 = 'P9_42'

# Set alert pins to input
GPIO.setup(Alert1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Alert2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Add function triggers to buttons
GPIO.add_event_detect(Alert1, GPIO.BOTH, callback=alert)
GPIO.add_event_detect(Alert2, GPIO.BOTH, callback=alert)

bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x49

bus.write_byte_data(address1, 3, 0x1B) # 27C
bus.write_byte_data(address1, 2, 0x19) # 25C
bus.write_byte_data(address1, 1, 0x80)
bus.write_byte_data(address2, 3, 0x1B) # 27C
bus.write_byte_data(address2, 2, 0x19) # 25C
bus.write_byte_data(address2, 1, 0x80)

while True:
   pass