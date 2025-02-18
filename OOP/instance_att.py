class NewShop:
    shopingMallname = "Jamuna"  # এটি একটি ক্লাস অ্যাট্রিবিউট, যা সব ইনস্ট্যান্সের জন্য একই থাকবে।

    def __init__(self, buyer):
        self.buyer = buyer  # এটি ইনস্ট্যান্স অ্যাট্রিবিউট, যা প্রতিটি ইনস্ট্যান্সের জন্য আলাদা থাকবে।
        self.cart = []  # এটি ইনস্ট্যান্স অ্যাট্রিবিউট, যা প্রতিটি ইনস্ট্যান্সের জন্য আলাদা একটি খালি লিস্ট তৈরি করবে।

    def add_to_cart(self, item):
        self.cart.append(item)  # এই মেথডটি পণ্য যোগ করার জন্য ব্যবহৃত হয়।


# নতুন একটি শপিং মল ইনস্ট্যান্স তৈরি করা হলো
newMall = NewShop("helloBuyer")

# newMall ইনস্ট্যান্সে বিভিন্ন পণ্য যোগ করা হলো
newMall.add_to_cart("watch")
newMall.add_to_cart("shirt")
newMall.add_to_cart("pant")

# newMall ইনস্ট্যান্সের কার্টের ভেতরের আইটেম প্রিন্ট করা হলো
print(newMall.cart)  # আউটপুট: ['watch', 'shirt', 'pant']


# নতুন আরেকটি শপিং মল ইনস্ট্যান্স তৈরি করা হলো
againOne = NewShop("Newbuyer")

# againOne ইনস্ট্যান্সে বিভিন্ন পণ্য যোগ করা হলো
againOne.add_to_cart("mobile")
againOne.add_to_cart("camera")
againOne.add_to_cart("laptop")

# againOne ইনস্ট্যান্সের কার্টের ভেতরের আইটেম প্রিন্ট করা হলো
print(againOne.cart)  # আউটপুট: ['mobile', 'camera', 'laptop']
