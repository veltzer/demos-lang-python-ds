#!/usr/bin/env python3

"""
This example shows that numpy can solve linear equation sets
"""

import numpy

A = numpy.array([[1,2],[3,4]])
B = numpy.array([3,0])
X = numpy.linalg.solve(A, B)

# Verify the solution by multiplying A and x
result = numpy.dot(A, X)

print("A * X =", result)
print("B =", B)

if numpy.allclose(result, B):
    print("The solution is correct!")
else:
    print("The solution is incorrect.")
