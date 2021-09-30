import numpy as np


def array_to_table(array: np.array):
    return '\n'.join(','.join(row) for row in array.astype(str))