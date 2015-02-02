#!/usr/bin/python
# Filename: using_dict.py

# 'ab' id short for 'a'ddress 'b'ook

ab = { 'Swaroop': 'swaroop@byteofpython.info',
        'Larry' : 'larry@wall.org',
        'Matsumoto': 'matz@ruby-lang.org',
        'Spammer': 'spammer@hotmail.com'
        }

print "Swaroop's address is %s" % ab['Swaroop']

# Adding a key/value pair
ab['Guido'] = 'guido@python.org'

# Deleting a key/values pair
del ab['Spammer']

print '\nThere are %d contacts in the address-book\n' % len(ab)
