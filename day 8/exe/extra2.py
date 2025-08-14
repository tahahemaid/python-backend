class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.__price = price  
        self.quantity = quantity

    
    def apply_discount(self, percent):
        if 0 < percent < 100:
            discount_amount = self.__price * (percent / 100)
            self.__price -= discount_amount
            print(f"Discount applied: {percent}% off. New price: ${self.__price:.2f}")
        else:
            print("Invalid discount percentage.")

    
    def restock(self, amount):
        if amount > 0:
            self.quantity += amount
            print(f"Restocked {amount} units. Total quantity: {self.quantity}")
        else:
            print("Restock amount must be positive.")

    
    def _get_price(self):
        return self.__price

    
    def _set_price(self, value):
        self.__price = value

    
    def __add__(self, other):
        if isinstance(other, Product) and self.product_id == other.product_id:
            total_quantity = self.quantity + other.quantity
            return Product(self.product_id, self.name, self.__price, total_quantity)
        raise ValueError("Can only add products with the same ID.")

    
    def __call__(self):
        return f"Product {self.product_id}: {self.name}, Price: ${self.__price:.2f}, Quantity: {self.quantity}"

    
    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - ${self.__price:.2f} [{self.quantity} in stock]"



class DigitalProduct(Product):
    def __init__(self, product_id, name, price, quantity, file_size):
        super().__init__(product_id, name, price, quantity)
        self.file_size = file_size  


    def apply_discount(self, percent):
        if percent > 20:
            print("Max discount for digital products is 20%. Applying 20%.")
            percent = 20
        super().apply_discount(percent)



class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, quantity, weight):
        super().__init__(product_id, name, price, quantity)
        self.weight = weight  


    def apply_discount(self, percent):
        original_price = self._get_price()
        new_price = original_price - (original_price * (percent / 100))
        if new_price < 5:
            print("Discount too high. Price cannot go below $5.")
        else:
            super().apply_discount(percent)



if __name__ == "__main__":

    ebook = DigitalProduct("D001", "Python Mastery", 50, 100, file_size=500)
    laptop = PhysicalProduct("P001", "Gaming Laptop", 1500, 5, weight=2.5)


    ebook.apply_discount(25)
    laptop.apply_discount(80) 
    laptop.apply_discount(10) 
    
    
    
    laptop.restock(3)

    
    print(ebook())
    print(laptop)   

    more_ebooks = DigitalProduct("D001", "Python Mastery", 50, 50, file_size=500)
    combined_ebooks = ebook + more_ebooks
    print(combined_ebooks())  
