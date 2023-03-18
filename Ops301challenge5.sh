#!/bin/bash


# Script: Ops 301 Class 05 Ops Challenge Solution
# Author: Andrew P.
# Date of lastest revision: 03/17/2023
# Purpose: Create a script that backs up and zips a file. Add a time stamp to it.


# Print the file size of the log files before compression
echo "File size of log files before compression:"
du -h /var/log/syslog /var/log/wtmp

# Create a backup directory if it doesn't exist
backup_dir="/var/log/backups"
if [ ! -d "$backup_dir" ]; then
  mkdir "$backup_dir"
fi

# Compress the contents of the log files to the backup directory
timestamp=$(date +%Y%m%d%H%M%S)
zip_file_syslog="$backup_dir/syslog-$timestamp.zip"
zip_file_wtmp="$backup_dir/wtmp-$timestamp.zip"

zip -r "$zip_file_syslog" /var/log/syslog
zip -r "$zip_file_wtmp" /var/log/wtmp

# Clear the contents of the log file
> /var/log/syslog
> /var/log/wtmp

# Print the file size of the compressed file
echo "File size of compressed files:"
du -h "$zip_file_syslog" "$zip_file_wtmp"

# Compare the size of the compressed files to the size of the original log files
echo "Comparison of file sizes:"
du -h /var/log/syslog /var/log/wtmp "$zip_file_syslog" "$zip_file_wtmp"
