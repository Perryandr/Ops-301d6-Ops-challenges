#!/bash/bin

# Script: Ops 301 Class 02 Ops Challenge Solution
# Author: Andrew P.
# Date of lastest revision: 03/15/2023
# Purpose: Create a script that changes permissions of a file and directory.



# Prompts user for a directory path.
echo "Which directory do you want?"
read dir_path

# Prompts user for input permissions number to change to.

echo "Please enter the permissions number"
read perm_num

# Navigates to the directory and changes the permissions.
# Stretch goal, have it create a log of changes made
cd $dir_path
chmod -R $perm_num * > chmod_log.txt 2>&1


# Prints to screen the directory contents and new permissions of everything in directory.
cd challenges

ls -l
