#!/usr/bin/env python3

# Script: Ops 301 Class 10 Ops Challenge Solution
# Author: Andrew P.
# Date of lastest revision: 03/25/2023
# Purpose: Code Fellows requires it to pass class.

# Credit for resources and reference goes to Code academy and itsolutionstuff. 
# https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-files/cheatsheet
# https://www.itsolutionstuff.com/post/how-to-create-multiline-text-file-in-pythonexample.html


# Create a script that creates a new .txt file.

# Appends three lines,

# prints to screen the first line


# deletes the file

# Code together
import os



with open("test.txt", "w") as f:
    line1 = "Every master started their journey by taking the first step. \n"
    line2= "Let us start our journey today. \n"
    line3 = "What direction will we go?"

    f.writelines([line1, line2, line3])

    print(line1)
    
 
os.remove("test.txt")    
    
    
