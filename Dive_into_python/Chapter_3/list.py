#!usr/bin/python
# Filename: list.py

li = ["a", "b", "mpilgrim", "z", "example"]

print li

print li[0]

print li[4]

#Example 3.7: Negative List Indices
print li[-1] #the last element

print li[-3] #li[-n]==li[len(li)-n]

#Example 3.8:Slicing a List
print li[1:3]

print li[1:-1]

print li[0:3]

#Example 3.9:Slicing Shorthand
print "Example 3.9 ---------->"
print li[:3]

print li[3:]

print li[:]

#Example 3.10: Adding Elements to a List
print "Example 3.10 -------->"

li.append("new")
print li

li.insert(2, "new")
print li

li.extend(["two", "elements"])
print li
