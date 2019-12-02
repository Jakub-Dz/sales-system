"""This module is for testing solutions, prior to including them in the main sales_system.py
"""


import json


class Item:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Stock:

    def __init__(self):
        with open("stock.json", "r") as stock_file:
            self.stock_dict = json.load(stock_file)

    def display(self, item_name="all"):
        if item_name == "all":
            for item in self.stock_dict:
                print(item, self.stock_dict[item]["price"], self.stock_dict[item]["quantity"])
        else:
            print(item_name, self.stock_dict[item_name]["price"], self.stock_dict[item_name]["quantity"])

    def remove(self, item_name, quantity):
        self.stock_dict[item_name]["quantity"] -= quantity

    def save(self):
        with open("stock.json", "w") as stock_file:
            json.dump(self.stock_dict, stock_file, indent=3)


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

    def stock(self):
        with open("stock.json", "r") as stock_file:
            self.stock_data = json.load(stock_file)


cost = 2000
user_1 = User("Basil Fawlty", 1267.56)
if user_1.check_balance(cost):
    print(user_1.update_wallet(cost))
else:
    print(user_1.user_name, "doesn't have enough money.")

transaction_1 = Transaction(user_1)
print(transaction_1.user_details())

stock = Stock()
stock.display()
stock.remove("Bookcase", 0)
stock.display("Bookcase")
stock.save()
