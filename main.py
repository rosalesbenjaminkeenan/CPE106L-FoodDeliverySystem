from customer import CustomerManager
from menu import Menu, FoodItem, BeverageItem
from order import Order
from payment_delivery import CardPayment, DeliveryTracker

def main():
    print("========================================")
    print("   FOOD DELIVERY MANAGEMENT SYSTEM     ")
    print("========================================")

    # 1. Customer Management
    cust_mgr = CustomerManager()
    customer = cust_mgr.register_customer(101, "Benjamin Rosales", "Muralla St, Intramuros, Manila", "09123456789")
    print(f"Customer Registered: {customer.get_details()}")

    # 2. Menu Management
    restaurant_menu = Menu()
    restaurant_menu.add_item(FoodItem(1, "Chicken Adobo Rice Bowl", 140.00, "1 Pax"))
    restaurant_menu.add_item(FoodItem(2, "Cheeseburger Deluxe", 120.00, "Solo"))
    restaurant_menu.add_item(BeverageItem(3, "Iced Green Tea", 65.00, 500))
    restaurant_menu.display_menu()

    # 3. Order Processing
    order = Order(5001, customer)
    order.add_order_item(restaurant_menu.get_item(1), 2)
    order.add_order_item(restaurant_menu.get_item(3), 1)
    order.display_order_summary()

    # 4. Payment & Delivery Management
    total = order.calculate_total()
    payment = CardPayment(total, "4111111111114321")
    if payment.process_payment():
        order.is_paid = True
        tracker = DeliveryTracker(order)
        tracker.update_status("Order Confirmed & Preparing")
        tracker.update_status("Out for Delivery")
        tracker.update_status("Delivered Successfully to Muralla St")

    print("\nTransaction Complete.")

if __name__ == "__main__":
    main()