class Family:
    def __init__(self,address):
        self.address=address


class School:
    def __init__(self,id,level):
        self.id=id
        self.level=level

class Sports:
    def __init__(self,game):
        self.game=game

class Student(Family,School,Sports):
    def __init__(self,name,age,address,id,level,game):
        self.name=name
        self.age=age
        Family.__init__(self,address)
        School.__init__(self,id,level)
        Sports.__init__(self,game)

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}\nID: {self.id}\nClass: {self.level}\nGame: {self.game}")

# অবজেক্ট তৈরি
student1 = Student("John Doe", 12, "Dhaka", 101, 7, "Cricket")
student1.display()
