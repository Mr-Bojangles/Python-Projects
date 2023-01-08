"""
Main module to instatiate a point-of-sale system.

Class(es):
    None

Function(s):
    main -> None
"""

from pos_system.customer import Customer
from pos_system.line_item import LineItem
from pos_system.order import Order
from pos_system.payment import StripePaymentProcessor
from pos_system.system import POSSystem


def main() -> None:
    """
    Module run function.
    """

    payment_processor = StripePaymentProcessor.create("https://api.stripe.com/v2")
    system = POSSystem(payment_processor)

    customer = Customer(
        id=12345,
        name="Craig",
        address="100 Any St.",
        postal_code="00001",
        city="Anywhere",
        email="junk@email.com",
    )

    order = Order(customer)

    order.add_line_item(LineItem(item="Keyboard", quantity=1, price=5_000))
    order.add_line_item(LineItem(item="SSD", quantity=1, price=15_000))
    order.add_line_item(LineItem(item="USB 3 Cable", quantity=3, price=500))

    system.register_order(order)
    system.process_order(order)


if __name__ == "__main__":
    main()
