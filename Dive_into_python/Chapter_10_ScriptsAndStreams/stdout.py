#!usr/bin/env python
# Filename: stdout.py

import sys

print 'Dive in'

saveout = sys.stdout
fsock = open('out.log', 'w')

sys.stdout = fsock

print 'This message  will be logged instead of displayed'
sys.stdout = saveout
fsock.close()
