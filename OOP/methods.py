def call():
    print("Called from methods.py")
    return "Calledsss from methods.py"

class Phone:
    price=1000
    colour="black"
    brand="apple"
    model="iPhone 11"

    def __repr__(self):
        return f"Phone price is {self.price} and colour is {self.colour} and brand is {self.brand} and model is {self.model}"

    def call(self):
        print("Hello abin,Called from methods.py")
        # return "Called from methods.py"    

my_phone=Phone()
print(my_phone)
call()
my_phone.call()