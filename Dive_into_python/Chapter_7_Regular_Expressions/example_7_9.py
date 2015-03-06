#!usr/bin/python
# Regular Expressions with Inline Comments
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

pattern = """
    ^                 # beginning of string
    M{0,4}            # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})  # hundreds - 900 (CM) 400 (CD) ,0-300 (0 to 3 C's),
                      #          or 500-800 (D, folowed by 0 to 3 C's)
    (XC|XL|L?X{0,3})  # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                      #         or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})  # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                      #          or 5-8 (V, followed by 0 to 3 I's)
    $                 # end of string
    """

print re.search(pattern, 'M',  re.VERBOSE)
print re.search(pattern, 'MCMLXXXIX',  re.VERBOSE)
print re.search(pattern, 'MMMMDCCCLXXXVIII',  re.VERBOSE)
print re.search(pattern, 'M')
