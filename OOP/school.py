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
        self.students = []  # ✅ এখানে students লিস্ট যোগ করা হয়েছে

    def add_teachers(self, name, sub):
        id = len(self.teachers) + 101
        teacher = Teacher(name, sub, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'Not enough money for enrollment.'
        else:
            id = len(self.students) + 1  # ✅ এখন self.students লিস্ট ঠিকমতো কাজ করবে
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is now a student with ID: {id}. Extra money returned: {fee - 6500}'

    def __repr__(self):
        output = f'Welcome to {self.name}\n'
        output += '----------------- OUR TEACHERS ----------------\n'
        for teacher in self.teachers:
            output += str(teacher) + '\n'
        output += '----------------- OUR STUDENTS ----------------\n'
        for student in self.students:
            output += str(student) + '\n'
        return output


# স্কুল তৈরি
hstu = School("HSTU")

# শিক্ষার্থী ভর্তি করা
print(hstu.enroll('Apurbo', 5000))  # টাকা কম, ভর্তি হবে না
print(hstu.enroll('Parbez', 8000))  # ভর্তি হবে
print(hstu.enroll('Abin', 9000))    # ভর্তি হবে
print(hstu.enroll('Soumik', 6000))  # টাকা কম, ভর্তি হবে না

# শিক্ষক যোগ করা
hstu.add_teachers("Muaj", 'EEE')
hstu.add_teachers("Fahim", 'CSE')

# স্কুলের তথ্য প্রিন্ট করা
print(hstu)
