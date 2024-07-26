#!/usr/bin/env python

"""
TBD
"""

import scipy.optimize as scop
import numpy as np


def nonlin(x, a, b, c):
    """ non linear function """
    x0, x1, x2 = x
    print(x)
    return [3 * x0 - np.cos(x1 * x2) + a,
            x0 * x0 - 81 * (x1 + 0.1) ** 2 + np.sin(x2) + b,
            np.exp(-x0 * x1)+20 * x2 + c]


def main():
    """ main function """
    a, b, c = -0.5, 1.06, (10 * np.pi - 3.0) / 3
    root = scop.fsolve(nonlin, [0.1, 0.1, -0.1], args=(a, b, c))
    print(root)
    print(nonlin(root, a, b, c))


if __name__ == "__main__":
    main()
