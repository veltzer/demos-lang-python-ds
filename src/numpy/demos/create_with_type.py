#!/usr/bin/env python3

"""
This is the way to forced numpy to create an array with a specific type

NumPy supports a wide range of data types, including:

    Integer types: int8, int16, int32, int64
    Floating-point types: float16, float32, float64
    Boolean type: bool
    String type: str
    Complex types: complex64, complex128
"""

import numpy

arr = numpy.array([1, 2, 3, 4, 5], dtype=numpy.float64)

# conversion to string in formatted strings work
print(f"arr = {arr}")
print(arr)
print(arr.shape)
print(arr.dtype)
