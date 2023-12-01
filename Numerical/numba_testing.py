"""
Custom module for learning about the Numba library.  Numba works best with Numpy, loops, and simpler 
math algorithms, e.g., python.math.

Class(es):
    None

Function(s):
    test(int) -> float
    test_numba(int) -> float
    test_numpy(int) -> float
    test_numpy_numba(int) -> float
    test_pandas(DataFrame) -> DataFrame
    test_pandas_numba(DataFrame) -> DataFrame
    main() -> None
"""

import math
import random
import time

import numpy as np
import numpy.typing as npt
import pandas as pd  # type: ignore
import pandas_datareader as web  # type: ignore
from numba import jit, njit  # type: ignore


def test(n: int) -> float:
    """
    Simple function without JIT to compare normal Python math performance to Numba JIT performance.

    Args:
        n (int): Range of numbers to compute

    Returns:
        float: The result of computation
    """
    c = 0.0

    for _ in range(n):
        a = random.random()
        b = random.random()
        c += math.sqrt(a**2 + b**2)

    return c


@njit  # nopython=True by default == @jit(nopython=True) <- Machine code ONLY
def test_numba(n: int) -> float:
    """
    Simple function with JIT to compare normal Python math performance to Numba JIT performance.

    Args:
        n (int): Range of numbers to compute

    Returns:
        float: The result of computation
    """
    c = 0.0

    for _ in range(n):
        a = random.random()
        b = random.random()
        c += math.sqrt(a**2 + b**2)

    return c


def test_numpy(n: int) -> npt.NDArray:
    """
    Simple function without JIT to compare normal Numpy performance to Numba JIT performance.

    Args:
        n (int): Range of numbers to compute

    Returns:
        float: The result of computation
    """
    c = np.zeros((n, n))

    for _ in range(n):
        a = np.random.rand(n, n)
        b = np.random.rand(n, n)
        c += np.sqrt(a**2 + b**2)

    return c


@njit  # nopython=True by default == @jit(nopython=True) <- Machine code ONLY
def test_numpy_numba(n: int) -> npt.NDArray:
    """
    Simple function with JIT to compare normal Numpy performance to Numba JIT performance.

    Args:
        n (int): Range of numbers to compute

    Returns:
        float: The result of computation
    """
    c = np.zeros((n, n))

    for _ in range(n):
        a = np.random.rand(n, n)
        b = np.random.rand(n, n)
        c += np.sqrt(a**2 + b**2)

    return c


def test_pandas(data: pd.DataFrame) -> pd.DataFrame:
    """
    Simple function without JIT to compare Pandas performance to Numba JIT performance.

    Args:
        data (pd.DataFrame): Data to be processed

    Returns:
        pd.DataFrame: Transposed result DataFrame
    """

    result = data.sort_values(by=["Volume"])
    result = result.applymap(math.sqrt)
    result += 2  # Valid Python code, but Numba can't compile
    result = result.applymap(
        lambda x: x**2
    )  # Valid Python code, but Numba can't handle lambda

    return result.T


@jit  # (nopython=False) Numba must run in object mode to handle Pandas DataFrames <- mixed compilation and interepretation
def test_pandas_numba(data: pd.DataFrame) -> pd.DataFrame:
    """
    Simple function with JIT to show limits of Numba when applied to Pandas DataFrames.  Numba doesn't fully
    understand DataFrames and can't fully type them, limiting its ability to compile.  Numba must be applied
    in object mode, a mix of compilation and Python interpretation.  Of note, Numba can't handle lambda functions.

    Args:
        data (pd.DataFrame): Data to be processed

    Returns:
        pd.DataFrame: Transposed result DataFrame
    """
    result = data.sort_values(by=["Volume"])
    result = result.applymap(math.sqrt)
    result += 2  # Valid Python code, but Numba can't compile
    # result = result.applymap(
    #     lambda x: x**2
    # )  # Valid Python code, but Numba can't handle lambda

    return result.T


def main():
    """
    Module run function.
    """

    n = 10_000_000
    p = 500

    data = web.DataReader(name="AAPL", data_source="stooq")

    # Run standard Python math
    start = time.time()
    test(n)
    end = time.time()
    print(f"Time to run test({n}): {end-start:.03f} seconds")

    # Run Python math with Numba - compilation happens here
    # Note: Despite compilation, siginficant speedup
    start = time.time()
    test_numba(n)
    end = time.time()
    print(f"Time to run test_numba({n}): {end-start:.03f} seconds")

    # Run Python math with Numba - compiled machine code used here
    # Note: Even greater speedup compared to pure Python math
    start = time.time()
    test_numba(n)
    end = time.time()
    print(f"Time to run test_numba({n}): {end-start:.03f} seconds")

    # Run standard Numpy
    start = time.time()
    test_numpy(p)
    end = time.time()
    print(f"Time to run test_numpy({p}): {end-start:.03f} seconds")

    # Run Numpy with Numba - compilation happens here
    start = time.time()
    test_numpy_numba(p)
    end = time.time()
    print(f"Time to run test_numpy_numba({p}): {end-start:.03f} seconds")

    # Run Numpy with Numba - compiled machine code used here
    # Note: Not a huge speedup in this case - it depends on the computations being done
    start = time.time()
    test_numpy_numba(p)
    end = time.time()
    print(f"Time to run test_numpy_numba({p}): {end-start:.03f} seconds")

    # Run standard Pandas
    start = time.time()
    test_pandas(data)
    end = time.time()
    print(f"Time to run test_pandas(data): {end-start:.03f} seconds")

    # Run Pandas with Numba - object mode = not fully compiled
    # Note: Runtime increased due to object mode
    start = time.time()
    test_pandas_numba(data)
    end = time.time()
    print(f"Time to run test_pandas_numba(data): {end-start:.03f} seconds")

    # Run Pandas with Numba - limited compiled machine code used here
    # Note: Some speedup
    start = time.time()
    test_pandas_numba(data)
    end = time.time()
    print(f"Time to run test_pandas_numba(data): {end-start:.03f} seconds")


if __name__ == "__main__":
    main()
