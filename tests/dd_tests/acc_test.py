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

    def interest(self, interest):
        if self.type == "savings":
            self.balance *= (1 + interest)


my_other_account = Account(1000, "savings")

try:
    my_other_account.withdraw(1250)
except ValueError:
    print("That doesn't work...")
try:
    my_other_account.deposit(-100)
except:
    print("That doesn't work either...")

my_account = Account(1000, "savings")
my_account.withdraw(500)
my_account.deposit(750)
my_account.interest(0.05)
print(my_account.balance)

my_other_account = Account(1000, "checking")
my_other_account.withdraw(500)
my_other_account.deposit(750)
my_other_account.interest(0.05)
print(my_other_account.balance)
