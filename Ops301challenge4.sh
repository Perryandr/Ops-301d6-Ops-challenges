#!/bin/bash


# Script: Ops 301 Class 02 Ops Challenge Solution
# Author: Andrew P.
# Date of lastest revision: 03/15/2023
# Purpose: Create a script that creates a menu and receives user input.






# Define a function to print the menu options
print_menu() {
    echo "Menu Options:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
}



# Print the initial menu
print_menu




# Loop until the user chooses to exit
while true; do
    # Ask for user input
    read -p "Enter an option number: " option

    # Evaluate the user's input and act accordingly
    case $option in
        1)
            echo "Hello world!"
            ;;
        2)
            ping -c 4 127.0.0.1
            ;;
        3)
            ifconfig
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid option. Please choose a valid option."
            ;;
    esac


    # Print the menu again
    print_menu
done
