import numpy as np


def check_number_of_alive_neighbours(grid: np.ndarray, ) -> np.ndarray:

    assert(np.ndim(grid) == 2), "Please provide an R^2 grid"

    for i, j in np.argwhere(grid):

        count = np.count_nonzero(grid[i-1:i+2, j-1:j+2]) - 1

        if count <= 1 or count >= 4:

            grid[i, j] = False

    for i, j in np.argwhere(~grid):

        count = np.count_nonzero(grid[i-1:i+2, j-1:j+2])

        if count == 3:

            grid[i, j] = True

    return grid





if __name__ == '__main__':


    grid = Grid(25, 25).grid

    mask = np.random.randint(0, 2, size=grid.shape).astype(bool)

    grid[mask] = True

    check_number_of_alive_neighbours(grid)
