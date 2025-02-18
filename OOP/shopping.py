class Shopping:
    def __init__(self, name):
        self.name = name         # গ্রাহকের নাম সংরক্ষণ করে
        self.cart = []           # শপিং কার্ট হিসাবে একটি খালি তালিকা

    def add_to_cart(self, item, price, quantity):
        # পণ্যের তথ্যসহ একটি ডিকশনারি তৈরি করা হলো
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)  # তৈরি করা পণ্যটি কার্টে যুক্ত করা হলো

    def remove_item(self, item_name):
        """
        নির্দিষ্ট পণ্যের নামের ভিত্তিতে কার্ট থেকে পণ্যটি সরানো হবে।
        যদি পণ্যটি পাওয়া যায়, তাহলে এটি সরিয়ে বার্তা প্রদর্শন করবে।
        যদি না পাওয়া যায়, তাহলে উপযুক্ত বার্তা প্রদর্শন করবে।
        """
        for product in self.cart:
            if product['item'] == item_name:
                self.cart.remove(product)
                print(f"{item_name} সরানো হয়েছে কার্ট থেকে।")
                return
        print(f"{item_name} কার্টে পাওয়া যায়নি।")

    def checkout(self, amount):
        total = 0
        # কার্টে থাকা প্রতিটি পণ্যের মোট মূল্য হিসাব করা হলো
        for product in self.cart:
            total += product['price'] * product['quantity']
        print("Total Price is:", total)
        
        # গ্রাহক প্রদত্ত টাকার পরিমাণের সাথে মোট মূল্য তুলনা করা হলো
        if amount < total:
            print(f"আপনি আরও {total - amount} টাকা প্রদান করুন।")
        else:
            print(f"আপনার অতিরিক্ত টাকা হলো {amount - total}")

# উদাহরণ:
she = Shopping("Girl")
she.add_to_cart("sharee", 500, 3)    # sharee যোগ করা হলো
she.add_to_cart("makeup", 100, 2)      # makeup যোগ করা হলো
she.add_to_cart("lipstic", 200, 1)     # lipstic যোগ করা হলো

print("কার্টের আইটেম:", she.cart)
she.checkout(1000)

# কার্ট থেকে lipstic পণ্যটি সরানো
she.remove_item("lipstic")
print("আপডেটেড কার্ট:", she.cart)
