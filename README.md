
# 1. First task: Sales System Project
_Test Project, can be built in any language (.NET preferred)._

Link to the main Python file: **[sales_system.py](https://github.com/Jakub-Dz/sales-system/blob/master/sales_system.py)**

GUI mock-up: **[WireFrame Online](https://wireframepro.mockflow.com/view/Mb007c13b48670f65df9aca01fa0e4e411575378753417)**

Trello board: https://trello.com/b/rt5U3gq3/sales-system


# 2. Second task: Match Point Assets
_Two data sets provided, the output is expected to be a list of Set1 UID alongside the corresponding UID from Set2._

_The problem should be carried out using VBA or a similar programming language._

Macro-enabled spreadsheet can be downloaded from here: **[Problem2.xlsm](https://github.com/Jakub-Dz/sales-system/blob/master/Problem2.xlsm)**

Source code can be viewed here: **[Problem2.bas](https://github.com/Jakub-Dz/sales-system/blob/master/Problem2.bas)**
___
***

## 1.1 First Task description
**The system must:**
- Keep an inventory of stock items and their cost
- Allow the customer to view the current quantity and cost of each item 
- Allow the customer to see their current balance
- Allow the customer to purchase an item if it is both in stock and they have enough money to do so
- Inform the customer if they do not have enough money to purchase an item
- Inform the customer if an item is out of stock
- When an item has been purchased:
- Update the inventory
- Update the customer’s balance

**Note: This sales system is for customer use, not company use.**

## 1.2 First Task Implementation

Assumptions:

| Core functionality | GUI |
| :--- |:---|
| Attempt OOP & interactions via Transaction class | tkinter simple GUI, based on **[this sketch](https://wireframepro.mockflow.com/view/Mb007c13b48670f65df9aca01fa0e4e411575378753417)** |

| Classes | Methods | Description |
| :--- |:---|:---|
| Stock | Init <br> Add <br> Remove | Load stock as a dict from .json <br> Return items from Basket to Stock <br> Remove items from stock when adding to basket |
| Basket | Add | Adds items from stock to basket instance |
