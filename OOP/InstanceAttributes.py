class Car:
    def __init__(self, brand, color):
        self.brand = brand  # Instance Attribute
        self.color = color  # Instance Attribute

# দুটি আলাদা অবজেক্ট তৈরি
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

print(car1.brand)  # Toyota
print(car2.color)  # Blue
