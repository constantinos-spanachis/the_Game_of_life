import numpy as np


class Grid:

    grid = None

    def __init__(self, n_rows: int, n_cols: int):

        self._check_int(n_rows)
        self._check_int(n_cols)

        self.n_rows = n_cols
        self.n_cols = n_cols

        self.create_grid()

    def _check_int(self, number):
        assert isinstance(number,int), f"Please enter an integer number of rows. {number} is not an integer"

    def create_grid(self):
        self.grid = np.zeros((self.n_rows, self.n_cols), dtype=bool)
