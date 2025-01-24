"""
Question3: Create a "Shape" class. Under this class, create two subclasses, the "Rectangle" and "Square" classes.

Let the "shape" class have two properties: "width" and "height."
Let the "Rectangle" class inherit from the "Shape" class and add an additional "calculate_area()" method.
Let the "Square" class inherit from the "Shape" class and calculate the area of ​​the square using the same "area_calculate()" method.
Create a "Rectangle" and a "Square" instance, determine the width and height of each, and calculate the area of ​​each and print the results.

"""
"""
Soru3: Bir “Şekil” sınıfı oluşturun. Bu sınıfın altında, “Dikdörtgen” ve “Kare” sınıfları olmak üzere iki alt sınıf oluşturun.

“Shape” sınıfının iki özelliği olsun: “genişlik” ve ‘yükseklik’.
“Dikdörtgen” sınıfı ‘Shape’ sınıfından miras alsın ve ek bir ‘Calculate_surface()’ yöntemi eklesin.
“Kare” sınıfı ‘Shape’ sınıfından miras alsın ve aynı ‘calculate_area()’ yöntemiyle karenin alanını hesaplasın.
Bir “Dikdörtgen” ve bir “Kare” örneği oluşturun, her birinin genişliğini ve yüksekliğini belirleyin, her birinin alanını hesaplayın ve sonuçları yazdırın.

"""
# Temel Shape sınıfı
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

# Rectangle (Dikdörtgen) sınıfı
class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height

# Square (Kare) sınıfı
class Square(Shape):
    def calculate_area(self):
        return self.width * self.width  

# Rectangle ve Square nesneleri oluşturuyoruz
rectangle = Rectangle(5, 7)  # Dikdörtgen: genişlik 5, yükseklik 7
square = Square(4, 4)       # Kare: genişlik ve yükseklik 4

# Alanları hesapla ve yazdır
print("Rectangle Area:", rectangle.calculate_area())
print("Square Area:", square.calculate_area())
