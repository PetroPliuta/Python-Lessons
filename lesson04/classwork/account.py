import random


class Account:
    __possible_currencies = ("UAH", "RUB", "USD")

    def __init__(self, amount=0, *, currency="UAH"):
        self.__account_number = random.randint(100000, 999999)
        if self.__check_float(amount):
            self.__amount = float(amount)
        else:
            self.__amount = 0.
        if currency in self.__possible_currencies:
            self.__currency = currency
        else:
            self.__currency = "UAH"

    def __str__(self):
        return "Account #"+str(self.__account_number)+". Amount: " + str(self.__amount) + ", currency: " + self.__currency

    def add_money(self, amount):
        if self.__check_float(amount):
            self.__amount += float(amount)

    def withdraw_money(self, amount):
        if self.__check_float(amount):
            self.__amount -= float(amount)

    def __check_float(self, amount):
        try:
            float(amount)
        except ValueError:
            return False
        else:
            return True

    def money_transfer(self, account_to, amount):
        if self.__check_float(amount) and isinstance(account_to, self.__class__):
            # print(type(account_to))
            self.withdraw_money(amount)
            account_to.add_money(amount)


account1 = Account(10, currency="~~")
print(account1)

account1.add_money("10")
print(account1)

account1.withdraw_money(2.6)
print(account1)

account2 = Account(1000000)
print(account2)
account2.money_transfer(account1, 100)
print(account1)
print(account2)
