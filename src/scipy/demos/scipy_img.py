#!/usr/bin/env python

"""
TBD
"""

import matplotlib.pyplot as plt
import scipy.signal as ssig

img = plt.imread("python.png")

# plt.imshow(img)  # noqa: ERA001  teaching: kept in the comment for the reader

img = ssig.medfilt(img)

plt.imshow(img)
