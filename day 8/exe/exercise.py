import math

class Shape:
    def __init__(self, color="Black"):
        self._color = color      
        self.__filled = True     

    def area(self):
        raise NotImplementedError("Subclasses must implement area() method.")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter() method.")

    def is_filled(self):
        return self.__filled

    def set_filled(self, filled):
        if isinstance(filled, bool):
            self.__filled = filled
        else:
            raise ValueError("filled must be a boolean.")

    def __str__(self):
        return f"{self.__class__.__name__}(Color: {self._color}, Filled: {self.__filled})"

    def __repr__(self):
        return f"{self.__class__.__name__}(color='{self._color}', filled={self.__filled})"

    def __add__(self, other):
        
        if isinstance(other, Shape):
            return CombinedShape(self.area() + other.area())
        return NotImplemented



class Circle(Shape):
    def __init__(self, radius, color="Black"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(Radius: {self.radius}, Color: {self._color}, Area: {self.area():.2f})"


class Rectangle(Shape):
    def __init__(self, width, height, color="Black"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(Width: {self.width}, Height: {self.height}, Color: {self._color}, Area: {self.area():.2f})"


class CombinedShape:
    def __init__(self, total_area):
        self.total_area = total_area

    def __str__(self):
        return f"CombinedShape(Total Area: {self.total_area:.2f})"

    def __repr__(self):
        return f"CombinedShape(total_area={self.total_area})"



def display_shape_info(shape):
    print(shape)
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print()



if __name__ == "__main__":
    circle = Circle(5, "Red")
    rect = Rectangle(4, 6, "Blue")

    for s in [circle, rect]:
        display_shape_info(s)

    combined = circle + rect
    print(combined)

    print("Circle filled?", circle.is_filled())
    circle.set_filled(False)
    print("Circle filled after change?", circle.is_filled())
