"""This module is for testing solutions, prior to including them in the main sales_system.py
"""


import json


class Item:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Stock(object):

    def __init__(self, d):
        self.__dict__ = d


class User:

    def __init__(self, user_name, wallet):
        self.user_name = user_name
        self.wallet = wallet

    def check_balance(self, checkout_cost):
        return self.wallet >= checkout_cost

    def update_wallet(self, checkout_cost):
        self.wallet -= checkout_cost
        return self.wallet


class Transaction:

    def __init__(self, user):
        self.user = user

    def user_details(self):
        return self.user.user_name, self.user.wallet


cost = 2000
user_1 = User("Basil Fawlty", 1267.56)
if user_1.check_balance(cost):
    print(user_1.update_wallet(cost))
else:
    print(user_1.user_name, "doesn't have enough money.")

transaction_1 = Transaction(user_1)
print(transaction_1.user_details())

with open("stock.json", "r") as stock_file:
    stock_data = json.load(stock_file)

for item in stock_data:
    print(stock_data[item])