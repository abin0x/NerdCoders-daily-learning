class Device:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
        print(f"{self.brand} is running")

class Laptop(Device):  # Inherited from Device
    def __init__(self, brand, price, color, memory):
        super().__init__(brand, price, color)
        self.memory = memory

    def coding(self):
        return 'Learning practice start'

class Phone(Device):
    def __init__(self, brand, price, color, dual_sim):
        super().__init__(brand, price, color)  # Fixed `super()`
        self.dual_sim = dual_sim

    def phone_call(self, number, text):
        return f'Sending SMS to {number}: {text}'

    def __repr__(self):
        return f"Phone({self.brand}, {self.price}, {self.color}, Dual SIM: {self.dual_sim})"

class Camera(Device):  # Inherited from Device
    def __init__(self, brand, price, color, resolution):
        super().__init__(brand, price, color)
        self.resolution = resolution

# Corrected instantiation
myphn = Phone('Samsung', 20000, 'black', True)
print(myphn)
print(myphn.brand)
