"""
Created on Sun Jan 18 00:57:43 2015

@author: liran
"""

from typing import TYPE_CHECKING

import matplotlib.pyplot as plt

import numpy as np

if TYPE_CHECKING:
    from typing import Any

x = np.arange(50)*2*np.pi/50
y = np.sin(x)

fig, ax = plt.subplots()


plt.plot(x, y, '-o', picker=4)
text = ax.text(0, -0.5, " ", va="bottom", ha="left")


# a pick event carries what its artist adds to it (here ind, the picked points)
def on_pick(event: Any) -> None:
    """ on_pick """
    thisline = event.artist
    _xdata, _ydata = thisline.get_data()
    ind = event.ind
    text.set_text(str(ind))


cid = fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()
