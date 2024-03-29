"""
Custom module for timing decorators.

Class(es):
    None

Function(s):
    simple_timer(function) -> function
    simple_add(int, int) -> int
"""

from functools import reduce, wraps
from operator import mul
from time import time as timer


def simple_timer(func):
    """
    Wrapper function for timing other functions.

    Args:
        func (function): Function to be timed
    """

    # Use wraps decorator to preserve info of original function passed to decorator
    # This is always important, but especially in case of chained decorators
    @wraps(func)
    def time_wrap(*args, **kwargs):
        start = timer()
        value = func(*args, **kwargs)
        after = timer()
        print(f"{func.__name__} took {after-start:.05f} seconds to complete.")

        return value

    return time_wrap


@simple_timer
def simple_add(n: int) -> int:
    """
    Simple function to sum integers from 1 to n inclusive.

    Args:
        n (int): Number of digits to sum

    Returns:
        int: Sum of numbers 1 to n inclusive
    """

    return sum(range(1, n + 1))

@simple_timer
def simple_multiply(n: int) -> int:
    """
    Simple function to multiple integers from 1 to n inclusive.

    Args:
        n (int): Number of digits to multiply

    Returns:
        int: Product of numbers 1 to n inclusive
    """

    return reduce(mul, range(1, n+1)) 


def main():
    """
    Module run method.

    Args:
        None

    Returns:
        None
    """

    n = 1000

    print(f"Sum of numbers from 1 to {n}: {simple_add(n)}")

    print(f"Product of numbers from to 10: {simple_multiply(10)}")


if __name__ == "__main__":
    main()
