class Shape:
    def __init__(self, name):
        self.name = name

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# বিভিন্ন শেপের অবজেক্ট তৈরি করা হচ্ছে
circle = Circle("Circle", 5)
print(f"Area of {circle.name}: {circle.area()}")

rectangle = Rectangle("Rectangle", 5, 10)
print(f"Area of {rectangle.name}: {rectangle.area()}")

triangle = Triangle("Triangle", 5, 10)
print(f"Area of {triangle.name}: {triangle.area()}")
