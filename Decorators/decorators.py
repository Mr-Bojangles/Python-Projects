"""
Custom module for learning about decorators with examples.

Classes:
    DecoratorClass

Functions:
    outer_function(str) -> function
    decorator_func(function) -> function
    display()
    display_info(str, int)
    my_logger(function) -> function
    logging_info(str, int)
"""

import logging
from functools import wraps
from typing import Any

from simple_timer import simple_timer


def outer_function(msg: str):
    """
    A simple function demonstrating the use of inner functions in Python.

    Args:
        msg (str): Message to be printed.

    Returns:
        function: Callable function
    """

    def inner_function():
        print(msg)  # Free variable - message is referenced, but NOT defined, here

    return inner_function


# Inner/Outer function call examples
# hi_func = outer_function("Hi!")
# by_func = outer_function("Bye!")
# hi_func()
# by_func()


def decorator_func(function):
    """
    A basic example of a decorator function that can take an arbitrary number of
    positional arguments.

    Args:
        function: Function to be decorated
    """

    def wrapper_func(*args, **kwargs):
        print(f"Wrapper function executed this before {function.__name__}")
        return function(*args, **kwargs)

    return wrapper_func


class DecoratorClass:
    """
    A basic example of using a class as a decorator.

    Class Attributes:
        None

    Instance Attributes:
        function: Dectorated function
    """

    def __init__(self, function) -> None:
        """
        Initialize instance with function to be decorated.

        Args:
            function: Function to be decorated
        """
        self.function = function

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """
        Create instance as a callable method.

        Returns:
            Any: A decorated function
        """
        print(f"Call method executed this before {self.function.__name__}")
        return self.function(*args, **kwargs)


@decorator_func  # Syntactic sugar for display = decorator_func(display)
# @DecoratorClass # Will behave the same as decorator_func
def display():
    """
    Simple function to demonstrate how to use a decorator.
    """
    print("Display function ran.")


# Example of a decorated function
# decorated_display = decorator_func(display)  # Equal to wrapper_func
# decorated_display()  # Calls wrapper_func(), which executes and returns display()

# Example of a decorated function using Python decorator syntax
# display()


@decorator_func  # Syntactic sugar for display_info = decorator_func(display_info)
# @DecoratorClass # Will behave the same as decorator_func
def display_info(name: str, age: int):
    """
    Simple function to demonstrate how to use a decorator with a function that takes arguments.

    Args:
        name (str): A user's name
        age (int): A user's age
    """
    print(f"display_info ran with arguments ({name}, {age})")


# Example of a decorated multi-argument function using Python decorator syntax
# display_info("Craig", 40)


def my_logger(function):
    """
    A practical example of using a decorator to log info about a function.

    Args:
        function: Function to be decorated for logging

    Returns:
        function: The decorated function
    """
    logging.basicConfig(filename=f"{function.__name__}.log", level=logging.INFO)

    # Use wraps decorator to preserve info of original function passed to decorator
    # This is always important, but especially in case of chained decorators
    @wraps(function)
    def wrapper_func(*args, **kwargs):
        logging.info("Ran with args: %s and kwargs: %s", args, kwargs)
        return function(*args, **kwargs)

    return wrapper_func


@simple_timer
@my_logger
def logging_info(name: str, age: int):
    """
    Simple function to demonstrate how to use a decorator with a function that takes arguments and log it.

    Args:
        name (str): A user's name
        age (int): A user's age
    """
    print(f"logging_info ran with arguments ({name}, {age})")


# Example of a decorated multi-argument function being timed and logged using Python decorator syntax
logging_info("Bill", 25)
