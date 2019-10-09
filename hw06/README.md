# HW06 

### What Every Driver Developer Should Know about RT  
1. Where does Julia Cartwrite work?  
<em> National Instruments </em>  
2. What is PREEMPT_RT?  
<em> The RT patch makes the linux kernel into a real-time system. This means that it does what yiu want it to do when you
want it to do it. </em>  
3. What is mixed criticality?  
<em> When there are two different degrees of time-sensitivity present </em>  
4. How can drivers misbehave?  
<em> The driver stacks are shared between applications. </em>  
5. What is the delta symbol in Figure 1?  
<em> It represents latency between the actual event and when the real-time event executes. </em>  
6. What is Cyclictest[2]?  
<em> It takes a timestamps, sleeps for a short amount of time, and then takes another timestamp when it wakes up. The difference between the timestamps is then
calcualted to help find the latency. </em>  
7. What is plotted in Figure 2?  
<em> Its a histogram of the latency found in a Cyclictest </em>  
8. What is dispatch latency? Scheduling latency?  
<em> Dispatch latency is the time between the hardware firing and the relevant thread to be woken up.  
Scheduling latency is time it takes the CPU to get the task after the thread knows that it need to schedule an event. </em>  
9. What is mainline?  
<em> Mianline is non-RT way interrupts are handled. </em>  
10. What is keeping the External event in Figure 3 from starting?  
<em> A low-priority interrupt that is current executing on the CPU. </em>  
11. Why can the External event in Figure 4 start sooner?  
<em> A small 'shim' of an event is used to wake up, or preempt a new thread, even if the CPU is currently executing a low-priority interrupt. </em>  

### PREEMPT_RT  
I created three plots, one when the two kernels were not busy and two when they were. The graph showing
the results when they aren't busy is named not busy.png and the graphs showing the results when the kernels 
were under a load are named busy.png and busy2.png.  
I didn't seem to have the same results as exercise 36, however, they RT kernel seemed to bound the latency to around 60 us. 
I am basing this on the sharp inclines and declines in the busy graphs.  
For the load, I was using the Makefile in the directory at ~/exercises/linux/modules so the load involved compiling C code.