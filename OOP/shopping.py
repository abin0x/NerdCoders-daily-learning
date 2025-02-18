class Shopping:
    def __init__(self,name):
        self.name=name
        self.cart=[]

    def add_to_cart(self,item,price,quantity):
        product={'item' :item,'price':price,'quantity':quantity}
        self.cart.append(product)
    def checkout(self,amount):
        total=0
        for item in self.cart:
            # print(item)
            total+=item['price']*item['quantity']
        print("total Price is : ",total)
        if amount<total:
            print(f"You give me more mone {total-amount}")
        else:
            print(f"Your extra money is {amount-total}")

she=Shopping("Girl")
she.add_to_cart("sharee",500,3)
she.add_to_cart("makeup",100,2)
she.add_to_cart("lipstic",200,1)
print(she.cart)
she.checkout(1000)