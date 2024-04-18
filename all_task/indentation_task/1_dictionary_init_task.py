class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        self.items[item_id] = {
            'item_name': item_name,
            'stock_count': stock_count,
            'price': price
        }

    def update_item(self, item_id, stock_count, price):
        if item_id in self.items:
            self.items[item_id]['stock_count'] = stock_count
            self.items[item_id]['price'] = price

    def check_item_details(self, item_id):
        if item_id in self.items:
            return self.items[item_id]
        else:
            return None

# Example usage:
inventory = Inventory()
inventory.add_item('001', 'Apple', 10, 1.99)
inventory.add_item('002', 'Orange', 5, 0.99)

print(inventory.check_item_details('001'))
inventory.update_item('001', 15, 2.49)
print(inventory.check_item_details('001'))

print(inventory.check_item_details('003'))
