import numpy as np


class Grid:
    """ Creates a grid """

    _grid = None

    def __init__(self, n_rows: int, n_cols: int):
        """
        Uses the number of rows and columns to create a numpy n-dimensional grid of zeros.
        
        Args:
            n_rows: The number of rows for the grid.
            n_cols: The number of columns for the grid.
        """

        self._check_int(n_rows)
        self._check_int(n_cols)

        self.n_rows = n_cols
        self.n_cols = n_cols

        self.create_grid()

    def _check_int(self, number):
        """ Asserts if the passed parameters are integers. """
        assert isinstance(number,int), f"Please enter an integer number of rows. {number} is not an integer"

    def create_grid(self):
        """ Generates the n-dimensional grid filled with zeros. """
        self._grid = np.zeros((self.n_rows, self.n_cols), dtype=bool)
