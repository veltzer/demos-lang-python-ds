#!/usr/bin/env python

"""
TBD
"""

import matplotlib.pyplot as plt
import scipy.signal as ssig

img = plt.imread("python.png")

# plt.imshow(img)

img = ssig.medfilt(img)

plt.imshow(img)
