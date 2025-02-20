class Person:
    population = 0  # ক্লাস ভেরিয়েবল যা জনসংখ্যা সংরক্ষণ করে

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1  # প্রতিবার নতুন অবজেক্ট তৈরি হলে জনসংখ্যা বাড়ে

    @classmethod
    def get_population(self):
        # এই ক্লাস মেথডটি cls এর মাধ্যমে ক্লাসের সকল ভেরিয়েবল অ্যাক্সেস করতে পারে
        print(f"Present People: {self.population}")
        

# কিছু Person অবজেক্ট তৈরি করা হলো
p1 = Person("রহিম",25)
p2 = Person("করিম", 30)
# print(Person.get_population())
Person.get_population()

# ক্লাস মেথড কল করা হলো
# print("Present People:", Person.get_population()) 
