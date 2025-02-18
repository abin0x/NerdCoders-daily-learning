class NewShop:
    shopingMallname="Jamuna"

    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[] # cart is an instance att

    def add_to_cart(self,item):
        self.cart.append(item)


newMall=NewShop("helloBuyer")

newMall.add_to_cart("watch")
newMall.add_to_cart("shirt")
newMall.add_to_cart("pant")
print(newMall.cart)

againOne=NewShop("Newbuyer")
againOne.add_to_cart("mobile")
againOne.add_to_cart("camera")
againOne.add_to_cart("laptop")
print(againOne.cart)


    