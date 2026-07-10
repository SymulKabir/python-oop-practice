class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
        
    def deposit(self, balance):
        if balance > 0:
            self.__balance += balance
    def withdraw(self, balance):
        if balance > 0 and balance <= self.__balance:
            self.__balance -= balance
    def get_balance(self):
        print(f"Dear {self.account_holder}, your current balance is {self.__balance} tk")
        

my_acc= BankAccount("Kamal", 100)

my_acc.get_balance()
my_acc.deposit(120)
my_acc.get_balance()
my_acc.withdraw(200)
my_acc.get_balance()
