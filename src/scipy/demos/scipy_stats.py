#!/usr/bin/env python

"""
TBD
"""

import matplotlib.pyplot as plt
import scipy.stats

import numpy as np

s = np.r_

rv1 = scipy.stats.norm()
rv2 = scipy.stats.norm(2.0, 0.8)
samp = s[rv1.rvs(size=100), rv2.rvs(size=100)]
# Kernel estimate (smoothed histogram)
apdf = scipy.stats.kde.gaussian_kde(samp)
x = np.linspace(-3, 6, 200)
plt.plot(x, apdf(x), 'r')

# Histogram
# plt.hist(x*10, bins=250, normed=True)
