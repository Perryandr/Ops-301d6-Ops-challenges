#!/bin/bash


# Script: Ops 301 Class 02 Ops Challenge Solution
# Author: Andrew P.
# Date of lastest revision: 03/14/2023
# Purpose: Create a script that time stamps the log generation. 

# Define the source file and target directory
source_file="C:\Users\deadl\Desktop\Writing projects"
target_dir="C:\Users\deadl\Desktop\logs"


# Create the target filename with date and time appended
timestamp=$(date +%Y-%m-%d_%H-%M-%S)
target_file="${target_dir}/syslog_${timestamp}.log"

# Print message indicating it was a success
echo "Copied $source_file to $target_file."
