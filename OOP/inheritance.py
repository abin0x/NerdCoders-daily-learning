class device:
    def __init__(self,brand,price,color):
        self.brand=brand
        self.price=price
        self.color=color
    def run(self):
        print(f"{self.brand} is running")

class Laptop:
    def __init__(self,memory):
        self.memory=memory
    def coding(self):
        return f'learning practice start'


class Phone:
    def __init__(self,dual_sim):
        self.dual_sim=dual_sim

    def phone_call(self,number,text):
        return f'sending SMS to : {number} with : {text}'



class Camera:
    def __init__(self,resolution):
        self.resolution=resolution
