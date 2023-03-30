#!/usr/bin/env python3

# Script: Ops 301 Class 11 Ops Challenge Solution
# Author: Andrew P.
# Date of lastest revision: 03/27/2023
# Purpose: Code Fellows requires it to pass class.

# Online resources used are https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps
# and https://www.manageengine.com/products/ad-manager/powershell/script-add-new-ad-user.html?utm_source=admp-how-to&utm_medium=rhs




# Set the required variables
$firstName = "Franz"
$lastName = "Ferdinand"
$displayName = "$firstName $lastName"
$office = "Springfield, OR"
$title = "TPS Reporting Lead"
$department = "TPS Department"
$email = "ferdi@GlobeXpower.com"
$username = $email.split('@')[0]

# Specify the OU where the new user will be created
$ou = "OU=Employees,DC=example,DC=com"

# Generate a secure password for the new user
$password = ConvertTo-SecureString -String "P@ssw0rd" -AsPlainText -Force

# Create a new user object and set its properties
$newUser = New-ADUser -Name $displayName -GivenName $firstName -Surname $lastName -SamAccountName $username -UserPrincipalName $email -AccountPassword $password -Office $office -Title $title -Department $department -EmailAddress $email -Enabled $true -Path $ou

# Display the new user's properties
$newUser | Format-List *
