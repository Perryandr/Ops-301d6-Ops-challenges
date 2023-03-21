#!/usr/bin/env python3

# Script: Ops 301 Class 06 Ops Challenge Solution
# Author: Andrew P.
# Date of lastest revision: 03/20/2023
# Purpose: Code Fellows requires it to pass class.


# I struggled with Bash for weeks, I probably will struggle here, its 10 pm at night and I think I am finally finishing this.

var_greeting = "Welcome to Python."

# First import the os library
import os


# Execute bash commands and store their output in variables
whoami_output = os.popen('whoami').read().strip()
ip_output = os.popen('ip a').read().strip()
lshw_output = os.popen('lshw -short').read().strip()

# I kept getting error messages when using os.system, somewhere I seen os.popen was a better alternative. 


# Print the output of the commands
print("Current user: ", whoami_output)
print("IP addresses: \n", ip_output)
print("Hardware information: \n", lshw_output)

# Aid for the assignment goes to Ethan's demo and the links posted in the ops challenge.




