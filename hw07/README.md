# hw07  

### leds.js  
This file is the example blynk file with my authentication token in it. The Blynk app
has one button that turns on the USR3 LED when pressed. The Blynk app also has a slider that controls
an LED on P9_14. Note that the pwn analogWrite doesn't work on the 5.3 kernel.
Run the following commands to get the file working:  
> sudo npm install -g -unsafe-perm blynk-library  
> sudo mv blynk-library/ /usr/local/lib/node_modules  
> node ./leds.js  
