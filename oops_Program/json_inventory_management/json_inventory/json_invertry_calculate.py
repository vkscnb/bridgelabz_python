#*************************************************************************
#@purpose : Read the Json file and calculate the price of the items
#@file : json_inventry_calculate.py
#@author: Vikas Sharma
#*************************************************************************

import json

def calculate_json_inventory():
    
    with open("/home/user/Videos/test/bridgelabz_python/oops_Program/json_inventory_management/json_program/inventry.json","r") as file:
        inventry_data = json.load(file)
        print(inventry_data)
    global rice_price , pulses_price , wheat_price 
    rice_price = 0
    pulses_price = 0
    wheat_price = 0

    def Price_rice(key):
        for price in key:
            rice_price = rice_price + price["price_per_kg"]

    def Price_pulses(key):
        for price in key:
            pulses_price = pulses_price + price["price_per_kg"]


    def Price_wheat(key):
        for price in key:
            wheat_price = wheat_price + price["price_per_kg"]

    for key in inventry_data["Rice"]:
        print(key)
        Price_rice(key) 

    for key in inventry_data["Pulses"]:
        print(key)   
        Price_pulses(key)

    for key in inventry_data["Wheat"]:
        print(key)
        Price_wheat(key)

    print("price of rice : {} \n price of pulses : {} \n price of wheat : {}".format(rice_price,pulses_price,wheat_price))

if __name__ == "__main__":
    calculate_json_inventory()