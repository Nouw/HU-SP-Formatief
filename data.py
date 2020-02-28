from pymongo import MongoClient
from pprint import pprint
import re

client = MongoClient('localhost', 27017)

pprint(client.huwebshop.profiles.find_one())

regx = re.compile("^R")

pprint(client.huwebshop.products.find_one({"name": regx}))

products = client.huwebshop.products.find()

total_amount = 0
product_amount = 0

for product in products:
    try:
        total_amount += int(product['price']['mrsp'])
        product_amount += 1

    except KeyError as e:
        print("price not found")

print(product_amount)

mean_price = total_amount / product_amount

print(f"mean price is: {mean_price/100} euro")
