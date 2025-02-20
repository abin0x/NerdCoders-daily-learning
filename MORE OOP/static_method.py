class MathOperations:
    @staticmethod
    def add(a, b):
        # দুইটি সংখ্যার যোগফল প্রদান করে
        print(a + b)

    @staticmethod
    def multiply(a, b):
        # দুইটি সংখ্যার গুণফল প্রদান করে
        print(a * b)

# স্ট্যাটিক মেথড কল করা হলো, অবজেক্ট তৈরি করার প্রয়োজন নেই
MathOperations.add(10, 20)
MathOperations.multiply(5, 4)

