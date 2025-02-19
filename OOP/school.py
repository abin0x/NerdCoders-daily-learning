class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self):
        return f"Student name: {self.name}, Studying in Class {self.current_class}, ID: {self.id}"

class Teacher:
    def __init__(self, name, sub, id):
        self.name = name
        self.sub = sub
        self.id = id

    def __repr__(self):
        return f"Teacher name: {self.name}, Subject: {self.sub}, ID: {self.id}"

class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
    
    def add_teachers(self, name, sub):
        id = len(self.teachers) + 101
        teacher = Teacher(name, sub, id)
        self.teachers.append(teacher)
    
    def enroll(self, name, fee):
        if fee < 6500:
            return f"Not enough money for enrollment for {name}."
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f"{name} is now a student with ID: {id}. Extra money returned: {fee - 6500}"
    
    def display(self):
        print("Welcome to", self.name)
        print("----------------- OUR TEACHERS ----------------")
        for teacher in self.teachers:
            print(teacher)
        print("----------------- OUR STUDENTS ----------------")
        for student in self.students:
            print(student)

# Create a School object
hstu = School("HSTU")

# Enroll students
print(hstu.enroll('apurbo', 5000))  # Insufficient fee, so not enrolled.
print(hstu.enroll('parbez', 8000))  # Enrolled.
print(hstu.enroll('abin', 9000))    # Enrolled.
print(hstu.enroll('soumik', 6000))  # Insufficient fee, so not enrolled.

# Add teachers
hstu.add_teachers("Muaj", 'EEE')
hstu.add_teachers("Fahim", 'CSE')

# Display school details using the custom display() method
hstu.display()
