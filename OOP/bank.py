class Bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=10000

    def get_balance(self):
        return self.balance
    
    def deposite(self,amount):
        if amount>0:
            self.balance +=amount
    
    def moneyWithdraw(self,amount):
        if amount<self.min_withdraw:
             print (f" vai tumi ki fokir naki? minimum{self.min_withdraw} taka nite parba")
        elif amount>self.max_withdraw:
            print (f"Vai tumi ato besi taka nite dibo na {self.max_withdraw} ato takar besi nite parba na")
        
        else:
            self.balance-=amount 
            print (f"here is your money {amount}")
            print(f"here you last money{self.get_balance()}")

brac=Bank(20000)
brac.moneyWithdraw(1200)
# print()