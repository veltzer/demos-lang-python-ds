#!/usr/bin/env python

"""
TBD
"""


from typing import TYPE_CHECKING

import matplotlib.animation
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

import numpy as np

if TYPE_CHECKING:
    from matplotlib.axes._axes import Axes

rng = np.random.default_rng()


class Scope:
    """ Scope """
    def __init__(self, ax: Axes, maxt: float = 2, dt: float = 0.02) -> None:
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata: list[float] = [0.0]
        self.ydata: list[float] = [0.0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-.1, 1.1)
        self.ax.set_xlim(0, self.maxt)

    def update(self, y: float) -> tuple[Line2D]:
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

    def __str__(self) -> str:
        return str(self.tdata)


def emitter(p: float = 0.03):
    'return a random value with probability p, else 0'
    while True:
        v = rng.random(1)
        if v > p:
            yield 0.
        else:
            yield rng.random(1)


def main() -> None:
    """ main entry """
    fig, ax = plt.subplots()
    scope = Scope(ax)
    # pass a generator in "emitter" to produce data for the update func
    _ = matplotlib.animation.FuncAnimation(fig, scope.update, emitter, interval=10,
                                blit=True)
    plt.show()


if __name__ == "__main__":
    main()
