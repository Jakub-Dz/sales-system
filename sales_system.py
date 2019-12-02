"""Sales System Project
This sales system is for customer use, not company use.
The company only has one customer.
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


class Basket(Stock):  # Not sure if calling Stock is a good idea, as Stock methods will be callable in Basket

    def __init__(self, value=0):
        super().__init__()
        self.value = value
        self.items = {}

    def add_item(self, item_name, quantity):
        self.items[item_name] = quantity
        self.value += quantity * self.stock_dict[item_name]["price"]

    def remove_item(self, item_name):
        del self.items[item_name]


class Transaction:

    def __init__(self, user):
        self.user = user

    def user_details(self):
        return self.user.user_name, self.user.wallet
    # if self.stock_dict[item_name]["quantity"] - quantity >= 0:


stock = Stock() # Must run
stock.display()
basket = Basket()
basket.add_item("Bed", 1)
basket.remove_item("Bed")
