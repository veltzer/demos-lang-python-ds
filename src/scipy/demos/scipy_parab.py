#!/usr/bin/env python3

"""
TBD
"""

import pylab as py
import scipy as sc
import numpy as np


def fx(x):
    """ simple function """
    return 2*(x[0]**2) + 10


def fx1(x):
    """ simple function """
    return 2*(x**2) + 10


def main():
    """ main entry """
    x = np.linspace(-20, 20, 100)
    y1 = fx1(x)
    py.plot(x, y1)
    fopt = sc.optimize.fmin(fx, x, full_output=True, disp=False)
    print(fopt[1])


if __name__ == "__main__":
    main()
