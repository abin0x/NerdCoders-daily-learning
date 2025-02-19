class Laptop:
    def __init__(self,brand,price,color,memory):
        self.brand=brand
        self.price=price
        self.color=color
        self.memory=memory

    def run(self):
        print(f"{self.brand} is running")
    def coding(self):
        return f'learning practice start'


class Phone:
    def __init__(self,brand,price,color,dual_sim):
        self.brand=brand
        self.price=price
        self.color=color
        self.dual_sim=dual_sim

    def phone_call(self,number,text):
        return f'sending SMS to : {number} with : {text}'
    
    def run(self):
        print(f"{self.brand} is running")


class Camera:
    def __init__(self,brand,price,color,resolution):
        self.brand=brand
        self.price=price
        self.color=color
        self.resolution=resolution

    def run(self):
        print(f"{self.brand} is running")