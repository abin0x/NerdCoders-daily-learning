class Shape:
    def __init__(self, name):
        self.name = name

class Circle(Shape):
    def __init__(self, name):
        super().__init__(name)
    
    def area(self, radius):
        return 3.14 * radius * radius
class Ractangle(Shape):
    def __init__(self, name, length, width):
        self.length = length
        self.width = width
        super().__init__(name)
    
    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, name, base, height):
        self.base = base
        self.height = height
        super().__init__(name)
    
    def area(self):
        return 0.5 * self.base * self.height

circle = Circle("Circle")
print(circle.area(5))
ractangle = Ractangle("Ractangle", 5, 10)
print(ractangle.area())
triangle = Triangle("Triangle", 5, 10)

print(triangle.area())

