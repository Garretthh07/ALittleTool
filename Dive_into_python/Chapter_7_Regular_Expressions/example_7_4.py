#!usr/bin/python
# Checking for Hundreds
import re

# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

# Checking for Hundreds
# 100 = C
# 200 = CC
# 300 = CCC
# 400 = CD
# 500 = D
# 600 = DC
# 700 = DCC
# 800 = DCCC
# 900 = CM

pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
print re.search(pattern, 'MCM')
print re.search(pattern, 'MD')
print re.search(pattern, 'MMMCCC')
print re.search(pattern, 'MCMC')
print re.search(pattern, '')

