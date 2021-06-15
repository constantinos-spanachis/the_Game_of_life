from game_of_life.construction import Grid
from game_of_life.rules import check_number_of_alive_neighbours
from game_of_life.visualisation import Animation

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from typing import Optional


class GameOfLife(Grid, Animation):
    """ A class that runs a game of life for a number of epochs based on an initial formation. """

    def __init__(self,
                 grid: np.ndarray = None,
                 n_rows: Optional[int] = 25,
                 n_cols: Optional[int] = 25,
                 time_sleep: int = 5,
                 n_iterations: int = 100):
        """
        Initiates the game.
        
        Args:
            grid: The grid at the zeroth epoch.
            n_rows: Numbers of rows in the grid. Only used if an initial grid is not passed
            n_cols: Numbers of columns in the grid. Only used if an initial grid is not passed
            time_sleep: The pause between each epoch.
            n_iterations: The number of epochs.
        """
        if grid == None:
            Grid.__init__(self, n_rows, n_cols)
            self.grid = self._get_random_starting_point()
        else:
            self.grid = grid
        Animation.__init__(self,)
        self.time_sleep = time_sleep
        self.n_iterations = n_iterations

    def _get_random_starting_point(self) -> np.ndarray:
        """
        If an initial grid is not passed, this function initiates a random grid based on the number of columns and rows
        passed.
        
        Returns:
            The grid as a numpy n-dimensional array
        """

        mask = np.random.randint(0, 2, size=self.grid.shape).astype(bool)

        random_starting_grid = self._grid

        random_starting_grid[mask] = True

        return random_starting_grid

    def get_frame(self, frame):
        """
        Runs the iterations.
        
        Args:
            frame: The current epoch's grid.

        Returns:
            The next epoch's grid
        """

        self.grid = check_number_of_alive_neighbours(self.grid)

        cmap = colors.ListedColormap(["white", "black"])

        bounds = [0, 0.5, 1]

        norm = colors.BoundaryNorm(bounds, cmap.N)

        self.plot_heatmap(self.grid, cbar=False, cmap=cmap, norm=norm)

        self.ax1.set_title(f"Iteration {frame}")

    def play_the_game(self):
        """ Runs the game based on the given configuration, for the passed number of iterations. """
    
        ani = self.animate(self.get_frame, self.time_sleep*1000, frames=self.n_iterations)

        plt.show()
