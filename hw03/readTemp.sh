#!/bin/sh

# Read Temperature from chip
temp=`i2cget -y 2 0x48`
# Convert temp to F
temp9=$(($temp *9))
temp95=$(($temp9 /5))
tempF=$(($temp95 +32))
# Print temp to console
echo "$tempF"