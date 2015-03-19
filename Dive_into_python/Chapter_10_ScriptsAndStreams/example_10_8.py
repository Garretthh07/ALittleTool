#!usr/bin/env python
# Introducing stdout and stderr

for i in range(3):
    print 'Dive in'

import sys
for i in range(3):
    sys.stdout.write('Dive in')

for i in range(3):
    sys.stderr.write('Dive in')
