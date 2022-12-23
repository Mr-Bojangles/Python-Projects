from timeit import timeit as timer


def fib(n):
    """
    Recursively calculate the Fibonacci numbers for the numbers 0 to n (exclusive)

    Args:
        n (int): The length of the Fibonacci sequence to be  generated
    """

    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def main():

    n = 10

    start = timer()
    for i in range(n):
        fib(i)
    stop = timer()

    print(f"")


if __name__ == "__main__":
    main()
