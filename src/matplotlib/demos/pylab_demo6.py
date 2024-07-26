#!/usr/bin/env python

"""
TBD
"""

from collections import namedtuple
import numpy as np
import matplotlib.pyplot as plt

PlotData = namedtuple("PlotData",
                      ["x", "xs", "ys", "fig", "ax", "ax2", "line"])


class PointBrowser:
    """
    Click on a point to select and highlight it -- the data that
    generated the point will be shown in the lower axes.  Use the "n"
    and "p" keys to browse through the next and previous points
    """
    def __init__(self, pd):
        self.lastind = 0

        self.text = pd.ax.text(
            0.05,
            0.95,
            "selected: none",
            transform=pd.ax.transAxes,
            va="top"
        )
        self.selected,  = pd.ax.plot(
            [pd.xs[0]],
            [pd.ys[0]],
            # 'o',
            ms=12,
            alpha=0.4,
            color="yellow",
            visible=False
        )

        self.pd = pd

    def onpress(self, event):
        """ onpress """
        if self.lastind is None:
            return
        if event.key not in ("n", "p"):
            return
        if event.key == "n":
            inc = 1
        else:
            inc = -1
        self.lastind += inc
        self.lastind = np.clip(self.lastind, 0, len(self.pd.xs)-1)
        self.update()
        return

    def onpick(self, event):
        """ onpick """
        if event.artist != self.pd.line:
            return True
        n = len(event.ind)
        if not n:
            return True
        # the click locations
        xp = event.mouseevent.xdata
        yp = event.mouseevent.ydata
        distances = np.hypot(
            xp-self.pd.xs[event.ind],
            yp-self.pd.ys[event.ind]
        )
        indmin = distances.argmin()
        dataind = event.ind[indmin]
        self.lastind = dataind
        self.update()
        return False

    def update(self):
        """ update """
        if self.lastind is None:
            return

        dataind = self.lastind

        self.pd.ax2.cla()
        self.pd.ax2.plot(self.pd.x[dataind])

        self.pd.ax2.text(
                0.05,
                0.9,
                f"mu={self.pd.xs[dataind]}\nsigma={self.pd.ys[dataind]}",
                transform=self.pd.ax2.transAxes,
                va="top"
        )
        self.pd.ax2.set_ylim(-0.5, 1.5)
        self.selected.set_visible(True)
        self.selected.set_data(self.pd.xs[dataind], self.pd.ys[dataind])

        self.text.set_text(f"selected: {dataind}")
        self.pd.fig.canvas.draw()
        return


def main():
    """ main entry point """
    x = np.random.rand(20, 20)
    xs = np.mean(x, axis=1)
    ys = np.std(x, axis=1)
    fig, (ax, ax2) = plt.subplots(2, 1)
    ax.set_title("click on point to plot time series")
    ax2.set_title("details")
    fig.tight_layout()
    line, = ax.plot(xs, ys, "o", picker=5)  # 5 points tolerance
    browser = PointBrowser(PlotData(x, xs, ys, fig, ax, ax2, line))
    fig.canvas.mpl_connect("pick_event", browser.onpick)
    fig.canvas.mpl_connect("key_press_event", browser.onpress)
    plt.show()


if __name__ == "__main__":
    main()
