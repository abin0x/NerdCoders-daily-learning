from food_item import FoodItem
from menu import Menu
from retaurent import Restaurent

from users import Employee, Customer, Admin
from orders import Order 
mamar_restaurent=Restaurent(name='Mamar Restaurent',location='Kathmandu')

def customer_menu():
    name=input('Enter Your Name: ')
    phon=input('Enter Your Phone Number: ')
    email=input('Enter Your Email: ')
    addres=input('Enter Your Address')
    customer=Customer(name=name,phon=phon,email=email,addres=addres)
    while True:
        print(f"Welcome {customer.name}")
        print("1. View Menu")
        print("2. Add To Cart")
        print("3. View Cart")
        print("4. Place Order")
        print("5. Exit")
        choice=input('Enter Your Choice: ')
        if choice=='1':
            customer.view_menu(mamar_restaurent)

        elif choice=='2':
            item_name=input('Enter Item Name: ')
            quantity=int(input('Enter Quantity: '))
            customer.add_to_cart(mamar_restaurent,item_name,quantity)

        elif choice=='3':
            customer.view_cart()

        elif choice=='4':
            customer.cart.place_order()
            break

        elif choice=='5':
            break

        else:
            print('Invalid Choice')


def admin_menu():
    name=input('Enter Your Name: ')
    phon=input('Enter Your Phone Number: ')
    email=input('Enter Your Email: ')
    addres=input('Enter Your Address')
    admin=Admin(name=name,phon=phon,email=email,addres=addres)


    while True:
        print(f"Welcome {admin.name}")
        print("1. Add Employee") # Add Employee to Restaurent
        print("2. View Employee") # View Employee of Restaurent
        print("3. Add Item") # Add Item to Menu
        print("4. View Menu") # View Menu
        print("5. Delete Item")
        print("6. Exit")
        choice=input('Enter Your Choice: ')
        if choice=='1':
            emp_name=input('Enter Employee Name: ')
            emp_phon=input('Enter Employee Phone Number: ')
            emp_email=input('Enter Employee Email: ')
            emp_addres=input('Enter Employee Address: ')
            emp_age=int(input('Enter Employee Age: '))
            emp_designation=input('Enter Employee Designation: ')
            emp_salary=int(input('Enter Employee Salary: '))
            employee=Employee(name=emp_name,phon=emp_phon,email=emp_email,addres=emp_addres,age=emp_age,designation=emp_designation,salary=emp_salary)
            admin.add_employee(mamar_restaurent,employee)

        elif choice=='2':
            admin.view_employee(mamar_restaurent)

        elif choice=='3':
            item_name=input('Enter Item Name: ')
            item_price=int(input('Enter Item Price: '))
            item_quantity=int(input('Enter Item Quantity: '))
            item=FoodItem(name=item_name,price=item_price,quntity=item_quantity)
            admin.add_item(mamar_restaurent,item)

        elif choice=='4':
            admin.view_menu(mamar_restaurent)

        elif choice=='5':
            item_name=input('Enter Item Name: ')
            admin.remove_item(mamar_restaurent,item_name)

        elif choice=='6':
            break

        else:
            print('Invalid Choice') 

while True:
    print(f"Welcome To Mamar Restaurent")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice=input('Enter Your Choice: ')
    if choice=='1':
        customer_menu()

    elif choice=='2':
        admin_menu()

    elif choice=='3':
        break

    else:
        print('Invalid Choice')