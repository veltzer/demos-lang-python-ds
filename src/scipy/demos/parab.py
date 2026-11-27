#!/usr/bin/env python

"""
TBD
"""

import matplotlib.pyplot as plt
import scipy.optimize as sco

import numpy as np
from numpy import dtype, float64, ndarray


def fx(x: np.ndarray):
    """ simple function """
    return 2 * (x[0] ** 2) + 10


def fx1(x: ndarray[tuple[int], dtype[float64]]):
    """ simple function """
    return 2 * (x ** 2) + 10


def main() -> None:
    """ main entry """
    x = np.linspace(-20, 20, 100)
    y1 = fx1(x)
    plt.plot(x, y1)
    fopt = sco.fmin(fx, x, full_output=True, disp=False)
    print(fopt)


if __name__ == "__main__":
    main()
