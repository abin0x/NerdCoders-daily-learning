class Person:
    def __init__(self, name, age):
        self._name = name  # ব্যক্তির নাম সংরক্ষণ করা হচ্ছে (private variable)
        self._age = age    # ব্যক্তির বয়স সংরক্ষণ করা হচ্ছে (private variable)

    @property
    def name(self):
        # নামের getter মেথড, যা প্রোপার্টি পড়ার জন্য ব্যবহার করা হয়
        return self._name

    @name.setter
    def name(self, value):
        # নামের setter মেথড, যা প্রোপার্টি সেট করার জন্য ব্যবহার করা হয়
        self._name = value

    @property
    def age(self):
        # বয়সের getter মেথড, যা প্রোপার্টি পড়ার জন্য ব্যবহার করা হয়
        return self._age

    @age.setter
    def age(self, value):
        # বয়সের setter মেথড, যা প্রোপার্টি সেট করার জন্য ব্যবহার করা হয়
        if value < 0:
            raise ValueError("বয়স ০ এর থেকে ছোট হতে পারে না")
        self._age = value

# Person অবজেক্ট তৈরি করা হচ্ছে
person = Person("Rahim", 25)

# getter ব্যবহার করে প্রোপার্টি পড়া হচ্ছে
print("Name:", person.name)  # আউটপুট: Name: Rahim
print("Age:", person.age)    # আউটপুট: Age: 25

# setter ব্যবহার করে প্রোপার্টি পরিবর্তন করা হচ্ছে
person.name = "Karim"
person.age = 30

print("Updated Name:", person.name)  # আউটপুট: Updated Name: Karim
print("Updated Age:", person.age)    # আউটপুট: Updated Age: 30

# ভুল মান দেওয়ার উদাহরণ, যা ValueError সৃষ্টি করবে
# person.age = -5
