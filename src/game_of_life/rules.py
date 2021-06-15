import numpy as np


def check_number_of_alive_neighbours(grid: np.ndarray, ) -> np.ndarray:
    """
    Dictates which cells will be alive on the next epoch using the rules for the game of life. The rules are:
        1. If there are no living cells around a cell then the cell will die
        2. If there are more than 4 living neighbour cells, the cell will die
        3. If there are exactly 3 living neighbour cells, the cell will live.
        
    Args:
        grid: The grid at a single epoch.
        
    Returns
        The grid for the next epoch.
    """

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
