from game_of_life.construction import Grid
from game_of_life.rules import check_number_of_alive_neighbours
from game_of_life.visualisation import Animation

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

class GameOfLife(Grid, Animation):

    def __init__(self,
                 grid: np.ndarray = None,
                 n_rows: int = 25,
                 n_cols: int = 25,
                 time_sleep: int = 5,
                 n_iterations: int = 100):
        if grid == None:
            Grid.__init__(self, n_rows, n_cols)
            self.grid = self._get_random_starting_point()
        else:
            self.grid = grid
        Animation.__init__(self,)
        self.time_sleep = time_sleep
        self.n_iterations = n_iterations

    def _get_random_starting_point(self):

        mask = np.random.randint(0, 2, size=self.grid.shape).astype(bool)

        random_starting_grid = self.grid

        random_starting_grid[mask] = True

        return random_starting_grid

    def get_frame(self, frame):

        self.grid = check_number_of_alive_neighbours(self.grid)

        cmap = colors.ListedColormap(["white", "black"])

        bounds = [0, 0.5, 1]

        norm = colors.BoundaryNorm(bounds, cmap.N)

        self.plot_heatmap(self.grid, cbar=False, cmap=cmap, norm=norm)

        self.ax1.set_title(f"Iteration {frame}")

    def play_the_game(self):

        ani = self.animate(self.get_frame, self.time_sleep*1000, frames=self.n_iterations)

        plt.show()


if __name__ == '__main__':

    class_ = GameOfLife(n_rows=25, n_cols=25, time_sleep=10, n_iterations=10)

    class_.play_the_game()