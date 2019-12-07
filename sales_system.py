"""Sales System Project
This sales system is for customer use, not company use.
The company only has one customer.
"""
import json
import tkinter as tk
from tkinter import messagebox, filedialog, END, StringVar  # messagebox needs to be imported separately


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
        self.value += self.items[item_name][0]

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
        # http://www.science.smith.edu/dftwiki/images/3/3d/TkInterColorCharts.png

        window_size = "800x400"
        window_xpos = int(root.winfo_screenwidth()/2 - 2 * root.winfo_reqwidth())
        window_ypos = int(root.winfo_screenheight()/2 - root.winfo_reqheight())

        master.geometry(f'{window_size}+{window_xpos}+{window_ypos}')
        master.configure(bg="gray95")

        self.stock_control = []
        self.stock_listbox(stock.stock_dict)

        self.basket_control = []
        self.basket_listbox(basket.items)

        self.var = StringVar()
        self.var.set(f'Basket value: £{basket.value}')

        # GUI Labels
        self.stock_label = tk.Label(master, text="Furniture catalogue:")
        self.stock_label.place(x=180, y=55)

        self.basket_top_label = tk.Label(master, text="Your basket:")
        self.basket_top_label.place(x=580, y=55)

        self.basket_total_label = tk.Label(master, textvariable=self.var)
        self.basket_total_label.place(x=535, y=282)
        # GUI Buttons

        self.remove_button = tk.Button(master, text="Remove Item", command=self.remove)
        self.remove_button.config(width=25, height=1, bg="red")
        self.remove_button.place(x=520, y=320)

        self.greet_button = tk.Button(master, text="    BUY    ", command=self.greet)
        self.greet_button.place(x=0, y=0)

        self.close_button = tk.Button(master, text="CANCEL", command=master.quit)
        self.close_button.place(x=0, y=0)

        self.close_test = tk.Button(master, text="Test", command=self.test)
        self.close_test.place(x=0, y=0)
        self.close_test.config(width=1, height=1)

        #  listbox https://stackoverflow.com/questions/15672552/python-tkinter-listbox-get-active-method
        #  http://zetcode.com/tkinter/widgets/
        #  https://stackoverflow.com/questions/34276663/tkinter-gui-layout-using-frames-and-grid

    def greet(self):
        print("Greetings!")

    def test(self):
        tk.messagebox.showinfo("Test", "Test2")

    def stock_listbox(self, items_dict):
        items_lb = tk.Listbox(self.master)

        for item in items_dict:
            text_item = f'{item:16}'
            text_price = f'Price: £{items_dict[item]["price"]:<6}'
            text_qty = f'Available: {items_dict[item]["quantity"]}'
            items_lb.insert(END, f'{text_item} | {text_price} | {text_qty}')
            self.stock_control.append(item)

        items_lb.bind("<<ListboxSelect>>", self.stock_select)
        items_lb.config(width=49)
        items_lb.place(x=40, y=80)

    def basket_listbox(self, basket_list):
        basket_lb = tk.Listbox(self.master)

        for item in basket_list:

            text_item = f'{item[:11]:11}'
            text_price = f'£{basket_list[item][0]:<6}'
            text_qty = f'{basket_list[item][1]}'
            basket_lb.insert(END, f'{text_item} | {text_price} | {text_qty}')

            self.basket_control.append(item)

        basket_lb.bind("<<ListboxSelect>>", self.basket_select)
        basket_lb.config(width=26)
        basket_lb.place(x=520, y=80)

    def stock_select(self, val):
        sender = val.widget
        idx = sender.curselection()
        tk.messagebox.showinfo("Test", self.stock_control[(idx[0])])

    def basket_select(self, val):
        sender = val.widget
        idx = sender.curselection()
        tk.messagebox.showinfo("Test", self.basket_control[(idx[0])])
        # self.selected_item = self.basket_control[(idx[0])]

    def remove(self):
        pass
        # basket.remove_item(self.selected_item)


user = User("Basil Fawlty", 1087.65)  # Hardcoded values as per project's spec
stock = Stock()
basket = Basket()

basket.add_item("Bed", 1)
basket.add_item("Bed", 1)
basket.add_item("Chest of Drawers", 1)
stock.remove("Bed", 1)
stock.remove("Chest of Drawers", 1)

root = tk.Tk()
my_gui = SalesGUI(root)
# root.mainloop()
while True:
    root.update()

