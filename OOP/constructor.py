class Car:
    brand="BMW"
    def __init__(self,price,colour,power):
        self.price=price
        self.colour=colour
        self.power=power

    def __repr__(self):
        return f'This is my car name {self.brand} and my car price is{self.price} and my car colour is {self.colour} and last is my car power is{self.power}'   

    def send_sms(self,number,sms):
        text=f'sending sms to {number} and sms is {sms}'
        print(text)


MyCar=Car(20000,"Black",1033)
print(MyCar)
MyCar.send_sms(1780942672,"helloe world")
