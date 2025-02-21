from abc import ABC, abstractmethod
from orders import Order

class User(ABC):
    def __init__(self,name,phon,email,addres):
        self.name = name
        self.phon = phon
        self.email = email
        self.addres = addres


class Customer(User):
    def __init__(self,name,phon,email,addres):
        super().__init__(name,phon,email,addres)
        self.cart=Order()

    def view_menu(self,restaurent):
        restaurent.menu.view_menu()

    def add_to_cart(self,restaurent,item_name,quantity):
        item=restaurent.menu.find_item(item_name)
        if item:
            if item.quntity<quantity:
                print(f'Sorry Boss!!! Only {item.quntity} {item_name} Available')
                return 
            else:
                item.quntity=quantity
                self.cart.add_item(item)
                print(f'{item_name} Added To Cart Successfully')
        else:
            print(f'{item_name} Not Found')
    
    def view_cart(self):
        print("----------------Cart Information----------------")
        print(f' Name       Price       Quantity')
        for item ,quantity in self.cart.items.items():
            print(f'{item.name}       {item.price}           {quantity}')
        print("----------------------------------------------------")
        print(f'Total Price: {self.cart.get_total_price}')
    
    def place_order(self):
        print(f'Total Price : {self.cart.get_total_price} and Your Order Placed Successfully')
        self.cart.clear()



class Employee(User):
    def __init__(self,name,phon,email,addres,age,designation,salary):
        self._designation = designation
        self.salary = salary
        self.age = age
        super().__init__(name,phon,email,addres)


class Admin(User):
    def __init__(self,name,phon,email,addres):
        super().__init__(name,phon,email,addres)
    def add_employee(self,restaurent,employee):
        restaurent.add_employee(employee)
    
    def view_employee(self,restaurent):
        restaurent.view_employee()
    
    def add_item(self,restaurent,item):
        restaurent.menu.add_item(item)
    
    def remove_item(self,restaurent,item_name):
        restaurent.menu.remove_item(item_name)

    def view_menu(self,restaurent):
        restaurent.menu.view_menu()
        