#!/usr/bin/env python3

"""
This desmo shows how much regular python consumes
"""

import sys
import resource
import random


def create_array():
    """ create an array """
    arr = []
    for _ in range(1000000):
        arr.append(random.randint(1, 1000000))
    return arr


a = create_array()
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print(sys.getsizeof(a))
input("press any key...")
