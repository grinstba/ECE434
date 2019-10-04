# HW05  

### Makefile  
This file is used to easily compile and link C files. This file was created as per Exercise 15 on the elinux website.  

### a.out Results on BeagleBone  
> debian@beaglebone:~$ ./a.out  
> Hello, World! Main is executing at 0x44a5ad  
> This address (0xbec25b78) is in our stack frame  
> This address (0x45b010) is in our bss section  
> This address (0x45b008) is in our data section  

### a.out Results on Host  
> grinstba@ubuntu:~/Desktop/exercises$ ./a.out  
> Hello, World! Main is executing at 0x55a07d8d86aa  
> This address (0x7ffca7e38980) is in our stack frame  
> This address (0x55a07dad9018) is in our bss section  
> This address (0x55a07dad9010) is in our data section  

### Minimal Device Driver  
This folder contains all of the files necessary for part one of the kernel modules homework.  
Run the following commands to ensure that the kernel module is working. Note that you can also pass 
parameters to the kernel module and its print statement will change.  
> make  
> sudo insmod hello.ko  
> sudo rmmod hello.ko  
> dmesg -H | tail -2  

### aCharacterDevice  
This foler contains all of the files necessary for part two of the kernel modules homework.  
Run the following commands to ensure that the module is working. Note that the test will ask for 
some user input and the module will function depending on that input.  
> make  
> sudo insmod ebbchar.ko  
> dmesg -H | tail -4  
> ./test  
> dmesg -H | tail -8  

### KernelGPIO  
This folder contains all the files necessary for part three of the kernel modules homework. 
Run the following commands to ensure that the module is working.  
> make  
> sudo insmof gpio_test.ko  
> tail -f /var/log/kern.log  