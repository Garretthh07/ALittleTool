#!usr/bin/python
# Handling Numbers Without Separators

import re

# 800 - 555 - 1212
# 800 555 1212
# 800.555.1212
# (800) 555-1212
# 1-800-555-1212
# 800-555-1212-1234
# 800-555-1212x1234
# 800-555-1212 ext. 1234
# work 1-(800) 555.1212 #1234

phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print phonePattern.search('80055512121234').groups()
print phonePattern.search('800.555.1212.x1234').groups()
print phonePattern.search('800-555-1212').groups()
print phonePattern.search('(800)5551212 x1234')
