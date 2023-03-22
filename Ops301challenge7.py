#!/usr/bin/env python3

# Script: Ops 301 Class 06 Ops Challenge Solution
# Author: Andrew P.
# Date of lastest revision: 03/21/2023
# Purpose: Code Fellows requires it to pass class.

import os

def generate_directory_structure(user_path):
    for dirpath, dirnames, filenames in os.walk(user_path):
        print(f"Directory Path: {dirpath}")
        print(f"Directories: {dirnames}")
        print(f"Files: {filenames}\n")

user_input = input("Enter a directory path: ")
generate_directory_structure(user_input)


