#!usr/bin/python
# Filename: example_6_7.py

logfile = open('test.log', 'w')

logfile.write('test successed')

logfile.close()
print file('test.log').read()

logfile = open('test.log', 'a')
logfile.write('line 2')

logfile.close()
print file('test.log').read()
