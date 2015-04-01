#!usr/bin/env python

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print x.r, x.i

x.a = 10
print x, x.a, x.r, x.i
