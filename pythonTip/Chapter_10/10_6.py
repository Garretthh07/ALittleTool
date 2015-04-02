#!usr/bin/env python
# http://scipy.org   for mathematics

import math

print math.cos(math.pi / 4.0)

print math.log(1024, 2)

import random

print random.choice(['apple', 'pear', 'banana'])

# sampling without replacement
print random.sample(xrange(100), 10)

# random float
print random.random()

# random integer chosen from range(6)
print random.randrange(6)

