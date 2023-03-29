#!/usr/bin/env python3

# Script: Ops 301 Class 11 Ops Challenge Solution
# Author: Andrew P.
# Date of lastest revision: 03/27/2023
# Purpose: Code Fellows requires it to pass class.


# Credit for information goes to Code Fellows Github page assigned for class 301d6 and https://www.geeksforgeeks.org/psutil-module-in-python/.




import psutil




# Time spent by normal processes executing in user mode
print("Time spent by normal processes executing in user mode:", cpu_times.user)


# Time spent by processes executing in kernel mode
print(cpu_times.system)

# Time when system was idle
print(cpu_times.idle)


# Time spent by priority processes executing in user mode
print(cpu_times.nice)

# Time spent waiting for I/O to complete.
print(cpu_times.iowait)


# Time spent for servicing hardware interrupts
print(cpu_times.irq)

# Time spent for servicing software interrupts
print(cpu_times.softirq)

# Time spent by other operating systems running in a virtualized environment
  print(cpu_times.steal)
  
# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
print(pu_times.guest)





