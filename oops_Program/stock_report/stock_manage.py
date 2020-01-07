#*************************************************************************
#@purpose : Read the Json file and calculate the stock price 
#@file : stock_manage.py
#@author: Vikas Sharma
#*************************************************************************

#importing json file

import json

class Stock:

    def getStockDetails(self):
        #Reading JSON from a File
        with open("/home/user/Videos/test/bridgelabz_python/oops_Program/stock_report/stock_record.json","r") as f:

            #read string from JSON & storing in variable
            data1= json.load(f)
            #storing key
            data = data1["Stock_report"]
        return data

#creating object of class
stock = Stock()
#storing method return value
a =stock.getStockDetails()
    