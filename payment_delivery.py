from abc import ABC, abstractmethod
from order import Order

# Abstraction: Base payment interface
class Payment(ABC):
    def __init__(self, amount: float):
        self.amount = amount

    @abstractmethod
    def process_payment(self) -> bool:
        pass


# Polymorphism: Concrete payment behaviors
class CashOnDelivery(Payment):
    def process_payment(self) -> bool:
        print(f"Payment Mode: Cash on Delivery | Total Due: PHP {self.amount:.2f}")
        return True


class CardPayment(Payment):
    def __init__(self, amount: float, card_number: str):
        super().__init__(amount)
        self.masked_card = f"****-****-****-{card_number[-4:]}"

    def process_payment(self) -> bool:
        print(f"Authorizing PHP {self.amount:.2f} via Card {self.masked_card}... Success.")
        return True


class DeliveryTracker:
    def __init__(self, order: Order):
        self.order = order
        self.status = "Pending"

    def update_status(self, new_status: str):
        self.status = new_status
        print(f"[Tracker] Order #{self.order.order_id} Status: {self.status}")