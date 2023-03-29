#!/usr/bin/env python3

# Script: Ops 301 Class 10 Ops Challenge Solution
# Author: Andrew P.
# Date of lastest revision: 03/25/2023
# Purpose: Code Fellows requires it to pass class.


import requests


# Prompt the user to type a string input as the variable for your destination URL.
url = input("Enter destination URL: ")



#Prompt the user to select a HTTP Method of the following options: 
http_method = input("Enter HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
print(f"Request to {http_method} {url}")
confirmation = input("Proceed with request? (y/n): ")


# Using the requests library, perform a GET request against your lab web server.
response = requests.request(http_method, url)
print("\nResponse Headers:")

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
if response.status_code == 200:
    print("Success!")
elif response.status_code == 400:
    print("Bad request.")
elif response.status_code == 401:
    print("Unauthorized access.")
elif response.status_code == 403:
    print("Access forbidden.")
elif response.status_code == 404:
    print("Site not found.")
else:
    print(f"Unknown error ({response.status_code}).")

