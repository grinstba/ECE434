# HW02  

### buttons.py  
This file runs a program that uses four buttons to light up four LEDs when the buttons are pressed.  
  
### etchASketch.py  
This file runs an etch-a-sketch type program in the console. The program will ask the user to specify the heigth and width of the board.
After that the board will be displayed. An X will note where the board has been filled. Use the buttons on the board to move the cursor around
and fill the board with X's. The buttons are in a wasd setup for up, down, left, and right. The button off to the side will clear the board.  

### togglegpio.py  
This file runs a program to toggle an LED pin on and off. Pass one parameter to specify the sleep time. The program toggle gpio_117 by default in the code.  

### togglegpio.c  
How to compile:  
   > gcc -lsoc -o togglegpio togglegpio.c   

This compiled program toggles gpio_117 on and off. The delay is hard coded in microseconds. The program takes no arguments.  
