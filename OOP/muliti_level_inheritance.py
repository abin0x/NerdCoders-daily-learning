# Base Class: Vehicle
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def __repr__(self):
        print(f"{self.brand} is moving at {self.speed} km/h.")

# Intermediate Class: Car (Inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)  # Calling Vehicle's constructor
        self.fuel_type = fuel_type

    def refuel(self):
        print(f"{self.brand} runs on {self.fuel_type}.")

# Derived Class: ElectricCar (Inherits from Car)
class ElectricCar(Car):
    def __init__(self, brand, speed, battery_capacity):
        super().__init__(brand, speed, "Electric")  # Calling Car's constructor
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.brand} is charging. Battery capacity: {self.battery_capacity} kWh.")

# Object Creation
tesla = ElectricCar("Tesla Model 3", 200, 75)

# Calling methods from different levels of inheritance

tesla.refuel() # From Car
tesla.charge() # From ElectricCar
