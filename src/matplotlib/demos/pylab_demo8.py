#!/usr/bin/env python3

"""
TBD
"""


import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
from matplotlib import animation


class Scope:
    """ Scope """
    def __init__(self, ax, maxt=2, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-.1, 1.1)
        self.ax.set_xlim(0, self.maxt)

    def update(self, y):
        """ update """
        lastt = self.tdata[-1]
        if lastt > self.tdata[0] + self.maxt:  # reset the arrays
            self.tdata = [self.tdata[-1]]
            self.ydata = [self.ydata[-1]]
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
            self.ax.figure.canvas.draw()

        t = self.tdata[-1] + self.dt
        self.tdata.append(t)
        self.ydata.append(y)
        self.line.set_data(self.tdata, self.ydata)
        return (self.line,)

    def __str__(self):
        return self.tdata


def emitter(p=0.03):
    'return a random value with probability p, else 0'
    while True:
        v = np.random.rand(1)
        if v > p:
            yield 0.
        else:
            yield np.random.rand(1)


def main():
    """ main entry """
    fig, ax = plt.subplots()
    scope = Scope(ax)
    # pass a generator in "emitter" to produce data for the update func
    _ = animation.FuncAnimation(fig, scope.update, emitter, interval=10,
                                blit=True)
    plt.show()


if __name__ == "__main__":
    main()
