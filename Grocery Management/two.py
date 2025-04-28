class GroceryManagementSystem:
    def __init__(self):
        self.grocery_list = {}

    def add_grocery(self, name, quantity, price):
        if name in self.grocery_list:
            print("Grocery already exists. Updating quantity and price.")
            self.grocery_list[name]['quantity'] += quantity
            self.grocery_list[name]['price'] = price
        else:
            self.grocery_list[name] = {'quantity': quantity, 'price': price}
        print(f"Grocery '{name}' added successfully.")

    def remove_grocery(self, name):
        if name in self.grocery_list:
            del self.grocery_list[name]
            print(f"Grocery '{name}' removed successfully.")
        else:
            print(f"Grocery '{name}' not found.")

    def update_grocery(self, name, quantity=None, price=None):
        if name in self.grocery_list:
            if quantity:
                self.grocery_list[name]['quantity'] = quantity
            if price:
                self.grocery_list[name]['price'] = price
            print(f"Grocery '{name}' updated successfully.")
        else:
            print(f"Grocery '{name}' not found.")

    def display_groceries(self):
        print("Grocery List:")
        for name, details in self.grocery_list.items():
            print(f"Name: {name}, Quantity: {details['quantity']}, Price: {details['price']}")

    def search_grocery(self, name):
        if name in self.grocery_list:
            print(f"Grocery '{name}' found.")
            print(f"Quantity: {self.grocery_list[name]['quantity']}, Price: {self.grocery_list[name]['price']}")
        else:
            print(f"Grocery '{name}' not found.")

def main():
    grocery_system = GroceryManagementSystem()

    while True:
        print("\nGrocery Management System")
        print("1. Add Grocery")
        print("2. Remove Grocery")
        print("3. Update Grocery")
        print("4. Display Groceries")
        print("5. Search Grocery")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter grocery name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            grocery_system.add_grocery(name, quantity, price)
        elif choice == '2':
            name = input("Enter grocery name: ")
            grocery_system.remove_grocery(name)
        elif choice == '3':
            name = input("Enter grocery name: ")
            quantity = input("Enter new quantity (press enter to skip): ")
            price = input("Enter new price (press enter to skip): ")
            quantity = int(quantity) if quantity else None
            price = float(price) if price else None
            grocery_system.update_grocery(name, quantity, price)
        elif choice == '4':
            grocery_system.display_groceries()
        elif choice == '5':
            name = input("Enter grocery name: ")
            grocery_system.search_grocery(name)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# This system provides the following features:

# - Add grocery items with quantity and price
# - Remove grocery items
# - Update grocery items (quantity and price)
# - Display all grocery items
# - Search for a specific grocery item

# You can run the code and follow the menu-driven interface to manage your grocery list.