#!/usr/bin/env python

"""
TBD
"""

import matplotlib.pyplot as plt
import scipy.stats as scs

import scipy as sc

x = scs.norm.pdf(sc.r_[-5:5:100])
plt.plot(x)
plt.show()
