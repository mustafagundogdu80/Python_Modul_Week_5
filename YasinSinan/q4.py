class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
class Off_Road_Vehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive=four_wheel_drive
    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
class Sport_Car(Vehicle):
    def __init__(self, make, model, year,max_speed):
        super().__init__(make, model, year )
        self.max_speed=max_speed
    def __str__ (self):
        return f"{self.make} {self.model} ({self.year})"
vehicle=Vehicle("Toyota", "corolla", 2015)
off_road_vehicle = Off_Road_Vehicle("Toyota", "Land Cruiser", 2015, True)
Sport_car = Sport_Car("Jaguar", "Spider", 1955, 200)
print(str(vehicle))
print(str(off_road_vehicle))
print(str(Sport_car))
