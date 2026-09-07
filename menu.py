class MenuItem:
    def __init__(self, item_id: int, name: str, price: float):
        self.item_id = item_id
        self.name = name
        self.price = price

    def get_info(self) -> str:
        return f"[{self.item_id}] {self.name} - PHP {self.price:.2f}"


class FoodItem(MenuItem):
    def __init__(self, item_id: int, name: str, price: float, serving_size: str):
        super().__init__(item_id, name, price)
        self.serving_size = serving_size

    def get_info(self) -> str:
        return f"[{self.item_id}] {self.name} ({self.serving_size}) - PHP {self.price:.2f}"


class BeverageItem(MenuItem):
    def __init__(self, item_id: int, name: str, price: float, volume_ml: int):
        super().__init__(item_id, name, price)
        self.volume_ml = volume_ml

    def get_info(self) -> str:
        return f"[{self.item_id}] {self.name} ({self.volume_ml}ml) - PHP {self.price:.2f}"


class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, item: MenuItem):
        self.items[item.item_id] = item

    def get_item(self, item_id: int) -> MenuItem:
        return self.items.get(item_id)

    def display_menu(self):
        print("\n--- RESTAURANT MENU ---")
        for item in self.items.values():
            print(item.get_info())