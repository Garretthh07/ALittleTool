#!/usr/bin/python
# Filename: os.py

import os

# os.name: 'nt' for Windows, 'posix' for Linux/Unix
print 'The OS name = ', os.name

# os.getcwd(): gets the current working directory
print 'The current working directory = ', os.getcwd()

# os.getenv(): get the environment
# os.putenv(): set the environment
# print 'The environment is = ', os.getenv()

source = r'E:\github_workspace\Python\A_Byte_of_Python\Chapter_14_PythonStandardLibrary'

# os.listdir(): return the name  of all file and directories in the directory
print 'The os.listdir() = ', os.listdir(source)

# os.remove(): delete a file
# os.system(): run a shell command

# os.linesep: give the line terminator used in the current platform
print 'The os.linesep = ', os.linesep

# os.path.split(): return the directory name and file name of the path
source = r'E:\github_workspace\Python\A_Byte_of_Python\Chapter_14_PythonStandardLibrary\poem.vim'
print 'The os.path.split = ', os.path.split(source)

# os.path.isfile() : check the give path is a file
# source = r'E:\github_workspace\Python\A_Byte_of_Python\Chapter_14_PythonStandardLibrary'
print 'The os.path.isfile = ', os.path.isfile(source)


# os.path.isdir() : check the give path is a directory
source = r'E:\github_workspace\Python\A_Byte_of_Python\Chapter_14_PythonStandardLibrary'
print 'The os.path.isdir = ', os.path.isdir(source)

# os.path.exists() : check the give path is a exist
source = r'E:\github_workspace\Python\A_Byte_of_Python\Chapter_14_PythonStandardLibrary'
print 'The os.path.exists = ', os.path.exists(source)
