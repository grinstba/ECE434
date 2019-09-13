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
# Button5 = 'P9_30'

def ledOn(channel):
    print(channel)
    GPIO.remove_event_detect(channel)
    GPIO.add_event_detect(channel, GPIO.FALLING, callback=ledOff)
    if (channel == 'P9_11'):
        GPIO.output(LED1, 1)
    elif (channel == 'P9_16'):   
        GPIO.output(LED2, 1)
    elif (channel == 'P9_17'):
        GPIO.output(LED3, 1)
    elif (channel == 'P9_13'):
        GPIO.output(LED4, 1)
    
def ledOff(channel):
    GPIO.remove_event_detect(channel)
    GPIO.add_event_detect(channel, GPIO.RISING, callback=ledOn)
    if (channel == 'P9_11'):
        GPIO.output(LED1, 0)
    elif (channel == 'P9_16'):   
        GPIO.output(LED2, 0)
    elif (channel == 'P9_17'):
        GPIO.output(LED3, 0)
    elif (channel == 'P9_13'):
        GPIO.output(LED4, 0)

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

GPIO.setup(Button1, GPIO.IN)
GPIO.setup(Button2, GPIO.IN)
GPIO.setup(Button3, GPIO.IN)
GPIO.setup(Button4, GPIO.IN)
# GPIO.setup(Button5, GPIO.IN)

GPIO.add_event_detect(Button1, GPIO.RISING, callback=ledOn)
GPIO.add_event_detect(Button2, GPIO.RISING, callback=ledOn)
GPIO.add_event_detect(Button3, GPIO.RISING, callback=ledOn)
GPIO.add_event_detect(Button4, GPIO.RISING, callback=ledOn)

while True:
    pass