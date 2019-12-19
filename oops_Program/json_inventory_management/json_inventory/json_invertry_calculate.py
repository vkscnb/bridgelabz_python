#*************************************************************************
#@purpose : Read the Json file and calculate the price of the items
#@file : json_inventry_calculate.py
#@author: Vikas Sharma
#*************************************************************************

import json

class InventoryManagement: 

    def calculate_inventory_price(self):
        
        with open("/home/user/Videos/test/bridgelabz_python/oops_Program/json_inventory_management/json_program/inventry.json","r") as file:
            inventry_data = json.load(file)

            wheat_arr = inventry_data['Wheat']
            rice_arr = inventry_data['Rice']
            pulses_arr = inventry_data['Pulses']

        rice_price = 0
        pulses_price = 0
        wheat_price = 0

        for rice_item_dict in rice_arr:  
            rice_price = rice_price + rice_item_dict["price_per_kg"]
            

        for pulses_item_dict in pulses_arr:  
            pulses_price = pulses_price + pulses_item_dict["price_per_kg"]
            

        for wheat_item_dict in wheat_arr:
            wheat_price = wheat_price + wheat_item_dict["price_per_kg"]       


        print("Total price of rice : {} \nTotal price of pulses : {} \nTotal price of wheat : {}".format(rice_price,pulses_price,wheat_price))

        json_string = json.dumps("/home/user/Videos/test/bridgelabz_python/oops_Program/json_inventory_management/json_program/inventry.json")
        
        with open("/home/user/Videos/test/bridgelabz_python/oops_Program/json_inventory_management/json_program/update.json","w") as f:
            json.dump(inventry_data, f, indent = 4)
        print(json_string)

obj = InventoryManagement()
obj.calculate_inventory_price()    
    