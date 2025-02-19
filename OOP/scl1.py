# 🔹 Student ক্লাসটি তৈরি করা হয়েছে
class Student:
    def __init__(self, name, current_class, id):
        # 🔹 শিক্ষার্থীর নাম, ক্লাস, এবং আইডি সেট করা হচ্ছে
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self):
        # 🔹 শিক্ষার্থীর তথ্য সুন্দরভাবে প্রিন্ট করার জন্য __repr__() মেথড ব্যবহার করা হয়েছে
        return f"Student name: {self.name}, Studying in Class {self.current_class}, ID: {self.id}"


# 🔹 Teacher ক্লাসটি তৈরি করা হয়েছে
class Teacher:
    def __init__(self, name, sub, id):
        # 🔹 শিক্ষকের নাম, বিষয়, এবং আইডি সেট করা হচ্ছে
        self.name = name
        self.sub = sub
        self.id = id

    def __repr__(self):
        # 🔹 শিক্ষকের তথ্য সুন্দরভাবে প্রিন্ট করার জন্য __repr__() মেথড ব্যবহার করা হয়েছে
        return f"Teacher name: {self.name}, Subject: {self.sub}, ID: {self.id}"


# 🔹 School ক্লাস তৈরি করা হয়েছে, যেখানে শিক্ষক ও শিক্ষার্থী সংরক্ষণ করা হবে
class School:
    def __init__(self, name):
        self.name = name  # 🔹 স্কুলের নাম সংরক্ষণ করা হচ্ছে
        self.teachers = []  # 🔹 শিক্ষকদের তালিকা রাখার জন্য একটি খালি লিস্ট
        self.students = []  # 🔹 শিক্ষার্থীদের তালিকা রাখার জন্য একটি খালি লিস্ট

    # 🔹 নতুন শিক্ষক যোগ করার ফাংশন
    def add_teachers(self, name, sub):
        id = len(self.teachers) + 101  # 🔹 স্বয়ংক্রিয়ভাবে শিক্ষকের আইডি নির্ধারণ করা হচ্ছে
        teacher = Teacher(name, sub, id)  # 🔹 নতুন Teacher অবজেক্ট তৈরি
        self.teachers.append(teacher)  # 🔹 শিক্ষককে তালিকায় যোগ করা হচ্ছে

    # 🔹 শিক্ষার্থী ভর্তি করার ফাংশন
    def enroll(self, name, fee):
        if fee < 6500:
            print(f"Not enough money for enrollment for {name}.")
        else:
            id = len(self.students) + 1  # 🔹 স্বয়ংক্রিয়ভাবে শিক্ষার্থীর আইডি নির্ধারণ করা হচ্ছে
            student = Student(name, 'C', id)  # 🔹 নতুন Student অবজেক্ট তৈরি
            self.students.append(student)  # 🔹 শিক্ষার্থীকে তালিকায় যোগ করা হচ্ছে
            print(f"{name} is now a student with ID: {id}. Extra money returned: {fee - 6500}")

    # 🔹 স্কুলের সব তথ্য প্রিন্ট করার জন্য display() মেথড ব্যবহার করা হচ্ছে
    def display(self):
        print("Welcome to", self.name)
        print("----------------- OUR TEACHERS ----------------")
        for teacher in self.teachers:
            print(teacher)
        print("----------------- OUR STUDENTS ----------------")
        for student in self.students:
            print(student)


# 🔹 স্কুল তৈরি করা হচ্ছে
hstu = School("HSTU")

# 🔹 শিক্ষার্থীদের ইনপুট নেওয়া হচ্ছে
num_students = int(input("Enter the number of students to add: "))
for i in range(num_students):
    name = input(f"Enter student name {i+1}: ")
    fee = int(input(f"Enter the money for student {i+1}: "))
    hstu.enroll(name, fee)

# 🔹 শিক্ষক যোগ করার জন্য ইনপুট নেওয়া হচ্ছে
num_teachers = int(input("Enter number of teachers to add: "))
for i in range(num_teachers):
    teacher_name = input(f"Enter name for teacher {i+1}: ")
    teacher_subject = input(f"Enter subject for teacher {i+1}: ")
    hstu.add_teachers(teacher_name, teacher_subject)

# 🔹 স্কুলের তথ্য প্রিন্ট করা হচ্ছে
print()  # For a line break
hstu.display()
