class Person:
    def __init__(self,name,age,hight,weight):
        self.name = name
        self.age = age
        self.hight = hight
        self.weight = weight
    def eat(self):
        print(f"Vat pulao kurma")

    def exercise(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Circketer(Person):
    def __init__(self,name,age,hight,weight,runs,wickets):
        self.runs = runs
        self.wickets = wickets
        super().__init__(name,age,hight,weight)

    def eat(self):
        print(f"Name: {self.name}\nAge: {self.age}\nHight: {self.hight}\nWeight: {self.weight}\nRuns: {self.runs}\nWickets: {self.wickets}")
    def exercise(self):
        print(f"{self.name} is doing excercise")

sakib=Circketer("Sakib",35,5.6,75,5000,200)
sakib.eat()
sakib.exercise()
# Output:
# Name: Sakib
# Age: 35
# Hight: 5.6
# Weight: 75
# Runs: 5000