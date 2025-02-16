# math মডিউল ব্যবহার
import math
print("π এর মান:", math.pi)
print("16 এর বর্গমূল:", math.sqrt(16))

# sys মডিউল ব্যবহার
import sys
print("পাইথনের ভার্সন:", sys.version)
print("কমান্ড লাইন আর্গুমেন্ট:", sys.argv)

# os মডিউল ব্যবহার
import os
print("বর্তমান কাজের ডিরেক্টরি:", os.getcwd())
print("সকল ফাইল ও ডিরেক্টরি:", os.listdir('.'))

# datetime মডিউল ব্যবহার
import datetime
now = datetime.datetime.now()
print("বর্তমান তারিখ ও সময়:", now)

# random মডিউল ব্যবহার
import random
print("একটি এলোমেলো সংখ্যা (1 থেকে 10):", random.randint(1, 10))
print("একটি এলোমেলো উপাদান:", random.choice(['apple', 'banana', 'cherry']))
