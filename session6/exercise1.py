# EX 1: Bank Exercise
#
# Create a Bank, an Account, and a Customer class.
# All classes should be in a single file.
# The bank class should be able to hold many account.
# You should be able to add new accounts.
# he Account class should have relevant details.
# The Customer class Should also have relevant details.
#
# Stick to the techniques we have covered so far.
# Add the ability for your __init__ method to handle
# different inputs (parameters).

class Bank:

    def __init__(self):
        self.accounts = list()

    def add_account(self, new_entry):
        self.accounts.append(new_entry)

    def print_accounts(self):
        for account in self.accounts:
            print("account number: ", account.id)


class Account:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)


class Customer:
    def __init__(self, name, age, sex, account):
        self.name = name
        self.age = age
        self.sex = sex
        self.account = account

    def __repr__(self):
        return str(self.__dict__)


def main():
    one = Account(1)
    two = Account(2)
    three = Account(3)

    cus1 = Customer("peter", 23, "helicopter", one)
    cus2 = Customer("Cris", 12, "m?", two)
    cus3 = Customer("NameHere", 99, "sex", three)

    print(cus1)     # this requires repr and str for it to work
    print("customer one: ", cus1.name, cus1.age, cus1.sex, cus1.account.id)
    print("customer two: ", cus2.name, cus2.age, cus2.sex, cus2.account.id)
    print("customer three: ", cus3.name, cus3.age, cus3.sex, cus3.account.id)

    bankOne = Bank()
    bankOne.add_account(one)
    bankOne.add_account(two)
    bankOne.add_account(three)

    bankOne.print_accounts()


main()
