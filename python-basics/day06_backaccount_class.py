class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def show_balance(self):
        print("Balance is", self.balance)

acc = BankAccount("Aditya", 1000)
acc.show_balance()
acc.deposit(500)
acc.show_balance()
acc.withdraw(300)
acc.show_balance()