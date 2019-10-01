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

