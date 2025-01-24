# ANSWER4:
class Vehicle:
    def __init__(self,make,model,year):
        self.make = make 
        self.model = model
        self.year = year
class OffRoadVehicle(Vehicle):
        def __init__(self, make, model, year, four_wheel_drive):
            super().__init__(make, model, year)
            self.four_wheel_drive = four_wheel_drive
class SportsCar(Vehicle):
        def __init__(self, make, model, year, max_speed):
            super(SportsCar,self).__init__(make, model, year)
            self.max_speed = max_speed
vehicle = Vehicle("Toyota", "Corolla", 2015)
off_road_vehicle = OffRoadVehicle("Toyota", "Land Cruiser", 2022, True)
sports_car = SportsCar("Toyota", "Supra", 2023, 300)
print(f"Vehicle: {vehicle.make} {vehicle.model} ({vehicle.year})")
print(f"Off-Road Vehicle: {off_road_vehicle.make} {off_road_vehicle.model} ({off_road_vehicle.year}), Four-Wheel Drive: {off_road_vehicle.four_wheel_drive}")
print(f"Sports Car: {sports_car.make} {sports_car.model} ({sports_car.year}), Max Speed: {sports_car.max_speed} km/h")
