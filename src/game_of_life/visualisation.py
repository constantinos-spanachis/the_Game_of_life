import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
from matplotlib import style
import numpy as np


class Animation:
    """ Generates the game's animation using seaborn's heatmap, and matplotlib's animation """
    style.use("fivethirtyeight")

    fig = plt.figure()

    ax1 = fig.add_subplot(1, 1, 1)

    def plot_heatmap(self, grid, **kwargs) -> None:
        """
        Plots the heatmap of a grid.
        
        Args:
            grid: The grid you want to plot.
            **kwargs: Any seaborn argument that you want to use.
        """
        
        self.ax1.clear()

        self.ax1 = sns.heatmap(grid, linewidths=0.5, **kwargs)

    def animate(self, function, time_sleep: int, frames: int = 10) -> animation.FuncAnimation:
        """
        Uses matplotlib's animation package to animate the different frames.
        
        Args:
            function: The function that will be animated.
            time_sleep: The pause between each frame.
            frames: The frames.

        Returns:
            The animation.
        """

        if not isinstance(time_sleep, int):
            raise TypeError("Please set time_sleep to be an integer.")

        return animation.FuncAnimation(self.fig, function, interval=time_sleep, frames=frames)


