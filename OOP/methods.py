# methods.py থেকে একটি সাধারণ ফাংশন ডিফাইন করা হচ্ছে
def call():
    # ফাংশনটি কল হলে "Called from methods.py" প্রিন্ট হবে
    print("Called from methods.py")
    # ফাংশনটি "Calledsss from methods.py" স্ট্রিং রিটার্ন করে
    return "Calledsss from methods.py"

# Phone নামের একটি ক্লাস তৈরি করা হচ্ছে
class Phone:
    # ক্লাসের ডিফল্ট অ্যাট্রিবিউটগুলো
    price = 1000        # ফোনের দাম
    colour = "black"    # ফোনের রঙ
    brand = "apple"     # ফোনের ব্র্যান্ড
    model = "iPhone 11" # ফোনের মডেল

    # __repr__ মেথড: অবজেক্টের স্ট্রিং রিপ্রেজেন্টেশন প্রদান করে
    def __repr__(self):
        return f"Phone price is {self.price} and colour is {self.colour} and brand is {self.brand} and model is {self.model}"

    # Phone ক্লাসের call মেথড, যা একটি instance method
    def call(self):
        # মেথডটি কল হলে এই বার্তা প্রিন্ট হবে
        print("Hello abin,Called from methods.py")
        # আপনি চাইলে এখানে একটি রিটার্ন স্টেটমেন্টও যোগ করতে পারেন
        # return "Called from methods.py"

# Phone ক্লাস থেকে একটি অবজেক্ট তৈরি করা হচ্ছে
my_phone = Phone()

# __repr__ মেথডের মাধ্যমে ফোন অবজেক্টের তথ্য প্রিন্ট করা হচ্ছে
print(my_phone)

# সাধারণ call() ফাংশন কল করা হচ্ছে (যা methods.py-তে ডিফাইন করা হয়েছে)
call()

# Phone অবজেক্টের call() মেথড কল করা হচ্ছে
my_phone.call()
