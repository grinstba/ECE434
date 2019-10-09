# HW06 

### What Every Driver Developer Should Know about RT  
1. Where does Julia Cartwrite work?
2. What is PREEMPT_RT?
3. What is mixed criticality?
4. How can drivers misbehave?
5. What is the delta symbol in Figure 1?
6. What is Cyclictest[2]?
7. What is plotted in Figure 2?
8. What is dispatch latency? Scheduling latency?
9. What is mainline?
10. What is keeping the External event in Figure 3 from starting?
11. Why can the External event in Figure 4 start sooner?

### PREEMPT_RT  
I created three plots, one when the two kernels were not busy and two when they were. The graph showing
the results when they aren't busy is named not busy.png and the graphs showing the results when the kernels 
were under a load are named busy.png and busy2.png.  
I didn't seem to have the same results as exercise 36, however, they RT kernel seemed to bound the latency to around 60 us. 
I am basing this on the sharp inclines and declines in the busy graphs.  
For the load, I was using the Makefile in the directory at ~/exercises/linux/modules so the load involved compiling C code.