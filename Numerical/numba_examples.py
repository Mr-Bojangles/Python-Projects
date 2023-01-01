"""
Custom module for learning how to use Numba with Numpy.

Class(es):
    None

Function(s):
    numpy_features(np.array) -> None
    main() -> None
"""

import time

import numpy as np
from numba import njit


def numpy_features(matrix: np.array) -> None:
    """
    Simple function demonstrating basic features of NumPy.

    Args:
        matrix (np.array): Multidimensional array
    """

    cos_trace = 0.0

    for i in range(matrix.shape[0]):
        cos_trace += np.cos(matrix[i, i])

    matrix = matrix + cos_trace  # Numpy broadcasting


@njit  # nopython=True by default == @jit(nopython=True) <- Machine code ONLY
def numba_features(matrix: np.array) -> None:
    """
    Simple function demonstrating using Numba with NumPy.

    Args:
        matrix (np.array): Multidimensional array
    """

    cos_trace = 0.0

    for i in range(matrix.shape[0]):
        cos_trace += np.cos(matrix[i, i])

    matrix = matrix + cos_trace  # Numpy broadcasting


def main():
    """
    Module run method.
    """
    a = np.arange(1_000_000).reshape(1000, 1000)

    # Run standard NumPy
    start = time.time()
    numpy_features(a)
    end = time.time()
    print(f"Time to compute numpy_features(a): {end-start:.03f} seconds")

    # Run Numpy with Numba - compilation happens here, so potentially slower
    start = time.time()
    numba_features(a)
    end = time.time()
    print(f"Time to compute numba_features(a): {end-start:.03f} seconds")

    # Run Numpy with Numba - use compiled machine code to see speedup
    start = time.time()
    numba_features(a)
    end = time.time()
    print(f"Time to compute numba_features(a): {end-start:.03f} seconds")


if __name__ == "__main__":
    main()
