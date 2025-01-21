class rectangle:
    def __init__(self,width, height ):
        self.width=width
        self.height=height
    def perimeter(self):
        return 2*(self.width+self.height)
    def area(self):
        return self.width*self.height
rect = rectangle(5, 7)
print("Area:", rect.area())

rect= rectangle(5,7)
print ("perimeter:", rect.perimeter())









