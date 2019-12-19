#*************************************************************************
#@purpose : Read the Json file and calculate the stock price 
#@file : json_inventry_calculate.py
#@author: Vikas Sharma
#*************************************************************************

import json

class StockReport:

    def calculate_stock_price(self):
        
        with open("/home/user/Videos/test/bridgelabz_python/oops_Program/stock_report/json_file/stock_record.json","r") as file:
            stock_data = json.load(file)

            stock_arr = stock_data['Stock']

        for stock_item_dict in stock_arr:  
            stock_price =  stock_item_dict["price_per_stock"]
            stock_item = stock_item_dict["number_of_stock"]
            Stock_name = stock_item_dict["stock_name"]
            stock_total_price = stock_price * stock_item
            print("Name of the stock : {} \nNumber of the stock : {} \nPrice for one stock : {} \nPrice for total stock is {}".format(Stock_name,stock_item,stock_price,stock_total_price))
            print()
               

obj = StockReport()
obj.calculate_stock_price()    
    