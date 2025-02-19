class Bank:
    def __init__(self,holder_name,initial_deposite):
        self.holder_name=holder_name #Public variable
        self._branch='Banani' #Protected variable
        self.__balance=initial_deposite #Private variable

    def deposit(self,amount): 
        self.__balance+=amount

    def get_balance(self):
        return self.__balance

refasn=Bank("Abin",10000)
print(refasn.holder_name)
print(refasn.get_balance())