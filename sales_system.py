"""Sales System Project
This sales system is for customer use, not company use.
The company only has one customer.
"""
from random import randint
import json

print(randint(0, 5))

with open("stock.json", "r") as json_file:
    data = json.load(json_file)

print(json.dumps(data))
