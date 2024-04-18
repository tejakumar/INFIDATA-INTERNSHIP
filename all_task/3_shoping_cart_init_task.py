n1=10
n2=0
# Initialize an empty shopping cart as a list
shopping_cart = []


# Function to add an item to the shopping cart
def add_to_cart(item_name, item_price, item_quantity):
    item = {
        "name": item_name,
        "price": item_price,
        "quantity": item_quantity
    }
    shopping_cart.append(item)
    print(f"{item_quantity} {item_name}(s) added to the cart.")


# Function to calculate the total price of items in the cart
def calculate_total_price(cart):
    total_price = 0
    for item in cart:
        total_price += item["price"] * item["quantity"]
    return total_price


# Main program
while True:
    print("\nMenu:")
    print("1. Add item to cart")
    print("2. View cart")
    print("3. Calculate total price")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        item_name = input("Enter the name of the item: ")
        item_price = float(input("Enter the price of the item: "))
        item_quantity = int(input("Enter the quantity: "))
        add_to_cart(item_name, item_price, item_quantity)

    elif choice == "2":
        print("\nShopping Cart:")
        for item in shopping_cart:
            print(f"{item['name']} - Price: ${item['price']:.2f} - Quantity: {item['quantity']}")

    elif choice == "3":
        total_price = calculate_total_price(shopping_cart)
        print(f"Total price of items in the cart: ${total_price:.2f}")

    elif choice == "4":
        print("Thank you for shopping with us!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")