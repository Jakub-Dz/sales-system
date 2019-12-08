"""Sales System Project
This sales system is for customer use, not company use.
The company only has one customer.
"""
import json
import tkinter as tk
from tkinter import messagebox, filedialog, END, StringVar, DISABLED, NORMAL  # messagebox needs to be imported separately


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
        if item_name in self.items:
            new_quantity = self.items[item_name][1] + quantity
        else:
            new_quantity = quantity

        self.items[item_name] = (new_quantity * stock.stock_dict[item_name]["price"], new_quantity)

        self.value += quantity * stock.stock_dict[item_name]["price"]

    # Removing item by type completely, quantity edits not implemented
    def remove_item(self, item_name):
        self.value -= self.items[item_name][0]
        del self.items[item_name]


class Transaction:

    def __init__(self, name):
        self.name = name

    def user_details(self):
        pass
        # return self.user.user_name, self.user.wallet
    # if self.stock_dict[item_name]["quantity"] - quantity >= 0:


class SalesGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sales System")
        master.resizable(False, False)
        master.option_add("*Font", "consolas")

        window_size = "800x375"
        window_xpos = int(root.winfo_screenwidth()/2 - 2 * root.winfo_reqwidth())
        window_ypos = int(root.winfo_screenheight()/2 - root.winfo_reqheight())

        master.geometry(f'{window_size}+{window_xpos}+{window_ypos}')
        master.configure(bg="gray95")

        self.var = StringVar()
        self.var.set(f'Basket value: £{basket.value}')

        self.selected_item = None

        # GUI List boxes
        self.stock_control = []  # To access key/index for dict/list
        self.items_lb = None
        self.stock_listbox(stock.stock_dict)

        self.basket_control = []  # To access key/index for dict/list
        self.basket_lb = None
        self.basket_listbox(basket.items)

        self.user_lb = None
        self.user_listbox(user.name, user.wallet)

        # GUI Labels
        self.user_label = tk.Label(master, text="User details:")
        self.user_label.place(x=180, y=0)

        self.stock_label = tk.Label(master, text="Furniture catalogue:")
        self.stock_label.place(x=180, y=55)

        self.basket_top_label = tk.Label(master, text="Your basket:")
        self.basket_top_label.place(x=580, y=55)

        self.basket_total_label = tk.Label(master, textvariable=self.var)
        self.basket_total_label.place(x=535, y=285)

        # GUI Buttons
        self.remove_button = tk.Button(master, text="Remove Item", command=self.remove)
        self.remove_button.config(width=25, height=1, bg="red")
        self.remove_button.place(x=520, y=320)

        self.checkout_button = tk.Button(master, text="CHECKOUT", command=self.test)
        self.checkout_button.config(width=25, height=1, bg="lightblue")
        self.checkout_button.place(x=520, y=15)

        self.add_button = tk.Button(master, text="Add to basket", command=self.add)
        self.add_button.config(width=25, height=1, bg="palegreen")
        self.add_button.place(x=135, y=320)

        #  listbox https://stackoverflow.com/questions/15672552/python-tkinter-listbox-get-active-method
        #  http://zetcode.com/tkinter/widgets/
        #  https://stackoverflow.com/questions/34276663/tkinter-gui-layout-using-frames-and-grid

    def greet(self):
        print("Greetings!")

    def test(self):
        tk.messagebox.showinfo("Test", "Test2")

    def user_listbox(self, name, wallet):
        self.user_lb = tk.Listbox(self.master)
        self.user_lb.insert(END, f'Name: {name}  |  Funds available: £{wallet}')

        self.user_lb.config(width=49, height=1)
        self.user_lb.place(x=40, y=25)

    def stock_listbox(self, items_dict):
        self.items_lb = tk.Listbox(self.master)

        for item in items_dict:
            text_item = f'{item:16}'
            text_price = f'Price: £{items_dict[item]["price"]:<6}'
            text_qty = f'Available: {items_dict[item]["quantity"]}'
            self.items_lb.insert(END, f'{text_item} | {text_price} | {text_qty}')
            self.stock_control.append(item)
            if items_dict[item]["quantity"] == 0:
                self.items_lb.itemconfig(END, fg="red")

        self.items_lb.bind("<<ListboxSelect>>", self.stock_select)
        self.items_lb.config(width=49)
        self.items_lb.place(x=40, y=80)

    def basket_listbox(self, basket_list):
        self.basket_lb = tk.Listbox(self.master)

        for item in basket_list:

            text_item = f'{item[:11]:11}'
            text_price = f'£{basket_list[item][0]:<6}'
            text_qty = f'{basket_list[item][1]}'
            self.basket_lb.insert(END, f'{text_item} | {text_price} | {text_qty}')

            self.basket_control.append(item)

        self.basket_lb.bind("<<ListboxSelect>>", self.basket_select)
        self.basket_lb.config(width=26)
        self.basket_lb.place(x=520, y=80)

    def stock_select(self, val):
        sender = val.widget
        idx = sender.curselection()
        print("stock", idx)
        self.selected_item = self.stock_control[(idx[0])]

    def basket_select(self, val):
        sender = val.widget
        idx = sender.curselection()
        print("basket", idx)
        self.selected_item = self.basket_control[(idx[0])]
        print(self.selected_item)

    def remove(self):
        basket.remove_item(self.selected_item)
        self.basket_control = []
        self.refresh_gui()

    def add(self):
        basket.remove_item(self.selected_item)
        self.basket_control = []
        self.refresh_gui()

    def refresh_gui(self):
        self.basket_lb.delete(0, END)
        self.basket_listbox(basket.items)

        self.items_lb.delete(0, END)
        self.stock_listbox(stock.stock_dict)

        self.var.set(f'Basket value: £{basket.value}')


user = User("Basil Fawlty", 1087.65)  # Hardcoded values as per project's spec
stock = Stock()
basket = Basket()

basket.add_item("Bed", 1)
basket.add_item("Bed", 1)
basket.add_item("Chest of Drawers", 1)
basket.add_item("Chest of Drawers", 1)
stock.remove("Bed", 1)
stock.remove("Chest of Drawers", 1)

root = tk.Tk()
my_gui = SalesGUI(root)
root.mainloop()
# while True:
#     root.update()

