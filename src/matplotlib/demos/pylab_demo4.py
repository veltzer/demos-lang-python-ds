#!/usr/bin/env python3

"""
TBD
"""

import matplotlib.pyplot as plt


def handle_close(_evt):
    """ close function """
    print('Closed Figure!!!')


fig = plt.figure()
fig.canvas.mpl_connect('close_event', handle_close)

plt.text(0.35, 0.5, 'Close Me!', {"size": 30})
plt.show()
