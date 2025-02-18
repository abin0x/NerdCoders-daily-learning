class Car:
    wheels = 4  # Class Attribute (সব কারের জন্য একটাই থাকবে)

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

print(car1.wheels)  # 4
print(car2.wheels)  # 4

# Class Attribute পরিবর্তন করলে সব অবজেক্টে প্রভাব পড়বে
Car.wheels = 6
print(car1.wheels)  # 6
print(car2.wheels)  # 6
