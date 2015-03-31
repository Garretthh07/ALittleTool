#!usr/bin/env python
# Skill for loop

# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
#
# print "Test method of iteritems()"
# for k, v in knights.items():
#     print (k, v)
#
#
# print "print the index, and values"
# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print (i, v)
#
# print "Operation zip for two or more list"
# queations = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
#
# for q, a in zip(queations, answers):
#     print('What is your {0}? It is {1}.'.format(q, a))

print "Test function reversed"
for i in reversed(range(1, 10, 2)):
    print(i)

print "Test method sorted"
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print "Origin List of <basket> = ", basket
for f in sorted(set(basket)):
    print(f)
print "After sorted List of <basket> = ", basket

