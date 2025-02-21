from menu import Menu

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
