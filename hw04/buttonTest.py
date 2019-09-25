#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO

# Define button pins
Button1 = 'P9_41'
Button2 = 'P9_42'

# Setup button pins to be input
GPIO.setup(Button1, GPIO.IN)
GPIO.setup(Button2, GPIO.IN)

def buttonPrint(channel):
    print(channel)

# Setup buttons to trigger a function
GPIO.add_event_detect(Button1, GPIO.RISING, callback=buttonPrint)
GPIO.add_event_detect(Button2, GPIO.RISING, callback=buttonPrint)

# Keep program running
while True:
    pass