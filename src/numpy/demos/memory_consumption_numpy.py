#!/usr/bin/env python

"""
This is a demo to show how much memory numpy consumes.
"""

import sys
import resource
import numpy


def create_array():
    """ create a large array """
    arr = numpy.random.randint(1, 1000000, 10000000)
    print(f"arr = {arr}")
    print(arr)
    print(arr.shape)
    print(arr.dtype)
    return arr


a = create_array()
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print(sys.getsizeof(a))
input("press any key...")
