#!usr/bin/env python
#Filename: for.py

# Measure some strings

a = ['cat', 'window', 'defenestrate']

for x in a:
    print(x, len(x))

for x in a[:]: # make a slice copy of the entire list
    if len(x) > 6: a.insert(0, x)

print a
