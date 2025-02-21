class Order:
    def __init__(self):
        self.items={}
    def add_item(self,item):
        if item in self.items:
            self.items[item]+=item.quntity
        else:
            self.items[item]=item.quntity
    def remove_item(self,item):
        if item in self.items:
            del self.items[item]
    @property
    def get_total_price(self):
        return sum(item.price*quantity for item,quantity in self.items.items())
    def clear(self):
        self.items={}
    
    def place_order(self):
        if not self.items:
            print("Your cart is empty!")
            return
        total = self.get_total_price
        print(f"Order placed successfully! Total price: {total}")
        self.clear()  # Optionally clear the cart after order is placed


# class Employee(User):