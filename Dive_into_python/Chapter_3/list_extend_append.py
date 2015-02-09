#!usr/bin/python
#Filename: list_extend_append.py

li = ['a', 'b', 'c']
li.extend(['d', 'e', 'f'])

print li
print "Extend: The length of list ", len(li), li[-1]

li = ['a', 'b', 'c']
li.append(['d', 'e', 'f'])

print li
print "Append: The length of list ", len(li), li[-1]
