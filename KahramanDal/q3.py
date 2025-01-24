# ANSWER3:
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
class Rectangle(Shape):
    def calculate_area(self):
        return self.width*self.height
    
class Square(Shape):
    def calculate_area(self):
        if self.width != self.height:
            raise ValueError("The width and height of a square must be equal.")
        return self.width*self.height
    
Rectangle1 = Rectangle(5,7)
Rectangle_area = Rectangle1.calculate_area()
print(f"Rectangle area: {Rectangle_area}")
Square1 = Square(5,5)
Square_area = Square1.calculate_area()
print(f"Square area: {Square_area}")
