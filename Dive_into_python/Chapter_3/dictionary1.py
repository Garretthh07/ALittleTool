#!usr/bin/python
# Filename: dictionary1.py

d = {}

d["key"] = "value"
d["key"] = "other value"

print d

d["Key"] = "third value"

print d

#Example 3.4: Mixing Datatypes in a Dictionary

d["retrycount"] = 3
print d

d[42] = "douglas"
print d

#Example 3.5: Deleting Items from a Dictionary

del d[42]
print d

d.clear()
print d
