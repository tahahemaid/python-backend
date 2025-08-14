class Car:
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1 

    def display_car(self):
        return f"Car: {self.make} {self.model}"

    @staticmethod
    def get_total_cars():
        return Car.total_cars


car1 = Car("GMC", "YUKON")
car2 = Car("CHEVE", "TAHOE")
car3 = Car("CADILAC", "ESCALED")

print(car1.display_car())
print(car2.display_car())
print(car3.display_car())
print(f"Total cars created: {Car.get_total_cars()}")
