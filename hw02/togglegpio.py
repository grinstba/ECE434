#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time
import sys

def main(argv):
    
    if (len(argv) > 1):
        print('Only one argument allowed')
        return
    elif (len(argv) < 1):
        print('One argument needed')
        return
    
    # Parse argument
    sleepTime = float(argv[0])
    
    # Define LED pin
    LED = 'P9_25'
    
    GPIO.setup(LED, GPIO.OUT)
    
    # Main loop
    while True:
        # LED on
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(sleepTime)
        # LED off
        GPIO.output(LED, GPIO.LOW)
        time.sleep(sleepTime)
        
if __name__ == "__main__":
   main(sys.argv[1:])