class Account:
    def __init__(self, balance, type):
        self.balance = balance
        self.type = type

    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            raise ValueError(f"Can't withdraw {amount} from the account with balance{self.balance}")
        self.balance -= amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("You can't deposit negative amount")
        self.balance += amount

    def savings(self, interest):
        if self.type == "savings":
            self.balance *= (1 + interest)


my_account = Account(1000, "savings")
my_account.savings(50)
print(my_account.balance)

my_other_account = Account(1000, "savings")

try:
    my_other_account.withdraw(1250)
except ValueError:
    print("That doesn't work...")
try:
    my_other_account.deposit(-100)
except:
    print("That doesn't work either...")

