all:	toggleLED buttonLED

toggleLED: toggleLED.c beaglebone_gpio.h
	cc -O3 -g -o toggleLED toggleLED.c

buttonLED:  buttonLED.c beaglebone_gpio.h
	cc -O3 -g -o buttonLED buttonLED.c

clean:
	rm toggleLED buttonLED