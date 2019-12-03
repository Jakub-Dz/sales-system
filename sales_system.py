"""Sales System Project
This sales system is for customer use, not company use.
The company only has one customer.
"""
import json
import tkinter as tk


class Item:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Stock:

    def __init__(self):
        with open("stock.json", "r") as stock_file:
            self.stock_dict = json.load(stock_file)

    def remove(self, item_name, quantity):
        self.stock_dict[item_name]["quantity"] -= quantity

    def save(self):
        with open("stock.json", "w") as stock_file:
            json.dump(self.stock_dict, stock_file, indent=3)


class User:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def check_balance(self, checkout_cost):
        return self.wallet >= checkout_cost

    def update_wallet(self, checkout_cost):
        self.wallet -= checkout_cost


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


class Transaction:

    def __init__(self, name):
        self.name = name

    def user_details(self):
        pass
        # return self.user.user_name, self.user.wallet
    # if self.stock_dict[item_name]["quantity"] - quantity >= 0:


class GUI:

    def __init__(self, *args, **kwargs):
        pass


user = User("Basil Fawlty", 1087.65)  # Hardcoded values as per project's spec
stock = Stock()
basket = Basket()
gui = GUI()  # https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application

# Testing only
print(f'Username: {user.name}\nFunds available: £{user.wallet:.2f}')
print(f'Number of items in the basket: {len(basket.items)}\nTotal value: £{basket.value:.2f}')
for item in stock.stock_dict:
    print(f'{item} | Price: £{stock.stock_dict[item]["price"]} | Qty: {stock.stock_dict[item]["quantity"]}')

basket.add_item("Bed", 1)
stock.remove("Bed", 1)
print(f'Number of items in the basket: {len(basket.items)}\nTotal value: £{basket.value:.2f}')
for item in stock.stock_dict:
    print(f'{item} | Price: £{stock.stock_dict[item]["price"]} | Qty: {stock.stock_dict[item]["quantity"]}')