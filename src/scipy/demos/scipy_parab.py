#!/usr/bin/env python

"""
TBD
"""

import matplotlib.pyplot as plt

import numpy as np
import scipy as sc
from numpy import dtype, float64, ndarray


def fx(x: np.ndarray):
    """ simple function """
    return 2*(x[0]**2) + 10


def fx1(x: ndarray[tuple[int], dtype[float64]]):
    """ simple function """
    return 2*(x**2) + 10


def main() -> None:
    """ main entry """
    x = np.linspace(-20, 20, 100)
    y1 = fx1(x)
    plt.plot(x, y1)
    fopt = sc.optimize.fmin(fx, x, full_output=True, disp=False)
    print(fopt[1])


if __name__ == "__main__":
    main()
