#!usr/bin/env python
# Set Operation : union, intersection, difference, sysmmetric difference

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket) # show that duplicates have been removed

print 'orange' in basket   # fast membership testing

print 'crabgrass' in basket

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')

print 'unique letters in a ', a
print 'unique letters in b ', b

print 'letters in a but not in b', a - b

print  'letters in either a or b',a | b

print 'letters in both a and b', a & b

print 'letters in a or b but not both', a ^ b
