"""
Module defining a point-of-sale system.

Class(es):
    POSSystem

Function(s):
    generate_id(int) -> str
"""

import random
import string

from pos_system.order import Order, OrderStatus
from pos_system.payment import StripePaymentProcessor


def generate_id(length: int = 6) -> str:
    """
    Helper function for generating an id.

    Args:
        length (int, optional): Length of order ID. Defaults to 6.

    Returns:
        str: The order ID
    """
    return "".join(random.choices(string.ascii_uppercase, k=length))


class POSSystem:
    """
    Class defining the point-of-sale system.

    Attribute(s):
        payment_processor (StripePaymentProcessor): Payment processor to be used
        orders (dict[str, Order]): Dictionary of Orders, keyed by order ID
    """

    def __init__(self):
        self.payment_processor = StripePaymentProcessor(self)
        self.orders: dict[str, Order] = {}

    def setup_payment_processor(self, url: str) -> None:
        """
        Create connection to a payment processor.

        Args:
            url (str): Address of payment processor
        """

        self.payment_processor.connect_to_service(url)

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

    def compute_order_total_price(self, order: Order) -> int:
        """
        Calculate total price of a given order.

        Args:
            order (Order): Order to calculate price for

        Returns:
            int: Total price of given order
        """

        total = 0
        for i in range(len(order.prices)):
            total += order.quantities[i] * order.prices[i]
        return total

    def process_order(self, order: Order) -> None:
        """
        Process order for payment and shipping.

        Args:
            order (Order): Order to process
        """
        self.payment_processor.process_payment(order.id)
        order.set_status(OrderStatus.PAID)
        print("Shipping order to customer.")
