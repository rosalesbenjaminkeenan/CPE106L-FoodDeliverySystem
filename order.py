from menu import MenuItem
from customer import Customer

class OrderItem:
    def __init__(self, item: MenuItem, quantity: int):
        self.item = item
        self.quantity = quantity

    def calculate_subtotal(self) -> float:
        return self.item.price * self.quantity


class Order:
    def __init__(self, order_id: int, customer: Customer):
        self.order_id = order_id
        self.customer = customer
        self.order_items = []
        self.is_paid = False

    def add_order_item(self, item: MenuItem, quantity: int):
        if quantity > 0:
            self.order_items.append(OrderItem(item, quantity))

    def calculate_total(self) -> float:
        return sum(oi.calculate_subtotal() for oi in self.order_items)

    def display_order_summary(self):
        print(f"\nOrder #{self.order_id} Summary | Customer: {self.customer.name}")
        print(f"Deliver to: {self.customer.address}")
        for oi in self.order_items:
            print(f" - {oi.item.name} x {oi.quantity} @ PHP {oi.item.price:.2f} = PHP {oi.calculate_subtotal():.2f}")
        print(f"Total Amount: PHP {self.calculate_total():.2f}")