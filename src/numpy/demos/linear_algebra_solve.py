#!/usr/bin/env python

"""
This example shows that numpy can solve linear equation sets
"""

import numpy as np

A = np.array([[1, 2], [3, 4]], dtype=np.float64)
B = np.array([3, 0], dtype=np.float64)
X = np.linalg.solve(A, B)

# Verify the solution by multiplying A and x
result = np.dot(A, X)

print("A*X = ", result)
print("B = ", B)

if np.allclose(result, B):
    print("The solution is correct!")
else:
    print("The solution is incorrect.")
