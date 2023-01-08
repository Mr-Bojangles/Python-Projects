"""
Module for defining and connecting to a payment processor.

Class(es):
    PaymentServiceConnectionError
    OrderRepository
    StripePaymentProcessor

Function(s):
    None
"""

from typing import Protocol

from pos_system.order import Order


class PaymentServiceConnectionError(Exception):
    """Custom error that is raised when we can't connect to the payment service."""


class OrderRepository(Protocol):
    """
    Interface for an order repository.
    """

    def find_order(self, order_id: str) -> Order:
        """
        Find an order with a given ID.

        Args:
            order_id (str): ID of order to be found

        Returns:
            Order
        """

    def compute_order_total_price(self, order: Order) -> int:
        """
        Calculate the total price of an order.

        Args:
            order (Order): Order to calculate price for

        Returns:
            int: Total price of the order
        """


class StripePaymentProcessor:
    """
    Class for connecting to and processing payments with Stripe.

    Attribute(s):
        connected (bool): Connection status
        system (OrderRepository): Order repository for order payment processing
    """

    def __init__(self, system: OrderRepository) -> None:
        self.connected = False
        self.system = system

    def connect_to_service(self, url: str) -> None:
        """
        Connect to payment processor.

        Args:
            url (str): Address of payment processor
        """

        print(f"Connecting to payment processing service at url {url}... done!")
        self.connected = True

    def process_payment(self, order_id: str) -> None:
        """
        Process payment for a given order.

        Args:
            order_id (str): ID of order to process for payment

        Raises:
            PaymentServiceConnectionError
        """

        if not self.connected:
            raise PaymentServiceConnectionError()
        order = self.system.find_order(order_id)
        total_price = self.system.compute_order_total_price(order)
        print(
            f"Processing payment of ${(total_price / 100):.2f}, reference: {order.id}."
        )
