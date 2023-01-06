"""
Custom module for calculating Fibonacci sequences.

Class(es):
    Fibonacci

Function(s):
    None
"""


class Fibonacci:
    """
    Iteratively calculate the Fibonacci sequence for a given number.  Additionally, each instance
    has a list acting as a local cache of the sequence, speeding up lookup times for already
    calculated values and improving memory usage over the recursive Fibonacci calculation.

    Class Attributes:
        None

    Instance Attributes:
        cache (list[int]): Stores Fibonacci sequence
    """

    def __init__(self):
        """
        Initialize instance attributes.
        """

        self.cache = [0, 1]

    def __call__(self, n: int) -> list[int]:
        """
        Iteratively calculate a Fibonacci sequence by using the fact that the next number in
        the sequence only relies on the sum of the previous two numbers in the sequence.  An
        instance of this type is callable.

        Args:
            n (int): Length of Fibonacci sequence to be computed

        Raises:
            ValueError: n must be a positive integer

        Returns:
            list: The Fibonacci sequence of a number n
        """

        # Guard statements
        if not isinstance(n, int):
            raise ValueError(f"Integer expected, got {n}")
        if n < 0:
            return f"Expect positive integer, got {n}"
        if n < len(self.cache):
            return self.cache[n]

        for _ in range(2, n):
            fib_num = self.cache[-2] + self.cache[-1]
            self.cache.append(fib_num)

        return self.cache

    def __repr__(self) -> str:
        return "fib = Fibonacci()\nfib(n)"


def main():
    """
    Run Fibonacci sequence calculation.

    Args:
        None

    Returns:
        None
    """

    fib = Fibonacci()

    n: int = int(input("Input a number: "))

    seq: list[int] = fib(n)

    print(f"The Fibonacci sequence for n={n} is {seq}")


if __name__ == "__main__":
    main()
