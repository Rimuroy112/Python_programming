class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_number = acc

    def debit(self,amount):
        self.balance -= amount
        print(amount,"amount debited !")
        print("Total Balance: ",self.get_balance())
    def credit(self,amount):
        self.balance += amount
        print(amount,"amount credited")
        print("Total Balance: ",self.get_balance())
    def get_balance(self):
        return self.balance

acc1 = Account(50000,12345)
acc1.debit(5000)
acc1.credit(20000)
