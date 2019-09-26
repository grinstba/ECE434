// From : http://stackoverflow.com/questions/13124271/driving-beaglebone-gpio-through-dev-mem
// Modified by Mark A. Yoder  26-Sept-2013
// Modified by Brock Grinstead 25-Sept-2019
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include "beaglebone_gpio.h"


/****************************************************************
 * Global variables
 ****************************************************************/
int keepgoing = 1;    // Set to 0 when ctrl-c is pressed

/****************************************************************
 * signal_handler
 ****************************************************************/
void signal_handler(int sig);
// Callback called when SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
    printf( "\nCtrl-C pressed, cleaning up and exiting...\n" );
	keepgoing = 0;
}

int main(int argc, char *argv[]) {
    volatile void *gpio_addr;
    volatile void *gpio_addr2;
    volatile unsigned int *gpio_oe_addr;
    volatile unsigned int *gpio_oe_addr2;
    volatile unsigned int *gpio_datain;
    volatile unsigned int *gpio_setdataout_addr;
    volatile unsigned int *gpio_setdataout_addr2;
    volatile unsigned int *gpio_cleardataout_addr;
    volatile unsigned int *gpio_cleardataout_addr2;
    unsigned int reg;
    unsigned int reg2;
    
    // Config P9_11 to be GPIO
    system("config-pin P9_11 gpio");

    // Set the signal callback for Ctrl-C
    signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);
    
    
    // map address1
    gpio_addr = mmap(0, GPIO0_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 
                        GPIO0_START_ADDR);

    gpio_oe_addr           = gpio_addr + GPIO_OE;
    gpio_datain            = gpio_addr + GPIO_DATAIN;
    gpio_setdataout_addr   = gpio_addr + GPIO_SETDATAOUT;
    gpio_cleardataout_addr = gpio_addr + GPIO_CLEARDATAOUT;

    if(gpio_addr == MAP_FAILED) {
        printf("Unable to map address1\n");
        exit(1);
    }
    
    // map address2
    gpio_addr2 = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
    
    gpio_oe_addr2           = gpio_addr2 + GPIO_OE;
    gpio_setdataout_addr2   = gpio_addr2 + GPIO_SETDATAOUT;
    gpio_cleardataout_addr2 = gpio_addr2 + GPIO_CLEARDATAOUT;
    
    if(gpio_addr2 == MAP_FAILED) {
        printf("Unable to map address2\n");
        exit(1);
    }
    
    // Set USR3 to be an output pin
    reg = *gpio_oe_addr2;
    reg &= ~USR3;       // Set USR3 bit to 0
    *gpio_oe_addr2 = reg;
    
    // Set USR1 to be an output pin
    reg2 = *gpio_oe_addr2;
    reg2 &= ~USR1;       // Set USR1 bit to 0
    *gpio_oe_addr2 = reg2;
    
    
    while(keepgoing) {
    	if(*gpio_datain & GPIO_07) {
            *gpio_setdataout_addr2= USR3;
    	} 
    	else if (*gpio_datain & GPIO_30){
    	    *gpio_setdataout_addr2= USR1;
    	} 
    	else {
            *gpio_cleardataout_addr2 = USR3;
            *gpio_cleardataout_addr2 = USR1;
    	}
        usleep(1000);
    }

    munmap((void *)gpio_addr, GPIO0_SIZE);
    munmap((void *)gpio_addr2, GPIO1_SIZE);
    close(fd);
    return 0;
}
