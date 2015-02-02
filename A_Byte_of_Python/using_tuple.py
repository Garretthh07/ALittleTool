#!/usr/bin/python
# Filename: using_tuple.py

zoo = ('wolf', 'elephant', 'penguin')

print 'Number of animals in the zoo is', len(zoo)

new_zoo = ('monkey', 'dolphin', zoo)
print 'Number of animals in the new zoo is', len(new_zoo)

print 'All animals in new zoo are', new_zoo
print 'Animals brought from old zoo are', new_zoo[2]
print 'Last animals brought from old zoo id', new_zoo[2][2]

myempty = ()
print "Empty tuple = ", myempty

a = (2)

print 'a = ', a

b = (2, )  #if you want a tuple containing the item 2
print 'b = ', b
