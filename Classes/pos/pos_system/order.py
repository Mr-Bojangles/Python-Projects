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

    customer_id: int = 0
    customer_name: str = ""
    customer_address: str = ""
    customer_postal_code: str = ""
    customer_city: str = ""
    customer_email: str = ""
    items: list[str] = field(default_factory=list)
    quantities: list[int] = field(default_factory=list)
    prices: list[int] = field(default_factory=list)
    _status: OrderStatus = OrderStatus.OPEN
    id: str = ""

    def create_line_item(self, name: str, quantity: int, price: float) -> None:
        """
        Method to add a line item to an an order.

        Args:
            name (str): Name of item to be added
            quantity (int): Number of the item to be added
            price (float): Price of the item
        """

        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def set_status(self, status: OrderStatus) -> None:
        """
        Set status of an order

        Args:
            status (OrderStatus)
        """
        self._status = status
