#!/usr/bin/env python3

"""
TBD
"""

import scipy.signal as ssig
import matplotlib.pyplot as plt

img = plt.imread("python.png")

#plt.imshow(img)

img = ssig.medfilt(img)

plt.imshow(img)
