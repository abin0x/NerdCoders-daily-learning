class Phone:
    price=1000
    colour="black"
    brand="Samsung"
    model="Galaxy S10"

    def __repr__(self):
        return f"Phone price is {self.price} and colour is {self.colour} and brand is {self.brand} and model is {self.model}"
my_phone1=Phone()
my_phone2=Phone()
Phone.price=7000
print(my_phone1)
print(my_phone2)
