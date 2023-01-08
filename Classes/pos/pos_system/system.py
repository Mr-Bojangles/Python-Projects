"""
Module defining a point-of-sale system.

Class(es):
    POSSystem

Function(s):
    generate_id(int) -> str
"""

import random
import string
from typing import Protocol

from pos_system.order import Order, OrderStatus


def generate_id(length: int = 6) -> str:
    """
    Helper function for generating an id.

    Args:
        length (int, optional): Length of order ID. Defaults to 6.

    Returns:
        str: The order ID
    """
    return "".join(random.choices(string.ascii_uppercase, k=length))


class PaymentProcessor(Protocol):
    """
    Interface for payment processing.
    """

    def process_payment(self, reference: str, price: int) -> None:
        """
        Process payment for an order.

        Args:
            reference (str): ID of order to process for payment
            price (int): Total price of an order
        """


class POSSystem:
    """
    Class defining the point-of-sale system.

    Attribute(s):
        payment_processor (StripePaymentProcessor): Payment processor to be used
        orders (dict[str, Order]): Dictionary of Orders, keyed by order ID
    """

    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor
        self.orders: dict[str, Order] = {}

    def register_order(self, order: Order):
        """
        Register receipt of an order by giving it an ID and adding it to
        the order dictionary.

        Args:
            order (Order): Order received
        """

        order.id = generate_id()
        self.orders[order.id] = order

    def find_order(self, order_id: str) -> Order:
        """
        Find an order by its ID.

        Args:
            order_id (str): Order to be found

        Returns:
            Order: Requested order
        """

        return self.orders[order_id]

    def process_order(self, order: Order) -> None:
        """
        Process order for payment and shipping.

        Args:
            order (Order): Order to process
        """
        self.payment_processor.process_payment(order.id, order.total_price)
        order.set_status(OrderStatus.PAID)
        print("Shipping order to customer.")
