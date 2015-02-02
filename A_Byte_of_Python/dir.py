#!usr/bin/python
# Filename: dir.py

import sys

print dir(sys)
print dir()

a = 5
print dir()
del a
print dir()
