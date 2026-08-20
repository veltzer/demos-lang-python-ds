#!/usr/bin/env python

"""
TBD
"""

import pylab as py
import scipy.stats as scs

import scipy as sc

x = scs.norm.pdf(sc.r_[-5:5:100])
py.plot(x)
py.show()
