# 1. add(): সেটে একটি উপাদান যোগ করে।
s = {1, 2, 3}
s.add(4)
print("After add(4):", s)  # আউটপুট: {1, 2, 3, 4}

# 2. clear(): সেটের সকল উপাদান মুছে ফেলে।
s_clear = {1, 2, 3}
s_clear.clear()
print("After clear():", s_clear)  # আউটপুট: set()

# 3. copy(): সেটের একটি শ্যালো কপি ফেরত দেয়।
s_copy = {1, 2, 3}
s_copy2 = s_copy.copy()
print("Copy of set:", s_copy2)  # আউটপুট: {1, 2, 3}

# 4. difference(): দুটি সেটের পার্থক্য (difference) ফেরত দেয়।
set1 = {1, 2, 3}
set2 = {2, 3, 4}
diff = set1.difference(set2)
print("Difference (set1 - set2):", diff)  # আউটপুট: {1}

# 5. difference_update(): বর্তমান সেটকে আপডেট করে পার্থক্য দিয়ে।
set3 = {1, 2, 3}
set3.difference_update(set2)
print("After difference_update(set2) on set3:", set3)  # আউটপুট: {1}

# 6. discard(): উপাদানটি সেট থেকে মুছে ফেলে, যদি না থাকে তবুও কোনো ত্রুটি দেয় না।
s_discard = {1, 2, 3}
s_discard.discard(2)
s_discard.discard(5)  # 5 নেই, তবে ত্রুটি হবে না
print("After discard(2) and discard(5):", s_discard)  # আউটপুট: {1, 3}

# 7. frozenset(): একটি অপরিবর্তনীয় (immutable) frozenset অবজেক্ট ফেরত দেয়।
s_frozen = {1, 2, 3}
frozen = frozenset(s_frozen)
print("Frozen set:", frozen)  # আউটপুট: frozenset({1, 2, 3})

# 8. intersection(): দুই বা একাধিক সেটের মিল (intersection) ফেরত দেয়।
set4 = {1, 2, 3}
set5 = {2, 3, 4}
intersect = set4.intersection(set5)
print("Intersection (set4 ∩ set5):", intersect)  # আউটপুট: {2, 3}

# 9. intersection_update(): বর্তমান সেটকে মিলের সাথে আপডেট করে।
set6 = {1, 2, 3}
set6.intersection_update(set5)
print("After intersection_update(set5) on set6:", set6)  # আউটপুট: {2, 3}

# 10. isdisjoint(): চেক করে যে দুটি সেটে কোনো মিল নেই।
set7 = {1, 2, 3}
set8 = {4, 5, 6}
print("set7 and set8 are disjoint:", set7.isdisjoint(set8))  # আউটপুট: True

# 11. issubset(): চেক করে যে একটি সেটের সকল উপাদান অন্য সেটে আছে কিনা।
set9 = {1, 2}
set10 = {1, 2, 3}
print("set9 is subset of set10:", set9.issubset(set10))  # আউটপুট: True

# 12. issuperset(): চেক করে যে একটি সেট অন্য সেটের সকল উপাদান ধারণ করে কিনা।
print("set10 is superset of set9:", set10.issuperset(set9))  # আউটপুট: True

# 13. pop(): এলোমেলো একটি উপাদান মুছে ফেলে এবং ফেরত দেয়।
s_pop = {1, 2, 3}
popped_elem = s_pop.pop()
print("Popped element:", popped_elem, "Remaining set:", s_pop)

# 14. remove(): একটি নির্দিষ্ট উপাদান সেট থেকে মুছে ফেলে। (উপাদান না থাকলে KeyError দেয়)
s_remove = {1, 2, 3}
s_remove.remove(2)
print("After remove(2):", s_remove)  # আউটপুট: {1, 3}

# 15. symmetric_difference(): দুটি সেটের সিমেট্রিক ডিফারেন্স ফেরত দেয়।
set11 = {1, 2, 3}
set12 = {3, 4, 5}
sym_diff = set11.symmetric_difference(set12)
print("Symmetric difference (set11 ^ set12):", sym_diff)  # আউটপুট: {1, 2, 4, 5}

# 16. symmetric_difference_update(): বর্তমান সেটকে সিমেট্রিক ডিফারেন্স দিয়ে আপডেট করে।
set13 = {1, 2, 3}
set13.symmetric_difference_update(set12)
print("After symmetric_difference_update(set12) on set13:", set13)  # আউটপুট: {1, 2, 4, 5}

# 17. union(): দুই বা একাধিক সেটের ইউনিয়ন (union) ফেরত দেয়।
set14 = {1, 2}
set15 = {2, 3}
union_set = set14.union(set15)
print("Union of set14 and set15:", union_set)  # আউটপুট: {1, 2, 3}

# 18. update(): একটি বা একাধিক উপাদান সেটে যোগ করে।
s_update = {1, 2}
s_update.update([3, 4])
print("After update([3, 4]):", s_update)  # আউটপুট: {1, 2, 3, 4}
