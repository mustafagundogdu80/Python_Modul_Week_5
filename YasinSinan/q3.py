class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def calculate_area(self):
        return self.width * self.height

rectangle = Rectangle(4, 5)
square = Square(3, 3)


print(f"Rectangle area: {rectangle.calculate_area()}")
print(f"Square area : {square.calculate_area()}")
