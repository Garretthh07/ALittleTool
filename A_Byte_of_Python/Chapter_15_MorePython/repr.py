#!/usr/bin/python
# Filename: repr.py

# eval(repr(object))--object : is most of time true
mylist = []

mylist.append('item')

print `mylist`

repr_list = repr(mylist)
print repr_list

print 'Eval(repr) = ', eval(repr_list)




