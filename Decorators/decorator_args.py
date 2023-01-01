"""
Custom module for learning how to create a decorator that takes arguments.

Class(es):
    None

Function(s):
    prefix_decorator(Any) -> function
    display_info(str, int) -> function
    main() -> None
"""
from typing import Any


def prefix_decorator(prefix: Any):
    """
    Function that allows a decorator to take an argument.

    Args:
        prefix (Any): Prefix to be added to decorator output
    """

    def decorator_func(function):
        """
        A basic example of a decorator function that can take an arbitrary number of
        positional arguments.

        Args:
            function: Function to be decorated
        """

        def wrapper_func(*args, **kwargs):
            print(f"{prefix} Wrapper function executed this before {function.__name__}")
            return function(*args, **kwargs)

        return wrapper_func

    return decorator_func


@prefix_decorator(
    "TESTING DECORATOR ARGUMENTS:"
)  # display_info = prefix_decorator(prefix)(display_info)
def display_info(name: str, age: int, height: int):
    """
    Simple function to demonstrate how to use a decorator that takes arguments itself.

    Args:
        name (str): A user's name
        age (int): A user's age
    """
    print(f"display_info ran with arguments ({name}, {age}, {height})")


def main():
    """
    Module run method.
    """

    display_info("Craig", 40, 72)


if __name__ == "__main__":
    main()
