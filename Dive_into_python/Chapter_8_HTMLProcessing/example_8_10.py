#!usr/bin/python
# Introducing locals

def foo(arg):
    x = 1
    print locals()

foo(7)

foo('bar')
