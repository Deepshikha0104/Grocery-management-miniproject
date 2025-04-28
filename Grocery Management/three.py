

class Grocery:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class GroceryManagementSystem:
    def __init__(self):
        self.groceries = []

    def add_grocery(self):
        name = input("Enter grocery name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        grocery = Grocery(name, quantity, price)
        self.groceries.append(grocery)
        print(f"Grocery '{name}' added successfully.")

    def remove_grocery(self):
        name = input("Enter grocery name: ")
        for grocery in self.groceries:
            if grocery.name == name:
                self.groceries.remove(grocery)
                print(f"Grocery '{name}' removed successfully.")
                return
        print(f"Grocery '{name}' not found.")

    def update_grocery(self):
        name = input("Enter grocery name: ")
        for grocery in self.groceries:
            if grocery.name == name:
                grocery.quantity = int(input("Enter new quantity: "))
                grocery.price = float(input("Enter new price: "))
                print(f"Grocery '{name}' updated successfully.")
                return
        print(f"Grocery '{name}' not found.")

    def display_groceries(self):
        print("Grocery List:")
        for i, grocery in enumerate(self.groceries, start=1):
            print(f"{i}. {grocery.name} - Quantity: {grocery.quantity}, Price: {grocery.price}")

    def search_grocery(self):
        name = input("Enter grocery name: ")
        for grocery in self.groceries:
            if grocery.name == name:
                print(f"Grocery '{name}' found.")
                print(f"Quantity: {grocery.quantity}, Price: {grocery.price}")
                return
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
            grocery_system.add_grocery()
        elif choice == '2':
            grocery_system.remove_grocery()
        elif choice == '3':
            grocery_system.update_grocery()
        elif choice == '4':
            grocery_system.display_groceries()
        elif choice == '5':
            grocery_system.search_grocery()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


