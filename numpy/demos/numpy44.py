#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 22:23:54 2017

@author: liran
"""

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

