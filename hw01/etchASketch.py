#!/usr/bin/env python3
import random

width = int(input('Enter board width: '))
height = int(input('Enter board height: '))

grid = [[' ' for i in range(width)] for j in range(height)]

    
xPos = random.randint(0, width - 1)
yPos = random.randint(0, height - 1)


while (True):
    print('  ', end='')
    for z in range(len(grid[0])):
        print(' ' + str(z), end='')
    
    print('')
    
    for k in range(len(grid)):
        print(str(k) + ':', end='')
        for i in range(len(grid[k])):
            print(' ' + str(grid[k][i]), end='')
    
        print('')
        
    command = input('Enter command (up, down, left, rigth, clear): ')
    
    if (command == 'down'):
        xPos+= 1
        if (xPos >= width):
            xPos = width - 1
        grid[xPos][yPos] = 'X'
    elif (command == 'up'):
        xPos-= 1
        if (xPos <= 0):
            xPos = 0
        grid[xPos][yPos] = 'X'
    elif (command == 'right'):
        yPos+= 1
        if (yPos >= height):
            yPos = height - 1
        grid[xPos][yPos] = 'X'
    elif (command == 'left'):
        yPos-= 1
        if (yPos <= 0):
            yPos = 0
        grid[xPos][yPos] = 'X'
    elif (command == 'clear'):
        for k in range(len(grid)):
            for i in range(len(grid[k])):
                grid[k][i] = ' '
    else:
        print('Invalid Command')