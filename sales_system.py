"""Sales System Project
This sales system is for customer use, not company use. The company only has one customer.

Notes:
1. Stock to be read from the *.json file as a dictionary
2. User details are hardcoded, but can be opened for input if needed
3. Ideally GUI would access data only through Transaction class, but that would require additional work
"""
import json
import tkinter as tk
import datetime
import webbrowser
from tkinter import messagebox, END, StringVar, DISABLED, NORMAL


# Stock class -> Loading initial stock from .json file
class Stock:

    def __init__(self):
        with open("stock.json", "r") as stock_file:
            self.stock_dict = json.load(stock_file)

    def remove(self, item_name, quantity):
        self.stock_dict[item_name]["quantity"] -= quantity

    def add(self, item_name, quantity):
        self.stock_dict[item_name]["quantity"] += quantity


# User controls only static input for user name and initial balance
class User:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def check_balance(self, checkout_cost):
        return self.wallet >= checkout_cost

    def update_wallet(self, checkout_cost):
        self.wallet -= checkout_cost


# Basket controls adding/removing + final checkout receipt
class Basket:

    def __init__(self, value=0):
        self.value = value
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            new_quantity = self.items[item_name][1] + quantity
        else:
            new_quantity = quantity

        self.items[item_name] = (new_quantity * stock.stock_dict[item_name]["price"], new_quantity)

        self.value += quantity * stock.stock_dict[item_name]["price"]

    # Removing items one by one, in-basket quantity edits not implemented
    def remove_item(self, item_name, quantity):

        self.value -= quantity * stock.stock_dict[item_name]["price"]
        new_quantity = self.items[item_name][1] - quantity
        if new_quantity == 0:
            del self.items[item_name]
        else:
            self.items[item_name] = (new_quantity * stock.stock_dict[item_name]["price"], new_quantity)

        if not self.items:
            self.value = 0

    def is_item_in_basket(self, item_name):
        return item_name in self.items

    def save_rec(self):
        time = str(datetime.datetime.now())
        time = time.replace(":", "-")
        with open(f"{time}.txt", "w") as basket_file:
            basket_file.write(f"On {datetime.date.today()}, {user.name} spent {basket.value:.2f} GBP to purchase:\n")
            for item in self.items:
                basket_file.write(f"Item name: {item} | Quantity: {self.items[item][1]}\n")
        webbrowser.open(f"{time}.txt")


# Transaction class acts as a static container: GUI <-> Transaction <-> main Classes
class Transaction:

    def __init__(self):
        pass

    def add_to_basket(self, item_name):
        if self.in_stock(item_name):
            basket.add_item(item_name, 1)
            stock.remove(item_name, 1)

    def remove_from_basket(self, item_name, quantity):
        if basket.is_item_in_basket(item_name):
            basket.remove_item(item_name, quantity)
            stock.add(item_name, quantity)

    def in_stock(self, item_name):
        return stock.stock_dict[item_name]["quantity"] > 0

    def checkout(self):
        if user.check_balance(basket.value):
            user.update_wallet(basket.value)
            basket.save_rec()
            basket.items.clear()
            basket.value = 0
        else:
            tk.messagebox.showinfo("Funds warning", "You don't have enough money")


class SalesGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sales System")
        master.resizable(False, False)  # disable resizing
        master.option_add("*Font", "consolas 12")  # set font to consolas for even characters width

        # draw GUI at the centre of the screen
        window_size = "800x375"
        window_xpos = int(root.winfo_screenwidth()/2 - 2 * root.winfo_reqwidth())
        window_ypos = int(root.winfo_screenheight()/2 - root.winfo_reqheight())

        master.geometry(f'{window_size}+{window_xpos}+{window_ypos}')
        master.configure(bg="gray95")

        # GUI Labels
        self.user_label = tk.Label(master, text="User details:")
        self.user_label.place(x=180, y=0)

        self.stock_label = tk.Label(master, text="Furniture catalogue:")
        self.stock_label.place(x=180, y=55)

        self.basket_top_label = tk.Label(master, text="Your basket:")
        self.basket_top_label.place(x=580, y=55)

        self.text_basket_total = StringVar()
        self.text_basket_total.set(f'Basket value: £{basket.value:.2f}')
        self.basket_total_label = tk.Label(master, textvariable=self.text_basket_total)
        self.basket_total_label.place(x=535, y=285)

        # GUI Buttons initial state
        self.remove_button = tk.Button(master, text="Remove item", command=self.remove)
        self.remove_button.config(width=26, height=1, bg="gray", state=DISABLED)
        self.remove_button.place(x=520, y=320)

        self.checkout_button = tk.Button(master, text="CHECKOUT", command=self.checkout)
        self.checkout_button.config(width=26, height=1, bg="gray", state=DISABLED)
        self.checkout_button.place(x=520, y=15)

        self.add_button = tk.Button(master, text="Add to basket", command=self.add)
        self.add_button.config(width=26, height=1, bg="gray", state=DISABLED)
        self.add_button.place(x=135, y=320)

        self.help_button = tk.Button(master, text="Help", command=self.help)
        self.help_button.config(width=5, height=1, bg="gold", font="consolas 12")
        self.help_button.place(x=40, y=320)

        # GUI List boxes & declare control variables
        self.stock_idx = None
        self.stock_selected_item = None
        self.stock_control = []  # To access key/index for dict/list
        self.items_lb = None
        self.stock_listbox(stock.stock_dict)

        self.basket_idx = None
        self.basket_selected_item = None
        self.basket_control = []  # To access key/index for dict/list
        self.basket_lb = None
        self.basket_listbox(basket.items)

        self.user_lb = None
        self.user_listbox(user.name, user.wallet)

    def user_listbox(self, name, wallet):
        self.user_lb = tk.Listbox(self.master)
        self.user_lb.insert(END, f'Name: {name}  |  Funds available: £{wallet:.2f}')

        self.user_lb.config(width=49, height=1)
        self.user_lb.place(x=40, y=25)

        self.user_lb.bindtags((self.user_lb, self.master, "all"))  # disable LB selection

    def stock_listbox(self, items_dict):
        self.items_lb = tk.Listbox(self.master)
        self.stock_control = []

        for item in items_dict:
            text_item = f'{item:16}'
            price = f'£{items_dict[item]["price"]:.2f}'
            text_price = f'Price: {price:>7}'
            text_qty = f'Available: {items_dict[item]["quantity"]:>2}'
            self.items_lb.insert(END, f'{text_item} | {text_price} | {text_qty}')
            self.stock_control.append(item)
            if items_dict[item]["quantity"] == 0:
                self.items_lb.itemconfig(END, fg="red")

        self.items_lb.bind("<<ListboxSelect>>", self.stock_select)
        self.items_lb.config(width=49)
        self.items_lb.place(x=40, y=80)

    def basket_listbox(self, basket_list):
        self.basket_lb = tk.Listbox(self.master)
        self.basket_control = []

        for item in basket_list:
            text_item = f'{item[:11]:11}'
            text_price = f'£{basket_list[item][0]:.2f}'
            text_qty = f'{basket_list[item][1]:>2}'
            self.basket_lb.insert(END, f'{text_item} | {text_price:>8} | {text_qty}')
            self.basket_control.append((item, basket_list[item][1]))

        self.basket_lb.bind("<<ListboxSelect>>", self.basket_select)
        self.basket_lb.config(width=27)
        self.basket_lb.place(x=520, y=80)

        # checkout disable when basket empty
        if self.basket_control:
            self.checkout_button.config(width=25, height=1, bg="lightblue", state=NORMAL)
        else:
            self.checkout_button.config(width=25, height=1, bg="gray", state=DISABLED)

    def stock_select(self, val):
        sender = val.widget
        self.stock_idx = sender.curselection()
        self.stock_selected_item = None

        # check if listbox is contains elements
        if self.stock_idx:
            self.remove_button.config(bg="gray", state=DISABLED)
            self.add_button.config(bg="palegreen", state=NORMAL)
            self.stock_selected_item = self.stock_control[(self.stock_idx[0])]

            if not transaction.in_stock(self.stock_selected_item):
                self.add_button.config(bg="gray", state=DISABLED)

    def basket_select(self, val):
        sender = val.widget
        self.basket_idx = sender.curselection()
        self.basket_selected_item = None

        # check if listbox contains elements
        if self.basket_idx:
            self.basket_selected_item = self.basket_control[(self.basket_idx[0])]
            self.remove_button.config(bg="red", state=NORMAL)
            self.add_button.config(bg="gray", state=DISABLED)

    # Remove from basket via Transaction, reload widgets, re-select previously added item
    def remove(self):
        transaction.remove_from_basket(self.basket_selected_item[0], 1)
        self.refresh_gui()

        # Disable button if basket empty
        if basket.items:
            self.remove_button.config(bg="red", state=NORMAL)
        else:
            self.remove_button.config(bg="gray", state=DISABLED)

        # Don't select if item no longer exists
        if self.basket_selected_item[0] in basket.items:
            self.basket_lb.selection_set(self.basket_idx)

    # Add to basket via Transaction, reload widgets, re-select previously added item
    def add(self):
        transaction.add_to_basket(self.stock_selected_item)
        self.refresh_gui()
        self.items_lb.selection_set(self.stock_idx)

    def checkout(self):
        transaction.checkout()
        self.refresh_gui()

    def refresh_gui(self):
        self.basket_lb.delete(0, END)
        self.basket_listbox(basket.items)

        self.items_lb.delete(0, END)
        self.stock_listbox(stock.stock_dict)

        self.user_lb.delete(0, END)
        self.user_listbox(user.name, user.wallet)

        self.text_basket_total.set(f'Basket value: £{basket.value:.2f}')

        # Check basket total vs wallet
        if basket.value > user.wallet:
            self.basket_total_label.config(fg="red")
        else:
            self.basket_total_label.config(fg="black")

    def help(self):
        tk.messagebox.showinfo("Help", "Instructions:\n\n"
                                       "1. Select an item from the Furniture Catalogue\n\n"
                                       "2. Click <Add to basket> button to add 1 item to the basket\n\n"
                                       "3. To remove 1 item from the basket, select and click <Remove item>\n\n"
                                       "4. Once there's at least 1 item in the Basket, <CHECKOUT> becomes available\n\n"
                                       "5. To checkout you need to have enough money in the 'wallet'\n\n"
                                       "6. Receipt appears after checkout and automatically saved in the main folder")


#  Main classes init and GUI loop
user = User("Basil Fawlty", 1087.65)  # Hardcoded values as per project's specs
stock = Stock()
basket = Basket()
transaction = Transaction()

# GUI main loop
root = tk.Tk()
gui = SalesGUI(root)
root.mainloop()
