class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = .02, balance = 0)

    def make_deposit(self, amount):
        self.account += amount
        return self

    def make_withdrawal(self, amount):
        self.account -= amount
        return self

    def display_user_balance(self):
        print(f"Name: {self.name}, {self.account}")
        return self

    def transfer_money(self, other_user, amount):
        self.account -= amount
        other_user.account += amount
        return self
        
class BankAccount:
    def __init__(self, int_rate = .02, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Interest Rate: {self.int_rate}, {self.balance}")
        return self
        
    def yield_interest(self):
        self.balance *= self.int_rate
        return self

first_user = User("Guido van Rossum", "guido@python.com" )
second_user = User("Monty Python", "monty@python.com")
third_user = User("Jacob Sexton", "jake@example.com")
# Create 3 instances of user class
print(first_user.name)
print(second_user.name)
print(third_user.name)
first_user.display_user_balance()
second_user.display_user_balance()
third_user.display_user_balance()
# First user makes 3 deposits and 1 withdrawal, then display account balance
first_user.make_deposit(100)
first_user.make_deposit(200)
first_user.make_deposit(300)
first_user.make_withdrawal(150)
first_user.display_user_balance()
# Second User makes 2 deposits and 2 withdrawals, then display balance
second_user.make_deposit(200)
second_user.make_deposit(400)
second_user.make_withdrawal(100)
second_user.make_withdrawal(150)
second_user.display_user_balance()
# Third user makes 1 deposit and 3 withdrawals, then display balance
third_user.make_deposit(10000000)
third_user.make_withdrawal(825)
third_user.make_withdrawal(50)
third_user.make_withdrawal(40000)
third_user.display_user_balance()
# Transfer first user's money to third user, the print both balances
first_user.transfer_money(third_user, 450)
first_user.display_user_balance()
third_user.display_user_balance()