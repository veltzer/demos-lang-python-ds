#!/usr/bin/env python3

import numpy
import pylab
from matplotlib import pyplot

def fadd(c):
    c+=10
 
a = numpy.array([1, 4, 5, 8], float)
b = numpy.array([1, 2, 3, 4], float)
fadd(b)
a=a*b

print(a)
pylab.plot(a,b)
pylab.show()
