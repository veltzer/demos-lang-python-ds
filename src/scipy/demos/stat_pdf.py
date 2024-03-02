#!/usr/bin/env python3

import scipy as sc
import scipy.stats as scs
import pylab as py

x= scs.norm.pdf(sc.r_[-5:5:100j])
py.plot(x)
py.show()
