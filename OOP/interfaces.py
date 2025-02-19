from abc import ABC, abstractmethod

# 🔹 Interface হিসাবে কাজ করবে
class Animal(ABC):  
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

# 🔹 এই ক্লাসকে বাধ্যতামূলকভাবে eat() এবং move() ইমপ্লিমেন্ট করতে হবে
class Dog(Animal):
    def eat(self):
        print("Dog is eating...")
    
    def move(self):
        print("Dog is running...")

class Fish(Animal):
    def eat(self):
        print("Fish is eating...")
    
    def move(self):
        print("Fish is swimming...")

# ✅ এখন Dog এবং Fish ক্লাসকে অবশ্যই eat() ও move() ইমপ্লিমেন্ট করতে হবে
dog = Dog()
dog.eat()   # Output: Dog is eating...
dog.move()  # Output: Dog is running...

fish = Fish()
fish.eat()   # Output: Fish is eating...
fish.move()  # Output: Fish is swimming...
