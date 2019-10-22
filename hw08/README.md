# hw08  

I had to change the setup.sh scripts to recognize a beaglebone model green rather than black.  

Part | Summary | Image|
|----|---------|------|
2.6 Blinking an LED | The start target has a command to start the PRU code, The stop target is run before start and will stop the PRU code from running When the delay is set to 0, there is quite a bit of jitter and the waveform seems unstable The pin was being toggled at 41.88kHz in the image, but this value fluctuated quite a bit on the scope | ![alt text](https://github.com/grinstba/ECE434/blob/master/hw08/tek00001.png)|
5.3 PWN Generator | The pwm waveform at 50 MHz is very stable. There is a standard devialtion of a few kHz, which is quite small. There is also no jitter present on the scope capture. | ![alt text](https://github.com/grinstba/ECE434/blob/master/hw08/tek00003.png)|
5.4 Controlling the PWN Frequency | P9_28, P9_29, P9_30, and P9_31 are being driven. The highest frequency we can get is 12.5 MHz. There is also still no jitter present. I couldn't get the pwm-test.c file to run since it couldn't find the <fcntl.h> header file| ![alt text](https://github.com/grinstba/ECE434/blob/master/hw08/tek00004.png)|
5.9 Reading an Input at Regular Intervals | There was no visible delay on the scope. I put a cursor over the rising and falling edges of the button that was used as input and the output pin responded on the same cursor. | ![alt text](https://github.com/grinstba/ECE434/blob/master/hw08/tek00005.png)|
