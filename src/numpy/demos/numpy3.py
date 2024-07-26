#!/usr/bin/env python

"""
TBD
"""

import numpy as np

a = np.array([[0, 4, 5, 8, 10, 12],
              [1, 4, 5, 8, 10, 12],
              [1, 4, 5, 8, 10, 12],
              [1, 4, 5, 8, 10, 12],
              [1, 4, 5, 8, 10, 12],
              [1, 4, 5, 8, 10, 12]], 'i8')
b = a.view('i4')
d = [hex(val.item()) for val in b.flat]
print(d)
dt = np.dtype("i4,f8,a5")
print(dt.fields)
a = np.array([(1, 2.0, "Hello"), (2, 3.0, "World")], dtype=dt)
print(a['f2'])
