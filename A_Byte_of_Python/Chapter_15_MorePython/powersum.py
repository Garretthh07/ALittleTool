#!/usr/bin/python
# Filename: powersum.py

# *: This is for tunple
# **: This is for dictionary

import math
def powersum(power, *args):
    ''' Return the sum of each argument raised to specified power.'''
    sum = 0
    for i in args:
        sum = sum + pow(i, power)
    return sum

def powersum2(power,a1, *args):
    ''' Return the sum of each argument raised to specified power.'''
    sum = 0
    for i in args:
        sum = sum + pow(i, power)
    return sum

print powersum(2, 3, 4)
print powersum(2, 10)
print powersum2(2, 2, 3, 4)
print powersum2(2,10,10)


