"""
Module for representing the LineItems of an Order.

Class(es):
    LineItem

Function(s):
    None
"""
from dataclasses import dataclass


@dataclass
class LineItem:
    """
    Dataclass representing a line item in an order.
    """

    item: str
    quantity: int
    price: int

    @property
    def total_price(self) -> int:
        """
        Calculate total price for a line item.

        Returns:
            int: Total price of line item
        """
        return self.quantity * self.price
