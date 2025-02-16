# ডিকশনারি ডিক্লেয়ার করা
myDict = {
    "name": "Phitron",
    "age": 25,
    "city": "Dhaka"
}

# 1. keys() - সকল কী দেখুন
print("Keys:", myDict.keys())  
# Output: dict_keys(['name', 'age', 'city'])

# 2. values() - সকল মান দেখুন
print("Values:", myDict.values())  
# Output: dict_values(['Phitron', 25, 'Dhaka'])

# 3. items() - কী-ভ্যালু জোড়া দেখুন
print("Items:", myDict.items())  
# Output: dict_items([('name', 'Phitron'), ('age', 25), ('city', 'Dhaka')])

# 4. get() - নির্দিষ্ট কী-এর মান পান
print("Age:", myDict.get("age"))  
# Output: 25

# 5. pop() - নির্দিষ্ট কী-ভ্যালু সরিয়ে মান পান
popped_age = myDict.pop("age")
print("Popped Age:", popped_age)  
# Output: 25
print("After pop:", myDict)  
# Output: {'name': 'Phitron', 'city': 'Dhaka'}

# 6. popitem() - শেষের কী-ভ্যালু জোড়া সরিয়ে নেয়
popped_item = myDict.popitem()
print("Popped Item:", popped_item)  
# উদাহরণস্বরূপ আউটপুট: ('city', 'Dhaka')
print("After popitem:", myDict)  
# Output: {'name': 'Phitron'}

# 7. update() - নতুন কী-ভ্যালু যোগ করে বা আপডেট করে
myDict.update({"country": "Bangladesh", "name": "Phitron Institute"})
print("After update:", myDict)  
# Output: {'name': 'Phitron Institute', 'country': 'Bangladesh'}

# 8. copy() - শ্যালো কপি তৈরি করা
dict_copy = myDict.copy()
print("Dictionary Copy:", dict_copy)  
# Output: {'name': 'Phitron Institute', 'country': 'Bangladesh'}

# 9. clear() - সকল কী-ভ্যালু সরিয়ে ফেলা
myDict.clear()
print("After clear:", myDict)  
# Output: {}

# 10. fromkeys() - নতুন ডিকশনারি তৈরি করা
keys = ["a", "b", "c"]
newDict = dict.fromkeys(keys, 0)
print("New Dictionary from keys:", newDict)  
# Output: {'a': 0, 'b': 0, 'c': 0}
