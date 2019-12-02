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


class Basket:

    def __init__(self, value=0):
        self.value = value
        self.items = {}

    def add_item(self, item_name, quantity):
        self.items[item_name] = (quantity, quantity * stock.stock_dict[item_name]["price"])  # requires stock = Stock()
        self.value += self.items[item_name][1]

    def remove_item(self, item_name):
        self.value -= self.items[item_name][1]
        del self.items[item_name]

    def display(self):
        print(self.items)
        print(f'Total basket value: {self.value:.2f}.')


class Transaction:

    def __init__(self, user):
        self.user = user

    def user_details(self):
        return self.user.user_name, self.user.wallet
    # if self.stock_dict[item_name]["quantity"] - quantity >= 0:


stock = Stock()
basket = Basket()
basket.add_item("Sofa", 4)
basket.add_item("Bed", 2)
basket.display()
basket.remove_item("Bed")
basket.display()
