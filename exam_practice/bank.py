
# Create a Bank, an Account, and a Customer class.
#  All classes should be in a single file.
#  Bank class should be able to hold many account.
#   You should be able to add new accounts.
# Account class should have relevant details.
# Customer class Should also have relevant details.

# Stick to the techniques we have covered so far.

class Account():
    number = 1

    def __init__(self, balance=0):
        self.id = self.number
        self.balance = balance
        Account.number += 1

    def __repr__(self):
        return self.__dict__

    def __str__(self):
        return f"< id: {self.id}, balance: {self.balance} >"

    def __eq__(self, other):
        return (self.balance, self.id) == (other.balance, other.id)


class Customer():
    def __init__(self, name, *balance):
        self.name = name
        if balance:
            for number in balance:
                self.account = Account(number)
        else:
            self.account = Account()

    def __repr__(self):
        return f"< name: {self.name}, account: {self.account} >"

    def __str__(self):
        return f"< name: {self.name}, account: {self.account} >"

    def __eq__(self, other):
        return (self.name, self.account) == (other.name, other.account)


class Bank():
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.accounts = []

    def add_customer(self, *clients):
        for client in clients:
            self.customers.append(client)

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return f"< bank name: {self.name}, customers: {self.customers} >"


# Bank
bank = Bank("Nordea")

# Customers
peter = Customer("Peter")
luis = Customer("Luis", 520)
anders = Customer("Anders", 1000)

bank.add_customer(peter, luis, anders)

print(bank)
print(peter == luis)
print(peter.account == luis.account)
