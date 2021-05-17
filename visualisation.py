import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
from matplotlib import style
import numpy as np


class Animation:
    style.use("fivethirtyeight")

    fig = plt.figure()

    ax1 = fig.add_subplot(1, 1, 1)

    def __init__(self):
        pass

    def plot_heatmap(self, grid, **kwargs):

        self.ax1.clear()

        self.ax1 = sns.heatmap(grid, linewidths=0.5, **kwargs)

    def animate(self, function, time_sleep: int, frames: int = 10):

        if not isinstance(time_sleep, int):
            raise TypeError("Please set time_sleep to be an integer.")

        return animation.FuncAnimation(self.fig, function, interval=time_sleep, frames=frames)


