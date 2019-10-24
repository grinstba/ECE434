#!/usr/bin/env python3
import smbus
import time
import subprocess
import postToSheet

subprocess.call(['./setup.sh'])

bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x49

oldTemp1 = None

while True:
    temp1 = bus.read_byte_data(address1, 0)
    temp1 *= 9
    temp1 /= 5
    temp1 += 32
    
    if(temp1 != oldTemp1):
        print('Posting ' + str(temp1) + ' to Google')
        postToSheet.main(temp1)
        oldTemp1 = temp1
        
    else:
        time.sleep(0.1)