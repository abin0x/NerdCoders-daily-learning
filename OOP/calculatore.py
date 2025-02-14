class Calculator:
    brand="Casio"

    def add(self, a, b):
        return a+b
    
    def sub(self, a, b):
        return a-b
    
    def mul(self, a, b):
        return a*b
    
    def div(self, a, b):
        return a/b
    
    def __str__(self):
        return "This is a calculator class"
    
    def __repr__(self):
        return "Calculator()"
    
    def __len__(self):
        return 0
    
    def __del__(self):
        print("Calculator object deleted")

# এখন আমরা এই ক্লাস থেকে অবজেক্ট তৈরি করতে পারি
casio = Calculator()
print(casio.add(5, 10))  # আউটপুট: 15
print(casio.sub(10, 5))  # আউটপুট: 5
print(casio.mul(5, 10))  # আউটপুট: 50
print(casio.div(10, 5))  # আউটপুট: 2.0
print(casio)  # আউটপুট: This is a calculator class
print(len(casio))  # আউটপুট: 0
del casio  # Calculator object deleted
