#!usr/bin/python
# Filename: list_searching.py

li = ['a','b','new','mpilgrim','z','example','new','two','elements']

print li.index("example")

print li.index("new")

# print li.index("c")


# 0, "", [], (), {}  is false
print "c" in li

print "Example 3.13: Removing Elements from a List ----> "
print "Source --->", li
li.remove("z")

print li

li.remove("new")
print li

# li.remove("c")

print li.pop()
print li


