#!/usr/bin/env python3

"""
TBD
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


def update_line(num, datums, line):
    """ update_line """
    line.set_data(datums[..., :num])
    return (line,)


fig1 = plt.figure()
data = np.random.rand(2, 25)
l, = plt.plot([], [], 'r-')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(
    fig1, update_line,
    25, fargs=(data, l), interval=300
)
# line_ani.save('lines.mp4')

fig2 = plt.figure()

x = np.arange(-9, 10)
y = np.arange(-9, 10).reshape(-1, 1)
base = np.hypot(x, y)
ims = []
for add in np.arange(5):
    ims.append((plt.pcolor(x, y, base + add, norm=plt.Normalize(0, 30)),))
im_ani = animation.ArtistAnimation(
        fig2, ims, interval=50,
        repeat_delay=3000, blit=True
)
# im_ani.save('im.mp4', metadata={'artist':'Guido'})

plt.show()
