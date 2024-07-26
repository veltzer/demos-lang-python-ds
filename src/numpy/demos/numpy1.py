#!/usr/bin/env python

"""
TBD
"""

import pylab
import numpy


def fadd(c):
    """ simple function """
    c += 10


a = numpy.array([1, 4, 5, 8], float)
b = numpy.array([1, 2, 3, 4], float)
fadd(b)
a = a * b
print(a)
pylab.plot(a, b)
pylab.show()
