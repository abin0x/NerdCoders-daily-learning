# সুপার ক্লাস
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

# সাব ক্লাস
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Animal-এর __init__ কল করা হলো
        self.breed = breed

    # মেথড ওভাররাইড করা হচ্ছে
    def speak(self):
        print(f"{self.name} says: Woof!")

# অবজেক্ট তৈরি করা
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.speak()  # আউটপুট: Buddy says: Woof!
