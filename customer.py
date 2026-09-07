class Customer:
    def __init__(self, customer_id: int, name: str, address: str, phone: str):
        self.__customer_id = customer_id
        self.__name = name
        self.__address = address
        self.__phone = phone

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    def get_details(self) -> str:
        return f"[{self.__customer_id}] {self.__name} | Address: {self.__address} | Contact: {self.__phone}"


class CustomerManager:
    def __init__(self):
        self.customers = {}

    def register_customer(self, customer_id: int, name: str, address: str, phone: str) -> Customer:
        customer = Customer(customer_id, name, address, phone)
        self.customers[customer_id] = customer
        return customer

    def get_customer(self, customer_id: int) -> Customer:
        return self.customers.get(customer_id)