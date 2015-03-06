#!usr/bin/python
# Finding Numbers

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

phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
print phonePattern.search('800-555-1212')
print phonePattern.search('800-555-1212').groups()
print phonePattern.search('800-555-1212-1234')
