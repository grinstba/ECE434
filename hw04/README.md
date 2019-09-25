# HW04  

### displayOn.sh  
This file is called by other scripts to configure the LCD display and beagle pins to the proper settings  

### displayBoris.sh  
This file displays Boris the beagle wearing a tux on the LCD display  

### displayMovie.sh  
This file displays RedsNightmare on the LCD display  

### displayName.sh  
This file displays 'Brock Grinstead' in text on the LCD display  

### displayBorisName.sh  
This file displays the text 'Brock Grinstead' over the image of Boris the beagle in a tux  

### Makefile  
This makefile will compile toggleLED.c and buttonLED.c with the appropriate flags  

### beaglebone_gpio.h  
This header file defines many GPIO addresses needed to use mmap  

### toggleLED.c  
This file toggles USR3 using mmap  

### buttonLED.c  
This file controls USR1 and USR3 using mmap and two push buttons  