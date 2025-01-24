
# Question4: Create a "Vehicle" class in Python. Make sure this class has the following properties:

# Features:
# "make" (Brand of vehicle)
# "model" (Vehicle model)
# "year" (Year of manufacture of the vehicle)
# Create a "Vehicle" class and create two derived subclasses, "Off-Road Vehicle" (SUV) and "SportsCar" classes.

# The "Off-Road Vehicle" class inherits from the "Vehicle" class and adds an additional "four_wheel drive" feature.
# Let the "SportCar" class inherit from the "Vehicle" class and add a "max_speed" property.
# Create an instance of each class, determine its properties, and write a program to display these properties.


# Soru4: Python'da bir “Araç” sınıfı oluşturun. Bu sınıfın aşağıdaki özelliklere sahip olduğundan emin olun:

# Özellikler:
# “make” (Araç markası)
# “model” (Araç modeli)
# “yıl” (Aracın üretim yılı)
# Bir “Vehicle” sınıfı oluşturun ve “Off-Road Vehicle” (SUV) ve “SportsCar” sınıfları olmak üzere iki türetilmiş alt sınıf oluşturun.

# “Off-Road Vehicle” sınıfı ‘Vehicle’ sınıfından miras alır ve ek bir ‘four_wheel drive’ özelliği ekler.
# “SportCar” sınıfı ‘Vehicle’ sınıfından miras alsın ve bir ‘max_speed’ özelliği eklesin.
# Her sınıfın bir örneğini oluşturun, özelliklerini belirleyin ve bu özellikleri görüntülemek için bir program yazın.


# Temel Vehicle sınıfı
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
# Off-Road Vehicle (SUV) sınıfı
class OffRoadVehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive

# SportsCar sınıfı
class SportsCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed

# Off-Road Vehicle ve SportsCar nesneleri oluşturuuyoruz
suv = OffRoadVehicle("Jeep", "Wrangler", 2021, True)
sports_car = SportsCar("Ferrari", "488 Spider", 2023, 330)

print(f"Off-Road Vehicle: Make: {suv.make}, Model: {suv.model}, Year: {suv.year}, Four-Wheel Drive: {suv.four_wheel_drive}")
print(f"Sports Car: Make: {sports_car.make}, Model: {sports_car.model}, Year: {sports_car.year}, Max Speed: {sports_car.max_speed} km/h")
