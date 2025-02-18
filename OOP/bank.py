class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100   # নূন্যতম উত্তোলনের পরিমাণ
        self.max_withdraw = 10000 # সর্বোচ্চ উত্তোলনের পরিমাণ

    def get_balance(self):
        return self.balance
    
    def deposite(self, amount):
        if amount > 0:
            self.balance += amount

    def moneyWithdraw(self, amount):
        # যদি উত্তোলনের পরিমাণ নূন্যতমের চেয়ে কম হয়, তাহলে বার্তা দেখাবে
        if amount < self.min_withdraw:
            print(f"Vai, tumi ki fokir naki? Minimum {self.min_withdraw} taka nite parba na.")
        # যদি উত্তোলনের পরিমাণ সর্বোচ্চের চেয়ে বেশি হয়, তাহলে বার্তা দেখাবে
        elif amount > self.max_withdraw:
            print(f"Vai, tumi ato besi taka nite dibo na. Maximum {self.max_withdraw} taka nite parba.")
        # যদি পরিমাণ সঠিক থাকে, তবে টাকা উত্তোলন করা হবে
        else:
            if amount > self.balance:
                print("Dukkho, apnar balance e parjapto taka nei.")
            else:
                self.balance -= amount 
                print(f"Here is your money: {amount}")

# উদাহরণ:
brac = Bank(20000)
brac.moneyWithdraw(12000000)  # এখানে উত্তোলনের পরিমাণ সর্বোচ্চ সীমার চেয়ে বেশি, তাই বার্তা দেখাবে
