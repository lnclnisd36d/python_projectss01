# defines the user class
class User:
    def __init__(self, user_id, name, phone):
        self.user_id = user_id  # initialize user id
        self.name = name  # initialize username
        self.phone = phone  # initialize user phone number
        self.account = Account(self)  # creating account for the user

    def __repr__(self):
        return f"User  ({self.user_id}, {self.name}, {self.phone})"  # Representation of the user object


# define account class
class Account:
    def __init__(self, user):
        self.user = user
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:  # check if the deposit is more than 0
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:  # check if the withdrawal amount is valid
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount")

    def __repr__(self):
        return f"Account(User: {self.user.name}, Balance: {self.balance})"  # Representation of Account object


# defines the transaction class
class Transaction:
    def __init__(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type

    def process(self):
        if self.transaction_type == 'deposit':
            self.account.deposit(self.amount)
        elif self.transaction_type == 'withdraw':
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type")

    def __repr__(self):
        return f"Transaction(Account: {self.account.user.name}, Amount: {self.amount}, Type: {self.transaction_type})"  # Representation of Transaction object

# Create user instances
user1 = User(1, "Joseph Ahadi", "701954706")
user2 = User(2, "Alice", "123-456-7890")
user3 = User(3, "Bob", "234-567-8901")
user4 = User(4, "Charlie", "345-678-9012")

print(user1)
print(user2)
print(user3)
print(user4)

# Example transactions
user1.account.deposit(10000)
user1.account.withdraw(15000)

transaction1 = Transaction(user1.account, 12000, 'deposit')
transaction1.process()

transaction2 = Transaction(user1.account, 10000, 'withdraw')
transaction2.process()

user2.account.deposit(10000)
user2.account.withdraw(15000)

transaction3 = Transaction(user2.account, 12000, 'deposit')
transaction3.process()

transaction4 = Transaction(user2.account, 10000, 'withdraw')
transaction4.process()

user3.account.deposit(10000)
user3.account.withdraw(15000)

transaction5 = Transaction(user3.account, 12000, 'deposit')
transaction5.process()

transaction6 = Transaction(user3.account, 10000, 'withdraw')
transaction6.process()

user4.account.deposit(10000)
user4.account.withdraw(15000)

transaction7 = Transaction(user4.account, 12000, 'deposit')
transaction7.process()

transaction8 = Transaction(user4.account, 10000, 'withdraw')
transaction8.process()

print(user1.account)
print(user2.account)
print(user3.account)
print(user4.account)