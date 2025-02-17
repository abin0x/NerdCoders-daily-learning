# methods.py থেকে একটি সাধারণ ফাংশন ডিফাইন করা হচ্ছে
def call():
    print("Called from methods.py")
    return "Calledsss from methods.py"

# Phone নামের একটি ক্লাস তৈরি করা হচ্ছে
class Phone:
    # ক্লাসের ডিফল্ট অ্যাট্রিবিউটগুলো
    price = 1000        # ফোনের দাম
    colour = "black"    # ফোনের রঙ
    brand = "apple"     # ফোনের ব্র্যান্ড
    model = "iPhone 11" # ফোনের মডেল
    features = ['abin', 'mahedi', 'obaidur']

    # __repr__ মেথড: অবজেক্টের স্ট্রিং রিপ্রেজেন্টেশন প্রদান করে
    def __repr__(self):
        return f"Phone price is {self.price} and colour is {self.colour} and brand is {self.brand} and model is {self.model} and also features {self.features}"

    # Phone ক্লাসের call মেথড, যা একটি instance method
    def call(self):
        print("Hello abin, Called from methods.py")

    # send_msg মেথড, যা একটি নির্দিষ্ট নম্বরে মেসেজ পাঠানোর কাজ করবে
    def send_msg(self, number, text):
        print(f"This {number} number send me {text} this text")

# Phone ক্লাস থেকে একটি অবজেক্ট তৈরি করা হচ্ছে
my_phone = Phone()

# __repr__ মেথডের মাধ্যমে ফোন অবজেক্টের তথ্য প্রিন্ট করা হচ্ছে
print(my_phone)

# সাধারণ call() ফাংশন কল করা হচ্ছে (যা methods.py-তে ডিফাইন করা হয়েছে)
call()

# Phone অবজেক্টের call() মেথড কল করা হচ্ছে
my_phone.call()

# send_msg মেথড কল করা হচ্ছে
my_phone.send_msg("01780946249", "Hello abin")
