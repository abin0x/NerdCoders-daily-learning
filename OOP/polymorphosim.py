class Animal:
    def __init__(self,name):
        self.name=name

    def make_sound(self):
        print("Animal is making sound ...")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Dog is barking ...")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print("Cat is meowing ...")


don=Dog("Don")
don.make_sound()
print(don.name)
me=Cat("Biral")
me.make_sound()
print(me.name)