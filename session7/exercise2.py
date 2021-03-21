# In the exercise from last monday with the bank, account and customer,
# change the code to use properties instead of the public variables.
#
# The bank class should futher be change into not taking any accounts
#   as parameters at initialization.
#
# The accouts should be added afterwards, either as a single account
#   one at a time, or as a collection of accounts (many at the sametime).
#
# Somewhere you should change the code so that a customer can only
#   create one account.
#
# The Customer class should make sure that the customer is over 18 year of age.


class Bank:
    def __init__(self):
        self.accounts = []

    @property  # accounts
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, account):
        self.__accounts = account

    def add_account(self, new_entry):
        self.accounts.append(new_entry)


class Account:
    account_number = 1
    customers_list = []

    def __init__(self, customer):
        self.number = Account.account_number
        self.customer = customer
        Account.account_number += 1

    def __repr__(self):
        return "\n" + str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)

    @property  # number
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property  # customer
    def customer(self):
        return self.customer

    @customer.setter
    def customer(self, customer):
        print("condition", Account.customers_list.count(customer))
        if Account.customers_list.count(customer) > 0:
            raise Exception("Customer already linked to one account.")
        Account.customers_list.append(customer)
        self.__customer = customer


class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return str(self.__dict__)

    @property  # name
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property  # age
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age >= 18:
            self.__age = age
        else:
            raise ValueError("User must be above the age of 18!")


peter = Customer("peter", 18)
anders = Customer("Anders", 21)
peter_account = Account(peter)
anders_account = Account(anders)
bank_of_antarctica = Bank()

bank_of_antarctica.add_account(peter_account)
bank_of_antarctica.add_account(anders_account)

print(bank_of_antarctica.__dict__)
