#!/usr/bin/env python3
import random
import curses
import Adafruit_BBIO.GPIO as GPIO

Button1 = 'P9_11'
Button2 = 'P9_16'
Button3 = 'P9_17'
Button4 = 'P9_13'
Button5 = 'P9_30'

GPIO.setup(Button1, GPIO.IN)
GPIO.setup(Button2, GPIO.IN)
GPIO.setup(Button3, GPIO.IN)
GPIO.setup(Button4, GPIO.IN)
GPIO.setup(Button5, GPIO.IN)

def cursorUp(channel):
    global xPos, yPos, update
    yPos-= 1
    if (yPos <= 0):
        yPos = 0
    grid[yPos][xPos] = 'X'
    update = True
    
def cursorDown(channel):
    global xPos, yPos, update
    yPos+= 1
    if (yPos >= height):
        yPos = height - 1
    grid[yPos][xPos] = 'X'
    update = True
    
def cursorRight(channel):
    global xPos, yPos, update
    xPos+= 1
    if (xPos >= width):
        xPos = width - 1
    grid[yPos][xPos] = 'X'
    update = True
    
def cursorLeft(channel):
    global xPos, yPos, update
    xPos-= 1
    if (xPos <= 0):
        xPos = 0
    grid[yPos][xPos] = 'X'
    update = True
    
def clearGrid(channel):
    global update
    for k in range(len(grid)):
        for i in range(len(grid[k])):
            grid[k][i] = ' '
            
    update = True

def main(stdscr):
    
    GPIO.add_event_detect(Button1, GPIO.RISING, callback=cursorLeft)
    GPIO.add_event_detect(Button2, GPIO.RISING, callback=cursorDown)
    GPIO.add_event_detect(Button3, GPIO.RISING, callback=cursorRight)
    GPIO.add_event_detect(Button4, GPIO.RISING, callback=cursorUp)
    GPIO.add_event_detect(Button5, GPIO.RISING, callback=clearGrid)

    # Main etch-a-sketch loop
    while True:
        if (update):
            showScreen(stdscr, width, height)
        else:
            pass
       
    
def showScreen(stdscr, width, height):
    global update
    # Clear the screen
    stdscr.clear()
    
    # Print the top line
    for k in range(width):
        stdscr.addstr(0, 2 + 3*k, ' ' + str(k))
        
     # Print each grid row
    for k in range(len(grid)):
        stdscr.addstr(k+1, 0, str(k))
        for i in range(len(grid[k])):
            stdscr.addstr(k+1, 3 + i*3, str(grid[k][i]))
            
    stdscr.addstr(height+1, 0, 'Use the wired buttons to move and clear the board ')
    
    # Show the screen
    stdscr.refresh()
    update = False


# Get board dimensions
width = int(input('Enter board width: '))
height = int(input('Enter board height: '))

# Generate a random starting location
xPos = random.randint(0, width - 1)
yPos = random.randint(0, height - 1)

# Create the grid
grid = [[' ' for i in range(width)] for j in range(height)]

update = True


curses.wrapper(main)