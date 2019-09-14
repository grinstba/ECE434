#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time

LED1 = 'P9_25'
LED2 = 'P9_27'
LED3 = 'P9_29'
LED4 = 'P9_31'

Button1 = 'P9_11'
Button2 = 'P9_16'
Button3 = 'P9_17'
Button4 = 'P9_13'

LEDmap = {
    'P9_11': 'P9_25',
    'P9_16': 'P9_27',
    'P9_17': 'P9_29',
    'P9_13': 'P9_31'
}

def updateLED(channel):
    GPIO.output(LEDmap[channel], not GPIO.input(LEDmap[channel]))

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

GPIO.setup(Button1, GPIO.IN)
GPIO.setup(Button2, GPIO.IN)
GPIO.setup(Button3, GPIO.IN)
GPIO.setup(Button4, GPIO.IN)

GPIO.add_event_detect(Button1, GPIO.RISING, callback=updateLED)
GPIO.add_event_detect(Button2, GPIO.RISING, callback=updateLED)
GPIO.add_event_detect(Button3, GPIO.RISING, callback=updateLED)
GPIO.add_event_detect(Button4, GPIO.RISING, callback=updateLED)

while True:
    pass