class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.booked_tables = []
        self.customer_orders = []

    def add_item_to_menu(self, item_name, item_price):
        self.menu_items[item_name] = item_price

    def book_table(self, table_number):
        if table_number not in self.booked_tables:
            self.booked_tables.append(table_number)
            print(f"Table {table_number} has been booked.")
        else:
            print(f"Table {table_number} is already booked.")

    def customer_order(self, table_number, order):
        if table_number in self.booked_tables:
            self.customer_orders.append({"table_number": table_number, "order": order})
            print(f"Order for table {table_number} has been placed.")
        else:
            print(f"Table {table_number} is not booked. Please book a table first.")

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")

    def print_booked_tables(self):
        print("Booked Tables:")
        for table in self.booked_tables:
            print(f"Table {table} is booked.")

    def print_customer_orders(self):
        print("Customer Orders:")
        for order in self.customer_orders:
            print(f"Table {order['table_number']} ordered: {order['order']}")

# Create an instance of the Restaurant class
my_restaurant = Restaurant()

# Add items to the menu
my_restaurant.add_item_to_menu("Burger", 10.99)
my_restaurant.add_item_to_menu("Pizza", 12.99)
my_restaurant.add_item_to_menu("Salad", 7.99)

# Book tables
my_restaurant.book_table(1)
my_restaurant.book_table(2)
my_restaurant.book_table(1)  # Try to book the same table again

# Take customer orders
my_restaurant.customer_order(1, "Burger and Fries")
my_restaurant.customer_order(2, "Pizza and Coke")
my_restaurant.customer_order(3, "Soup and Salad")  # Try to order from an unbooked table

# Print menu, booked tables, and customer orders
my_restaurant.print_menu()
my_restaurant.print_booked_tables()
my_restaurant.print_customer_orders()