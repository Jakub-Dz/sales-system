
# 1. First task: Sales System Project

:hammer: Link to the main Python file: **[sales_system.py](https://github.com/Jakub-Dz/sales-system/blob/master/sales_system.py)**

:calling: Link to the compiled version (use sales_system.exe after unpacking): **[sales_system.zip](https://github.com/Jakub-Dz/sales-system/blob/master/sales_system.zip)**


# 2. Second task: Match Point Assets

Macro-enabled spreadsheet can be downloaded from here: **[Problem2.xlsm](https://github.com/Jakub-Dz/sales-system/blob/master/Problem2.xlsm)**

Source code can be viewed here: **[Problem2.bas](https://github.com/Jakub-Dz/sales-system/blob/master/Problem2.bas)**
___
***

## 1.1 First Task description
**The system must:**
- [x] Keep an inventory of stock items and their cost
- [x] Allow the customer to view the current quantity and cost of each item 
- [x] Allow the customer to see their current balance
- [x] Allow the customer to purchase an item if it is both in stock and they have enough money to do so
- [x] Inform the customer if they do not have enough money to purchase an item
- [x] Inform the customer if an item is out of stock
- [x] When an item has been purchased:
- [x] Update the inventory
- [x] Update the customer’s balance

**Additional features:**
- [x] Basket
- [x] Saving receipts
- [x] Inventory from .json

**Improvement for the next revision:**
- [ ] Store prices as integers instead of floats
- [ ] Make GUI resizable, use grid & sticky property
- [ ] ...

**Note: This sales system is for customer use, not company use.**

## 1.2 First Task Implementation

Assumptions:

| Core functionality | GUI |
| :--- |:---|
| Attempt OOP & interactions via Transaction class | tkinter simple GUI, based on **[this sketch](https://wireframepro.mockflow.com/view/Mb007c13b48670f65df9aca01fa0e4e411575378753417)** |

Execution:

| Classes | Methods | Description |
| :--- |:---|:---|
| Stock | Init <br> Add <br> Remove | Load stock as a dict from .json <br> Return items from Basket to Stock <br> Remove items from stock when adding to basket |
| Basket | Add | Adds items from stock to basket instance |
