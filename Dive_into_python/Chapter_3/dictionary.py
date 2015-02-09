#!usr/bin/python
# Filename: dictionary.py

d = {"server":"mpilgrim", "database":"master"}

print d

print d["server"]

print d["database"]

# print d["mpilgrim"]

# Example 3.2: Modify  a Dictionary
d["database"] = "pubs"
print d

d["uid"] = "sa"
print d
