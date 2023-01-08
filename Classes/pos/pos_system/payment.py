"""
Module for defining and connecting to a payment processor.

Class(es):
    PaymentServiceConnectionError
    StripePaymentProcessor

Function(s):
    None
"""

from __future__ import annotations


class PaymentServiceConnectionError(Exception):
    """Custom error that is raised when we can't connect to the payment service."""


class StripePaymentProcessor:
    """
    Class for connecting to and processing payments with Stripe.

    Attribute(s):
        connected (bool): Connection status
        system (OrderRepository): Order repository for order payment processing
    """

    def __init__(self) -> None:
        self.connected = False

    # Use __future__.annotations so that interpreter can recognize types that haven't been annotated
    # In this case, returning type StripePaymentProcessor before it is instantiated
    @staticmethod
    def create(url: str) -> StripePaymentProcessor:
        """
        Create a connection to payment processor.

        FUTURE: Separating the connection object from the POS system like this can allow for
        async operations.

        Args:
            url (str): Address of payment processor

        Returns:
            StripePaymentProcessor: Connection object for payment processor
        """

        obj = StripePaymentProcessor()
        obj.connect_to_service(url)
        return obj

    def connect_to_service(self, url: str) -> None:
        """
        Connect to payment processor.

        Args:
            url (str): Address of payment processor
        """

        print(f"Connecting to payment processing service at url {url}... done!")
        self.connected = True

    def process_payment(self, reference: str, price: int) -> None:
        """
        Process payment for a given order.

        Args:
            reference (str): ID of order to process for payment
            price (int): Total price of an order

        Raises:
            PaymentServiceConnectionError
        """

        if not self.connected:
            raise PaymentServiceConnectionError()
        print(f"Processing payment of ${(price / 100):.2f}, reference: {reference}.")
