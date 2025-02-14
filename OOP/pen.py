class Pen:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    def write(self):
        return f"{self.brand} pen writes in {self.color} ink."

# Creating three different instances
pen1 = Pen("Parker", "Blue", 15.99)
pen2 = Pen("Reynolds", "Black", 2.99)
pen3 = Pen("Lamy", "Red", 20.50)

# Printing details
print(pen1.write())  # Output: Parker pen writes in Blue ink.
print(pen2.write())  # Output: Reynolds pen writes in Black ink.
print(pen3.write())  # Output: Lamy pen writes in Red ink.
