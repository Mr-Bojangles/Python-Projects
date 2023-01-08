"""
Main module to instatiate a point-of-sale system.

Class(es):
    None

Function(s):
    main -> None
"""

from pos_system.order import Order
from pos_system.system import POSSystem


def main() -> None:
    """
    Module run function.
    """

    system = POSSystem()
    system.setup_payment_processor("https://api.stripe.com/v2")

    order = Order(12345, "Craig", "100 Any St.", "00001", "Anywhere", "junk@email.com")

    order.create_line_item("Keyboard", 1, 5_000)
    order.create_line_item("SSD", 1, 15_000)
    order.create_line_item("USB 3 Cable", 3, 500)

    system.register_order(order)
    system.process_order(order)


if __name__ == "__main__":
    main()
