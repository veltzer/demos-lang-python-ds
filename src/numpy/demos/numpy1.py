#!/usr/bin/env python

"""
TBD
"""

import matplotlib.pyplot as plt

import numpy as np


def fadd(c: np.ndarray):
    """ simple function """
    c += 10


a = np.array([1, 4, 5, 8], float)
b = np.array([1, 2, 3, 4], float)
fadd(b)
a = a * b
print(a)
plt.plot(a, b)
plt.show()
