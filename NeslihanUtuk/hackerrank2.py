"""
Classes: Dealing with Complex Numbers: https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
"""
# import math

# class Complex(object):
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary
#     def __add__(self, no):
#         #(a + bi)+(c + di) = (a+c) +(b+d)i
#         return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
#     def __sub__(self, no):
#         #(a+bi)-(c+di)=(a-c)+(b-d)i
#         return Complex(self.real-no.real, self.imaginary - no.imaginary)
#     def __mul__(self, no):
#         #(a + bi) x (c + di) = (ac - bd)+(ad + bc)i
#         return Complex((self.real * no.real) - (self.imaginary * no.imaginary), (self.real * no.imaginary)+(self.imaginary* no.real) )

#     def __truediv__(self, no):
#         # (a + bi)/ (c + di) = ((ac+bd)/(c**2 + d**2))+((bc-ad)/(c**2 + d**2))
#         return Complex(((self.real*no.real)+(self.imaginary * no.imaginary))/(no.real **2 + no.imaginary **2),((self.imaginary * no.real) - (self.real * no.imaginary))/(no.real**2 + no.imaginary**2))

#     def mod(self):
#          # (a**2 + b**2)**0,5
#         return Complex(math.sqrt(self.real**2 + self.imaginary**2),0)

#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result

# if __name__ == '__main__':
#     c = map(float, input().split())
#     d = map(float, input().split())
#     x = Complex(*c)
#     y = Complex(*d)
#     print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        # (a + bi) + (c + di) = (a + c) + (b + d)i
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        # (a + bi) - (c + di) = (a - c) + (b - d)i
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        # (a + bi) × (c + di) = (ac - bd) + (ad + bc)i
        return Complex((self.real * no.real) - (self.imaginary * no.imaginary),
                       (self.real * no.imaginary) + (self.imaginary * no.real))

    def __truediv__(self, no):
        # (a + bi) ÷ (c + di) = [(ac + bd) / (c² + d²)] + [(bc - ad) / (c² + d²)]i
        denominator = no.real**2 + no.imaginary**2
        return Complex(((self.real * no.real) + (self.imaginary * no.imaginary)) / denominator,
                       ((self.imaginary * no.real) - (self.real * no.imaginary)) / denominator)

    def mod(self):
        # |a + bi| = √(a² + b²)
        return Complex((self.real**2 + self.imaginary**2)**0.5, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())  # Birinci kompleks sayı
    d = map(float, input().split())  # İkinci kompleks sayı
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
