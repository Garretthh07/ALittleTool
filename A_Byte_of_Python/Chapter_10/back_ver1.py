#!/usr/bin/python
# Filename: backup_ver1.py
# Usage: creates a backup of all my important files
import os
import time

# 1.The files and directories to be backed up are specified in a list
source = r'E:\github_workspace\Python\A_Byte_of_Python'

#If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something

#2. The backup must be stored in a main backup directory
target_dir = 'E:\\github_workspace\\Python\\A_Byte_of_Python\\Chapter_10\\backup\\' #remember change this to what you will use

#3. The files are backed up into a 'rar' file
#4. The name of the zip  archive is the current date and time
target = time.strftime('%Y%m%d%H%M%S') + '.rar'

rar_command = "rar a %s %s" % (target_dir, source)

target_file = target_dir + '.rar'
rename_command = "rename %s %s" % (target_file, target)

#Run the backup
if os.system(rar_command) == 0:
    os.system(rename_command)
    print 'Successful backup to ', target
else:
    print 'Backup FAILED'
