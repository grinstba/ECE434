#!/usr/bin/env python3
import random
import curses

def cursorUp():
    global xPos, yPos
    yPos-= 1
    if (yPos <= 0):
        yPos = 0
    grid[yPos][xPos] = 'X'
    
def cursorDown():
    global xPos, yPos
    yPos+= 1
    if (yPos >= height):
        yPos = height - 1
    grid[yPos][xPos] = 'X'
    
def cursorRight():
    global xPos, yPos
    xPos+= 1
    if (xPos >= width):
        xPos = width - 1
    grid[yPos][xPos] = 'X'
    
def cursorLeft():
    global xPos, yPos
    xPos-= 1
    if (xPos <= 0):
        xPos = 0
    grid[yPos][xPos] = 'X'
    
def clearGrid():
    for k in range(len(grid)):
        for i in range(len(grid[k])):
            grid[k][i] = ' '

def main(stdscr):

    # Main etch-a-sketch loop
    while True:
        showScreen(stdscr, width, height)
        pressedKey = stdscr.getch()
        
        if pressedKey == curses.KEY_UP:
            cursorUp()
        elif pressedKey == curses.KEY_DOWN:
           cursorDown()
        elif pressedKey == curses.KEY_RIGHT:
            cursorRight()
        elif pressedKey == curses.KEY_LEFT:
            cursorLeft()
        elif pressedKey == ord(' '):
            clearGrid()
    
def showScreen(stdscr, width, height):
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
            
    stdscr.addstr(height+1, 0, 'Use arrow keys to move and space bar to clear the board ')
    stdscr.addstr(height+2, 0, 'Or use the wired buttons to move and clear the board ')
    
    # Show the screen
    stdscr.refresh()


# Get board dimensions
width = int(input('Enter board width: '))
height = int(input('Enter board height: '))

# Generate a random starting location
xPos = random.randint(0, width - 1)
yPos = random.randint(0, height - 1)

# Create the grid
grid = [[' ' for i in range(width)] for j in range(height)]


curses.wrapper(main)