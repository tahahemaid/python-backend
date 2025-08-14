class MenuItem:
   
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display(self):
       
        return f"{self.name} ({self.category}) - ${self.price:.2f}"


class Order:
    
    def __init__(self):
        self.items = []

    def add_item(self, item):
        
        self.items.append(item)
        print(f"Added '{item.name}' to the order.")

    def remove_item(self, name):
        
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"Removed '{item.name}' from the order.")
                return
        print(f"No item named '{name}' found in the order.")

    def calculate_total(self):
        
        return sum(item.price for item in self.items)

    def display_order(self):
        
        if not self.items:
            print("Order is empty.")
            return

        print("Order details:")
        for item in self.items:
            print(f" - {item.display()}")

        total = self.calculate_total()
        print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    item1 = MenuItem("Mashed Poteto", 27.99, "Appetizer")
    item2 = MenuItem("Grilled Ribeye", 109.99, "Main Course")
    item3 = MenuItem("Cheesecake", 16.50, "Dessert")

    order = Order()

    order.add_item(item1)
    order.add_item(item2)
    order.add_item(item3)

    order.display_order()

    order.remove_item("Mashed Potato")

    order.display_order()