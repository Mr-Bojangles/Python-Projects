"""
Custom module for learning about the Numba library.
"""

import math
import random
import time

from numba import jit


def test(n: int) -> float:
    c = 0

    for _ in range(n):
        a = random.random()
        b = random.random()
        c += math.sqrt(a**2 + b**2)

    return c


n = 10_000_000
start = time.time()
test(n)
end = time.time()
print(f"Time to run test({n}): {end-start} seconds")
