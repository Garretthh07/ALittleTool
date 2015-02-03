#!/usr/bin/python
# Filename: backup_ver3.py
# Usage: creates a backup of all my important files
import os
import time

# 1.The files and directories to be backed up are specified in a list
source = r'E:\github_workspace\Python\A_Byte_of_Python'

#If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something

#2. The backup must be stored in a main backup directory
target_dir = 'E:\\github_workspace\\Python\\A_Byte_of_Python\\Chapter_10\\backup\\' #remember change this to what you will use

# 3.The files are backed up into a rar file.
# 4. The current day is the name of the subdiectory in the main directory
today = target_dir + time.strftime('%Y%m%d')

# The current time is the name of the rar archive
now = time.strftime('%H%M%S')

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) # make director
    print 'Successful create directory', today

# Take a comment from the user to create the name of the rar file
comment = raw_input('Enter a comment ---> ')
if len(comment) == 0: # check if a comment was entered
    target = now + '.rar'
else:
    target = now + '_' + comment.replace(' ','_') + '.rar'



# We usr the 'rar' command in Windows
rar_command  = 'rar a %s %s' % (today+os.sep, source)
rename_command = 'rename %s %s' % (today+os.sep+'.rar', target)

# Run the backup
if os.system(rar_command) == 0:
    os.system(rename_command)
    print 'Successful back to', now
else:
   print 'Backup Failure'


