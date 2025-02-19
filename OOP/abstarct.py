from abc import ABC,abstractmethod


class Animal(ABC):
    @abstractmethod
    def eat(self):
        print("Eating food ...")
    # @abstractmethod
    def move(self):
        print("Moving ...")

class Monkey(Animal):
    def __init__(self,name):
        self.name=name
        self.category="Mammal"
        super().__init__()
    def eat(self):
        print("Monkey is eating hahaha...")
    def move(self):
        print("Monkey is jumping ...")



lyka=Monkey("Lyka")
lyka.eat()
print(lyka.name)
lyka.move()
print(lyka.category)
# Animal.move(lyka)