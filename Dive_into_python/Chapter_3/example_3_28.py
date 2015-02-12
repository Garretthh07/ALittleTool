#!usr/bin/python
# Description: Spliting a String

li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)

print s

print s.split(";")

print s.split(";", 1)
