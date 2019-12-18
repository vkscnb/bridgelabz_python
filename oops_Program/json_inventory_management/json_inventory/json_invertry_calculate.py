#*************************************************************************
#@purpose : Read the Json file and calculate the price of the items
#@file : json_inventry_calculate.py
#@author: Vikas Sharma
#*************************************************************************

try:
    import json
except ImportError:
    print("import error")

def calculate_json_inventory():
    
    with open("/home/user/Videos/test/bridgelabz_python/oops_Program/json_inventory_management/json_program/inventry.json","r") as file:
        inventry_data = json.load(file)

        wheat_arr = inventry_data['Wheat']
        rice_arr = inventry_data['Rice']
        pulses_arr = inventry_data['Pulses']

    rice_price = 0
    pulses_price = 0
    wheat_price = 0
    try:

        for rice_item_dict in rice_arr:  
            rice_price = rice_price + rice_item_dict["price_per_kg"]
        

        for pulses_item_dict in pulses_arr:  
            pulses_price = pulses_price + pulses_item_dict["price_per_kg"]
        

        for wheat_item_dict in wheat_arr:
            wheat_price = wheat_price + wheat_item_dict["price_per_kg"]       

    except TypeError:
        
        print("type error")

        print("price of rice : {} \nprice of pulses : {} \nprice of wheat : {}".format(rice_price,pulses_price,wheat_price))

if __name__ == "__main__":
    calculate_json_inventory()
    