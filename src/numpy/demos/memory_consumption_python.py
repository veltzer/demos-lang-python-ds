#!/usr/bin/env python3

"""
"""

import resource
import sys
import random

def create_array():
    l = []
    for i in range(1000000):
        l.append(random.randint(1, 1000000))
    return l

a = create_array()
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print(sys.getsizeof(a))
input("press any key...")
