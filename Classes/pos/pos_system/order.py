"""
Module representing an order in a point-of-sale system.

Class(es):
    OrderStatus(Enum)
    Order

Function(s):
    None
"""

from dataclasses import dataclass, field
from enum import Enum, auto

from pos_system.customer import Customer
from pos_system.line_item import LineItem


class OrderStatus(Enum):
    """
    Represent status of an order.
    """

    OPEN = auto()
    PAID = auto()
    RETURNED = auto()
    CANCELED = auto()
    DELIVERED = auto()


@dataclass
class Order:
    """
    Representation of an order.
    """

    customer: Customer
    items: list[LineItem] = field(default_factory=list)
    _status: OrderStatus = OrderStatus.OPEN
    id: str = ""

    def add_line_item(self, item: LineItem) -> None:
        """
        Method to add a line item to an an order.

        Args:
            name (str): Name of item to be added
            quantity (int): Number of the item to be added
            price (float): Price of the item
        """

        self.items.append(item)

    def set_status(self, status: OrderStatus) -> None:
        """
        Set status of an order

        Args:
            status (OrderStatus)
        """

        self._status = status

    @property
    def total_price(self) -> int:
        """
        Calculate total price of an order.

        Returns:
            int: Total price
        """

        return sum(line_item.total_price for line_item in self.items)
