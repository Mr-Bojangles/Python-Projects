from time import time as timer
from functools import cache


@cache
def fib(n):
    """
    Recursively calculate the Fibonacci numbers for the numbers 0 to n (exclusive).

    The cache decorator stores values to be applied to subsequent calcuations, greatly reducing compute time.

    Args:
        n (int): The length of the Fibonacci sequence to be  generated
    """

    return n if n <= 1 else fib(n - 1) + fib(n - 2)


def main():

    n = 1000

    start = timer()
    for i in range(n):
        fib(i)
    stop = timer()

    print(f"Time to compute Fibonnaci sequence to n={n}: {stop - start:.05f} seconds.")


if __name__ == "__main__":
    main()
