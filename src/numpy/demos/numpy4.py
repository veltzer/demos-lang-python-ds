#!/usr/bin/env python3

import numpy as np


def fn1(x,num):
    return x*2 + num

a=np.arange(10)
print (a)

a2 = fn1(a,100)
print (a2)

vfn = np.vectorize(fn1)
b = vfn([9,3,94],200)
print (b)

