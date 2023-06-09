#!/usr/bin/env python3

# Script: Ops 301 Class 09 Ops Challenge Solution
# Author: Andrew P.
# Date of lastest revision: 03/24/2023
# Purpose: Code Fellows requires it to pass class.

# Credit for resources and reference goes to Code academy and itsolutionstuff. 
# https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-files/cheatsheet
# https://www.itsolutionstuff.com/post/how-to-create-multiline-text-file-in-pythonexample.html

# Create if an statement using a==b or not equals a!=b
a = 1
b = 2

if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")

# Create an if statement using using logical conditions.
a = 1 
b = 1

if a != b:
    print("a is not equal to b")
else:
    print("a is equal to b")


# Create an if statement that has elif and else.
a = 15
b = 20

if a >= b:
    print("a is greater than or equal to b")
elif a < b:
    print("a is less than b")
else:
    print("This statement should not be reached")
