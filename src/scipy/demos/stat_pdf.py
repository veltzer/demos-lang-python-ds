#!/usr/bin/env python

"""
TBD
"""

import matplotlib.pyplot as plt
import scipy.stats as scs

import numpy as np

x = scs.norm.pdf(np.r_[-5:5:100])
plt.plot(x)
plt.show()
