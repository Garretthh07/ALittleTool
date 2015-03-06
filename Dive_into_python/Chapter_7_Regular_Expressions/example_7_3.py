#!usr/bin/python
# Checking for Thousands

import re

#pattern = '^M?M?M?$'
#print re.search(pattern, 'M')
#print re.search(pattern, 'MM')
#print re.search(pattern, 'MMM')
#print re.search(pattern, 'MMMM')
#print re.search(pattern, 'MMP')
#print re.search(pattern, '')

pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
print re.search(pattern, 'MCM')
print re.search(pattern, 'MD')
print re.search(pattern, 'MMMCCC')
print re.search(pattern, 'MCMC')
print re.search(pattern, '')

