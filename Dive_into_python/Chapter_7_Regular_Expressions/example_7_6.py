#!usr/bin/python
# The New Way : From n o m
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

pattern = '^M?M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)$'
print re.search(pattern, 'MCMXL')
print re.search(pattern, 'MCML')
print re.search(pattern, 'MCMLX')
print re.search(pattern, 'MCMLXXX')
print re.search(pattern, 'MCMLXXXX')
