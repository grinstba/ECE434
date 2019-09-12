#!/usr/bin/env python3
import random

# Get board dimensions
width = int(input('Enter board width: '))
height = int(input('Enter board height: '))

# Create the grid
grid = [[' ' for i in range(width)] for j in range(height)]

# Generate a random starting location
xPos = random.randint(0, width - 1)
yPos = random.randint(0, height - 1)

# Main loop to use the etch-a-sketch
while (True):
    # Print the top line
    print('  ', end='')
    for z in range(len(grid[0])):
        print(' ' + str(z), end='')
    
    print('')
    
    # Print each grid row
    for k in range(len(grid)):
        print(str(k) + ':', end='')
        for i in range(len(grid[k])):
            print(' ' + str(grid[k][i]), end='')
    
        print('')
        
    # Ask for a user command
    command = input('Enter command (up, down, left, right, clear): ')
    
    if (command == 'right'):
        xPos+= 1
        if (xPos >= width):
            xPos = width - 1
        grid[yPos][xPos] = 'X'
    elif (command == 'left'):
        xPos-= 1
        if (xPos <= 0):
            xPos = 0
        grid[yPos][xPos] = 'X'
    elif (command == 'down'):
        yPos+= 1
        if (yPos >= height):
            yPos = height - 1
        grid[yPos][xPos] = 'X'
    elif (command == 'up'):
        yPos-= 1
        if (yPos <= 0):
            yPos = 0
        grid[yPos][xPos] = 'X'
    elif (command == 'clear'):
        for k in range(len(grid)):
            for i in range(len(grid[k])):
                grid[k][i] = ' '
    else:
        print('Invalid Command')