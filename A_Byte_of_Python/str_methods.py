#!/usr/bin/python
# Filename: str_methods.py

name = 'Swaroopwar_This is just so so war' # This is a string object.

par = ('S', 'Sw', 'Swa')    #one string in tuple is ok, the result is true
par1 = ('Sl', 'Swl', 'Swal')
par2 = ('S', 'Swk', 'Swal')

if name.startswith(par): #methods: startswith has the optional [start, [end]]
    print 'Yes, all is start with in par <MATCH>'

if name.startswith(par1):
    print 'No, all is not start with in par1 <NOT MATCH>'

if name.startswith(par2):
    print 'Yes, just one in par2 is match'

if 'a' in name:
    print 'Yes, it contains the string "a"'

print 'Test "find(par, [start,[end])"', name.find('war') # match the min, -1 if not success

print 'The length of string is ', len(name)
print 'Test "rfind(par, [start,[end])"', name.rfind('war') # match the max, -1 if not success

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']

print delimiter.join(mylist) # join can split object in list by 'str'
