#!/usr/bin/env python3
import random
import curses

def main(stdscr):
    
    # Generate a random starting location
    xPos = random.randint(0, width - 1)
    yPos = random.randint(0, height - 1)

    # Main etch-a-sketch loop
    while True:
        showScreen(stdscr, width, height)
        pressedKey = stdscr.getch()
        
        if pressedKey == curses.KEY_UP:
            yPos-= 1
            if (yPos <= 0):
                yPos = 0
            grid[yPos][xPos] = 'X'
        elif pressedKey == curses.KEY_DOWN:
            yPos+= 1
            if (yPos >= height):
                yPos = height - 1
            grid[yPos][xPos] = 'X'
        elif pressedKey == curses.KEY_RIGHT:
            xPos+= 1
            if (xPos >= width):
                xPos = width - 1
            grid[yPos][xPos] = 'X'
        elif pressedKey == curses.KEY_LEFT:
            xPos-= 1
            if (xPos <= 0):
                xPos = 0
            grid[yPos][xPos] = 'X'
        elif pressedKey == ord(' '):
            for k in range(len(grid)):
                for i in range(len(grid[k])):
                    grid[k][i] = ' '
    
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
            
    stdscr.addstr(height+1, 0, 'Enter command (up, down, left, right, clear): ')
    
    # Show the screen
    stdscr.refresh()


# Get board dimensions
width = int(input('Enter board width: '))
height = int(input('Enter board height: '))

# Create the grid
grid = [[' ' for i in range(width)] for j in range(height)]


curses.wrapper(main)