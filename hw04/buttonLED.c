// From : http://stackoverflow.com/questions/13124271/driving-beaglebone-gpio-through-dev-mem
//
// Read one gpio pin and write it out to another using mmap.
// Be sure to set -O3 when compiling.
// Modified by Mark A. Yoder  26-Sept-2013
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)

//#define GPIO1_START_ADDR 0x4804C000
#define GPIO0_START_ADDR 0x44e07000
#define GPIO0_END_ADDR 0x44e09000
#define GPIO0_SIZE (GPIO0_END_ADDR - GPIO0_START_ADDR)

#define GPIO1_START_ADDR 0x4804C000
#define GPIO1_END_ADDR 0x4804e000
#define GPIO1_SIZE (GPIO1_END_ADDR - GPIO1_START_ADDR)

#define GPIO_OE 0x134
#define GPIO_DATAIN 0x138
#define GPIO_SETDATAOUT 0x194
#define GPIO_CLEARDATAOUT 0x190

#define USR0 (1<<21)
#define USR1 (1<<22)
#define USR2 (1<<23)
#define USR3 (1<<24)
#define GPIO_03  (1<<3)
#define GPIO_07  (1<<7)
#define GPIO_60  (1<<28)


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

    // Set the signal callback for Ctrl-C
    signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    printf("Mapping %X - %X (size: %X)\n", GPIO0_START_ADDR, GPIO0_END_ADDR, 
                                           GPIO0_SIZE);

    gpio_addr = mmap(0, GPIO0_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 
                        GPIO0_START_ADDR);

    gpio_oe_addr           = gpio_addr + GPIO_OE;
    gpio_datain            = gpio_addr + GPIO_DATAIN;
    gpio_setdataout_addr   = gpio_addr + GPIO_SETDATAOUT;
    gpio_cleardataout_addr = gpio_addr + GPIO_CLEARDATAOUT;

    if(gpio_addr == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }
    printf("GPIO mapped to %p\n", gpio_addr);
    printf("GPIO OE mapped to %p\n", gpio_oe_addr);
    printf("GPIO SETDATAOUTADDR mapped to %p\n", gpio_setdataout_addr);
    printf("GPIO CLEARDATAOUT mapped to %p\n", gpio_cleardataout_addr);
    
    gpio_addr2 = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
    
    gpio_oe_addr2           = gpio_addr2 + GPIO_OE;
    gpio_setdataout_addr2   = gpio_addr2 + GPIO_SETDATAOUT;
    gpio_cleardataout_addr2 = gpio_addr2 + GPIO_CLEARDATAOUT;
    
    // Set USR3 to be an output pin
    reg = *gpio_oe_addr2;
    printf("GPIO1 configuration: %X\n", reg);
    reg &= ~USR3;       // Set USR3 bit to 0
    *gpio_oe_addr2 = reg;

    printf("Start copying GPIO_07 to GPIO_03\n");
    while(keepgoing) {
    	if(*gpio_datain & GPIO_07) {
            *gpio_setdataout_addr2= USR3;
    	} else {
            *gpio_cleardataout_addr2 = USR3;
    	}
        usleep(1000);
    }

    munmap((void *)gpio_addr, GPIO0_SIZE);
    munmap((void *)gpio_addr2, GPIO1_SIZE);
    close(fd);
    return 0;
}
