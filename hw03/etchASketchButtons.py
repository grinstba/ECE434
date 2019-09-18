#!/usr/bin/env python3
import random
import smbus
import Adafruit_BBIO.GPIO as GPIO

bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)


# Define button pins
Button1 = 'P9_11'
Button2 = 'P9_16'
Button3 = 'P9_17'
Button4 = 'P9_13'
Button5 = 'P9_30'

# Setup button pins to be input
GPIO.setup(Button1, GPIO.IN)
GPIO.setup(Button2, GPIO.IN)
GPIO.setup(Button3, GPIO.IN)
GPIO.setup(Button4, GPIO.IN)
GPIO.setup(Button5, GPIO.IN)

# Generate a random starting location
xPos = random.randint(0, 7)
yPos = random.randint(0, 7)

# The first byte is GREEN, the second is RED.
hexGrid = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]

# Create the grid
grid = [[0 for i in range(8)] for j in range(8)]

# Write to the LED matrix
bus.write_i2c_block_data(matrix, 0, hexGrid)

# Function calcualtes the needed values in order to light up the matrix
def updateMatrix():
    global hexGrid, bus, xPos, yPos, grid
    
    for k in range(len(grid)):
        byte = 0
        for i in range(len(grid[k])):
            if (grid[k][i]):
                byte+= 2**i
                
        hexGrid[2*k] = byte
    
    # Write to the matrix
    bus.write_i2c_block_data(matrix, 0, hexGrid)

# Move the cursor down
def cursorDown(channel=None):
    global xPos, yPos, grid
    if (yPos < 7):
        yPos+=1
    
    grid[xPos][yPos] = 1
    updateMatrix()
 
 # Move the cursor up   
def cursorUp(channel=None):
    global xPos, yPos, grid
    if (yPos > 0):
        yPos-=1
    
    grid[xPos][yPos] = 1
    updateMatrix()
   
# Move the cursor left 
def cursorLeft(channel=None):
    global xPos, yPos, grid
    if (xPos < 7):
        xPos+=1
    
    grid[xPos][yPos] = 1
    updateMatrix()
    
# Move the cursor right
def cursorRight(channel=None):
    global xPos, yPos, grid
    if (xPos > 0):
        xPos-=1
    
    grid[xPos][yPos] = 1
    updateMatrix()

# Clear the whole board
def clearGrid(channel=None):
    global grid
    grid = [[0 for i in range(8)] for j in range(8)]
    updateMatrix()

# Setup buttons to trigger a function
GPIO.add_event_detect(Button1, GPIO.RISING, callback=cursorLeft)
GPIO.add_event_detect(Button2, GPIO.RISING, callback=cursorDown)
GPIO.add_event_detect(Button3, GPIO.RISING, callback=cursorRight)
GPIO.add_event_detect(Button4, GPIO.RISING, callback=cursorUp)
GPIO.add_event_detect(Button5, GPIO.RISING, callback=clearGrid)

# Main loop that waits for interrupts
while True:
    pass