"""This module is for testing solutions, prior to including them in the main sales_system.py
"""


class Item:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class User:

    def __init__(self, user_name, wallet):
        self.user_name = user_name
        self.wallet = wallet

    def check_balance(self, checkout_cost):
        self.wallet -= checkout_cost


user_1 = User("Basil Fawlty", 1267.56)


