"""
Custom module for testing decorators.

Class(es):
    None

Function(s):
    rec_fib_seq(int) -> int
    iter_fib_seq(int) -> list[int]
    iter_fib_num(int) -> int
"""

from time import time as timer
from functools import cache
from simple_timer import simple_timer


@cache
def rec_fib_seq(n: int) -> int:
    """
    Recursively calculate the Fibonacci number for the numbers 0 to n (exclusive).

    The cache decorator stores values to be applied to subsequent calcuations, greatly
    reducing compute time.

    Args:
        n (int): The nth term in the Fibonacci sequence to be calculated

    Returns:
        int: The nth term in the Fibonacci sequence
    """

    return n if n <= 1 else rec_fib_seq(n - 1) + rec_fib_seq(n - 2)


@simple_timer
def iter_fib_seq(n: int) -> list[int]:
    """
    Iteratively calculate the Fibonnaci sequence for the numbers 0 to n (exclusive).

    Args:
        n (int): The length of the Fibonacci sequence to be generated.

    Returns:
        list[int]: The Fibonacci sequence of length n
    """
    a: int = 0
    b: int = 1

    fib_seq: list = [a, b]

    while n - 2:
        c = a + b
        a, b = b, c
        n -= 1
        fib_seq.append(c)

    return fib_seq


@simple_timer
def iter_fib_num(n: int) -> int:
    """
     Iteratively calculate the nth Fibonnaci number.

    Args:
        n (int): The nth term in the Fibonacci sequence to be calculated

    Returns:
        int: The nth term in the Fibonacci sequence
    """
    a: int = 0
    b: int = 1

    for _ in range(n):
        a, b = b, a + b

    return a


def main():
    """
    Module run method.

    Args:
        None

    Returns:
        None
    """

    n = 100

    # Timing recursive Fibonacci sequence
    start = timer()
    for i in range(n):
        rec_fib_seq(i)
    stop = timer()

    print(
        f"Time to recursively calculate Fibonnaci sequence to n={n}: {stop - start:.05f} seconds."
    )

    # Timing iterative Fibonacci sequence using decorator
    print(f"Time to iteratively calculate Fibonacci sequence to n={n}")
    iter_fib_seq(n)

    # Timing iterative Fibonacci number using decorator
    print(f"Time to iteratively calculate Fibonacci number {n}")
    iter_fib_num(n)


if __name__ == "__main__":
    main()
