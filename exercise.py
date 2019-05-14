class BankAccount:

    interest_rate = 0.03
    accounts = []

    def __init__(self):
        self.balance = 0

    def deposit(self, num):
        self.balance = self.balance + num

    def withdraw(self, num):
        self.balance = self.balance - num

    @classmethod
    def create(cls):
        new_account = BankAccount()
        cls.accounts.append(new_account) 
        return new_account

    @classmethod
    def total_funds(cls):
        total = 0
        for num in range(0, len(cls.accounts)):
            total += cls.accounts[num].balance
        return total

    @classmethod
    def interest_time(cls):
        
        for account in cls.accounts:
            account.balance = (account.balance * (1 + (cls.interest_rate)))
        
        

my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance) # 0
print(BankAccount.total_funds()) # 0
my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance) # 200
print(your_account.balance) # 1000
print(BankAccount.total_funds()) # 1200
BankAccount.interest_time()
print(my_account.balance) # 202.0
print(your_account.balance) # 1010.0
print(BankAccount.total_funds()) # 1212.0
my_account.withdraw(50)
print(my_account.balance) # 152.0
print(BankAccount.total_funds()) # 1162.0
