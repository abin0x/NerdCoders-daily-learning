from abc import ABC, abstractmethod

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
        
    
    


class Restaurent:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.employees=[]
        self.menu=Menu()
    
    def add_employee(self,employee):
        self.employees.append(employee)
        print(f'Add Employee {employee.name} Successfully')
    

    def view_employee(self):
        for emp in self.employees:
            print("----------------Employee Information----------------")
            print(f' Name       Email         Phone       Address  Age   Designation  Salary')
            print(f'{emp.name}  {emp.phon}  {emp.email}    {emp.addres}    {emp.age}      {emp._designation}    {emp.salary}')
            print("----------------------------------------------------")

class Menu:
    def __init__(self):
        self.items=[]
    def add_item(self,item):
        self.items.append(item)

    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    def remove_item(self,item_name):
        item=self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f'{item_name} Removed Successfully')
        else:
            print(f'{item_name} Not Found')
    
    def view_menu(self):
        print("----------------Menu Information----------------")
        print(f' Name       Price       Quantity')
        for item in self.items:
            print(f'{item.name}       {item.price}           {item.quntity}')
        print("----------------------------------------------------")

class FoodItem:
    def __init__(self,name,price,quntity):
        self.name=name
        self.price=price
        self.quntity=quntity

# add=Admin('Rahim','01700000000','abim@gmail.com','Dhaka')
# add.add_employee('Karim','karim@gmail.com','01700000001','Dhaka',25,'Manager',50000)
# add.view_employee()

mamar_desh=Restaurent('Mamar Desh','Dhaka')
mn=Menu()
item=FoodItem('Pizza',150,10)
item1=FoodItem('Pizza',150,20)
admin=Admin('Rahim','01700000000','abin@gmail.com','Dhaka')
admin.add_item(mamar_desh,item)
admin.add_item(mamar_desh,item1)

# mn.view_menu()
customer1=Customer('abin','01700000000','abin@gmail.com','Dhaka')
customer1.view_menu(mamar_desh)


item_name=input('Enter Item Name: ')
quantity=int(input('Enter Quantity: '))
customer1.add_to_cart(mamar_desh,item_name,quantity)
customer1.view_cart()