#!/usr/bin/env python

"""
TBD
"""

import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

s = np.r_

rv1 = stats.norm()
rv2 = stats.norm(2.0, 0.8)
samp = s[rv1.rvs(size=100), rv2.rvs(size=100)]
# Kernel estimate (smoothed histogram)
apdf = stats.kde.gaussian_kde(samp)
x = np.linspace(-3, 6, 200)
plt.plot(x, apdf(x), 'r')

# Histogram
# plt.hist(x*10, bins=250, normed=True)
