class Account:
    def __init__(self,id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if  money > 0:
            self.balance += money
            print(f"Deposit successful. Balance: {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print("Insufficient funds on the account.")
        elif money <= self.balance:
            self.balance -= money
            print(f"Withdraw of {money} successful. Balance: {self.balance}")

    def all_balance(self):
        print(f"Balance: {self.balance}")

man = Account("Man", 100)

man.all_balance()
man.withdraw(100)
man.deposit(100)
man.all_balance()