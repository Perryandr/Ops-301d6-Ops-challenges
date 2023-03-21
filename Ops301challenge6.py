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
who = os.popen('whoami')
ip = os.popen('ip a')
lshw = os.popen('lshw -short')

# I kept getting error messages when using os.system, somewhere I seen os.popen was a better alternative. 


# Print the output of the commands
print("Current user: ", who)
print("IP addresses: \n", ip)
print("Hardware information: \n", lshw)

# Aid for the assignment goes to Ethan's demo and the links posted in the ops challenge.




