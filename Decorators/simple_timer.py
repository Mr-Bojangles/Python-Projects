from time import time as timer


def simple_timer(func):
    """
    Wrapper function for timing other functions.

    Args:
        func (function): Function to be timed
    """

    def time_wrap(*args, **kwargs):
        start = timer()
        value = func(*args, **kwargs)
        after = timer()
        print(f"{func.__name__} took {after-start:.05f} seconds to complete.")

        return value

    return time_wrap


@simple_timer
def simple_add(n):
    """
    Simple function to sum numbers from 1 to n inclusive.

    Args:
        n (int): Number of digits to sum

    Returns:
        int: Sum of numbers 1 to n inclusive
    """

    return sum(range(1, n + 1))


def main():

    n = 1000

    print(f"Sum of numbers from 1 to {n}: {simple_add(n)}")


if __name__ == "__main__":
    main()
