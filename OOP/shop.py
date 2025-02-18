class Shop:
    cart=[]

    def __init__(self,buyer):
        self.buyer=buyer

    def addToCart(self,item):
        self.cart.append(item)


abinShop=Shop("hasan")
abinShop.addToCart("tea")
abinShop.addToCart("watch")
abinShop.addToCart("t shirt")
print(abinShop.cart)
nishu=Shop("Mahmudul")
nishu.addToCart("pant")
nishu.addToCart("touser")
print(nishu.cart)