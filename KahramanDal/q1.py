#ANSWER1:
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
rectangle = Rectangle(5, 7)
print(rectangle.area())
print(rectangle.perimeter())
