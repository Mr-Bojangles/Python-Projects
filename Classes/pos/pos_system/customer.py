"""
Module for representing the Customer of an Order.

Class(es):
    Customer

Function(s):
    None
"""

from dataclasses import dataclass


@dataclass
class Customer:
    """
    Dataclass representing a Customer for an Order.
    """

    id: int = 0
    name: str = ""
    address: str = ""
    postal_code: str = ""
    city: str = ""
    email: str = ""
