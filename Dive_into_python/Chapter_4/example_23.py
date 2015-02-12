#!usr/bin/python
# Description: Why Usr str on a doc string?

def foo(): print 2

print foo()

print foo.__doc__
print foo.__doc__ == None

print str(foo.__doc__)
