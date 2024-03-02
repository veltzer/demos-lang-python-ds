#!/usr/bin/env python3

"""
TBD
"""

from pylab import axis, legend
from scipy.interpolate import interp1d
import numpy

# sample values
x = numpy.linspace(0,2*numpy.pi,6)
y = numpy.sin(x)


spline_fit = interp1d(x,y,kind=5)
xx = numpy.linspace(0,2*numpy.pi, 50)
yy = spline_fit(xx)

# display the results.
numpy.plot(xx, numpy.sin(xx), 'r-', x,y,'ro',xx,yy, 'b--',linewidth=2)
axis('tight')
legend(['actual sin', 'original samples', 'interpolated curve'])
